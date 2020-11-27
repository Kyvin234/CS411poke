from django import template

register = template.Library()

@register.filter
def format_text(value):
    return value.replace("-"," ").title()