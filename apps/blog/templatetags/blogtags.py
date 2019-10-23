from django.template.defaulttags import register


@register.filter
def post_preview(text):
    ind = text.find('<!--more-->')
    return text[:ind] if ind != -1 else text
