from django import template

register = template.Library()

@register.filter
def make_float(string):
    try:

        string = float(string)
        # if string % 1 == 0:
        #     return str(string)
        if string >= 1900:
            return str(string)
        return string
    except:
        return string

@register.filter
def first_el(el_list):
    return el_list[0]