from django import forms
from web.models import List, User

class ProfileAvatarForm(forms.Form):
    avatar = forms.ImageField(
        label='Select a image'
    )


class ProfileEditForm(forms.Form):
    nick = forms.CharField(label="set a nick")
    bio = forms.CharField(label="set bio", widget=forms.Textarea, required=False)


class CreationListForm(forms.Form):
    name = forms.CharField(label="set a nick")
    intro = forms.CharField(label="set bio", widget=forms.Textarea, required=False)
    avatar = forms.ImageField()


class ListForm(forms.ModelForm):
    owner = forms.ModelChoiceField(queryset=User.objects.all())
    
    class Meta:
        model = List
        fields = ['name', 'cover', 'intro']

