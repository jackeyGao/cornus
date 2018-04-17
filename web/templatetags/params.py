from copy import deepcopy
from urllib import urlencode
from django import template

register = template.Library()


@register.simple_tag(name='remove_render')
def remove_render(params, _type, value):
    params = deepcopy(params)
    params['w'] = [params['w']]
    if str(value) in params[_type]:
        params[_type].remove(str(value))
    return urlencode(params, doseq=True)


@register.simple_tag(name="append_render")
def append_render(params, _type, value):
    params = deepcopy(params)
    params['w'] = [params['w']]
    if str(value) not in params[_type]:
        params[_type].append(str(value))
    return urlencode(params, doseq=True)
