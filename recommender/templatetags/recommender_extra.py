from django import template

register = template.Library()

@register.filter
def get(dict, key):
    return dict[key]
