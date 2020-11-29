from django import template

register = template.Library()

@register.filter
def format_text(value):
    return value.replace("-"," ").title()

@register.filter
def to_roman(num):
    if num == 1:
        return 'I'
    elif num == 2:
        return 'II'
    elif num == 3:
        return 'III'
    elif num == 4:
        return 'IV'
    elif num == 5:
        return 'V'
    elif num == 6:
        return 'VI'
    elif num == 7:
        return 'VII'
    elif num == 8:
        return 'VIII'
    elif num == 9:
        return 'IX'
    elif num == 10:
        return 'X'
    