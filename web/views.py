# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging, copy
from collections import defaultdict
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.validators import validate_email, ValidationError
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.files import File
from web.models import Tag, Poetry, List, Author, User, Profile
from web.forms import ProfileAvatarForm, ProfileEditForm
from web.forms import ListForm

validate_username = ASCIIUsernameValidator()


BRS = ('？', '。', '！')


def auto_content(p, lines=None):
    p.content = p.content.replace('？', '？\n')
    p.content = p.content.replace('。', '。\n')
    p.content = p.content.replace('！', '！\n')
            
    paragraphs = []
    for i in p.content.split('\n'):
        if i.strip():
            paragraphs.append(i)

    if lines:
        p.content = '\n'.join(paragraphs[0:lines])
    else:
        p.content = '\n'.join(paragraphs)
    return p


def init_user(user):
    Profile.objects.filter(user=user).update(
        avatar='avatar/default.png', nick=user.username
    )


class SearchListView(TemplateView):
    template_name = 'web/list_detail.html'

    def validate(self):
        params = {}
        params["w"] = self.request.GET.get('w', '')
        params["a"] = self.request.GET.getlist('a')
        params["d"] = self.request.GET.getlist('d')
        params["t"] = self.request.GET.getlist('t')
        return params

    def get_context_data(self, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)
        params = self.validate()
        raw_params = copy.deepcopy(params)
        
        if params['w']:
            qs = Poetry.objects.filter(
                Q(content__contains=params['w']) |
                Q(dynasty__contains=params['w']) |
                Q(title__contains=params['w']) |
                Q(author__name__contains=params['w'])
            )

        else:
            if 't' in params:
                params['t'] = Tag.objects.filter(pk__in=params['t'])
                qs = Poetry.objects.filter(tags__in=params['t'])
            else:
                qs = []

        # 所有统计参数在这里
        context["raw_params"] = raw_params
        context["authors"] = list(set([ p.author for p in qs ]))
        context["dynasty"] = list(set([ p.dynasty for p in qs ]))
        context["tags"] = list(set([ t for p in qs for t in p.tags.all() ]))

        # author filter
        if params['a']:
            params['a'] = Author.objects.filter(pk__in=params['a'])
            qs = qs.filter(author__in=params['a']) 
        
        # dynasty filter
        if params['d']:
            qs = qs.filter(dynasty__in=params['d'])

        # 处理格式
        poetrys = []
        for i in qs:
            poetrys.append(auto_content(i, 4))

        context["type"] = 'search'
        context['poetrys'] = qs
        context['params'] = params
        return context
    

class ListDetailView(DetailView):
    model = List

    def get_context_data(self, **kwargs):
        context = super(ListDetailView, self).get_context_data(**kwargs)
        obj = context["object"]
        poetrys = []
        for i in obj.poetrys.all():
            poetrys.append(auto_content(i, 4))

        context["type"] = 'list'
        context["poetrys"] = poetrys
        return context
 

class IndexListView(ListView):
    model = List
    

class PoetryDetailView(DetailView):
    model = Poetry
    
    def post(self, request, *args, **kwargs):
        list_id = request.POST.get('list', None)
        if not list_id:
            messages.error(request, '缺少诗集')
            return self.get(request)

        try:
            l = List.objects.get(pk=int(list_id))
        except List.DoesNotExist as e:
            messages.error(request, '诗集不存在')
            return self.get(request)

        obj = self.get_object()
        action = request.POST.get('action', '')
        if action == 'add':
            messages.success(request, '添加成功')
            l.poetrys.add(obj)
            l.save()
        elif action == 'remove':
            messages.success(request, '移除成功')
            l.poetrys.remove(obj)
            l.save()
        else:
            messages.error(request, '未知的操作类型')
            return self.get(request)

        return self.get(request)

    def get_context_data(self, **kwargs):
        context = super(PoetryDetailView, self).get_context_data(**kwargs)
        context["poetry"] = auto_content(context["poetry"])
        if self.request.user.is_authenticated:
            context["lists"] = List.objects.filter(owner=self.request.user)
        return context


class AboutView(TemplateView):
    template_name = 'web/about.html'


class LoginView(TemplateView):
    template_name = 'web/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return super(LoginView, self).get(request, *args, **kwargs)
        

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, '账户不匹配')
            return HttpResponseRedirect('/login/')

        if not user.is_active:
            messages.error(request, '账户没有激活')
            return HttpResponseRedirect('/login/')
        

        auth.login(request, user)
        return HttpResponseRedirect('/')

class RegisterView(TemplateView):
    template_name = 'web/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return super(RegisterView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        c_password = request.POST.get('c_password', '').strip()
        
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, '不合法的邮箱地址')
            return HttpResponseRedirect('/register/')

        try:
            validate_username(username)
        except ValidationError as e:
            messages.error(request, '仅支持英文，数字和@/./+/-/_符号')
            return HttpResponseRedirect('/register/')
        
        try:
            if password != c_password:
                messages.error(request, '密码不一致')
                return HttpResponseRedirect('/register/')

            user = User.objects.filter(username=username.strip())
            if user.exists():
                messages.error(request, '用户名已存在')
                return HttpResponseRedirect('/register/')

            user = User.objects.filter(email=email.strip())
            if user.exists():
                messages.error(request, '邮箱已存在')
                return HttpResponseRedirect('/register/')
        
            user = User.objects.create(username=username.strip(), email=email.strip())
            user.set_password(password.strip())
            user.save()
            init_user(user)
            return HttpResponseRedirect('/login/')    
        except Exception as e:
            messages.error(request, str(e))
            return HttpResponseRedirect('/register/')
    

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, '已经登出!')
        return HttpResponseRedirect('/login/')


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        is_edit = request.GET.get('edit', 0)
        is_new = request.GET.get('new', 0)
        lists = List.objects.filter(owner=request.user)
        return render(request, 'web/user.html', locals())

    def post(self, request, *args, **kwargs):
        if 'avatar' in request.FILES:
            form = ProfileAvatarForm(request.POST, request.FILES)
            if form.is_valid():
                user = request.user
                user.profile.avatar = request.FILES["avatar"]
                user.profile.save()
        else:
            form = ProfileEditForm(request.POST, request.FILES)
            if form.is_valid():
                user = request.user
                user.profile.nick = request.POST.get('nick')
                user.profile.bio = request.POST.get('bio')
                user.profile.save()
            
        return HttpResponseRedirect('/me/')



class ListView(View):

    def post(self, request, *args, **kwargs):
        form = ListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.owner = request.user
            form.save()
        
        return HttpResponseRedirect('/me/')
