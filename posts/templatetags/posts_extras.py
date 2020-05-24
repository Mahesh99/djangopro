from django import template

register = template.Library()


@register.filter
def add_str(arg1,arg2):
  return arg1+" "+arg2

@register.filter
def percent(num):
  return num*100

@register.simple_tag
def join_strs(sym,*args):
  return sym.join(args)


@register.inclusion_tag('posts/tags.html')
def dplst(lst):
  return {'lst':lst}

