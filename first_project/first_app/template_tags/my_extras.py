from django import template
register = template.Library()

#@register.filter(name='cut')
@register.filter
def cutout(value, arg):
    return value.replace(arg, '')