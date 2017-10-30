from django import template
import re

register = template.Library()

@register.filter()
def cited_html(html):
    html = str(html)
    match = re.search('\{\{([0-9]+)\}\}', html)

    if match is None:
        return html

    number = match.groups()[0]
    citation = '<span class="report__citation" data-citation-number="%s">%s</span>' % (number, number)
    html = html.replace(match.group(), citation)
    return cited_html(html)
