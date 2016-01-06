from django import template

from ..models import SmartPage

register = template.Library()


@register.simple_tag(takes_context=True)
def smartpage_url(context, value, lang=None):
    try:
        page = SmartPage.objects.get(code=value)
        result = page.get_absolute_url()
    except SmartPage.DoesNotExist:
        result = '/error/SmartPage.DoesNotExist/%s/' % value
    return result
