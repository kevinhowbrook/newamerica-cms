from datetime import date
from django import template
from django.conf import settings

from programs.models import Program

register = template.Library()

@register.simple_tag()
def listify(i):
	if i >= 2:
		return ","
	elif i == 1:
		return " and"
	else:
		return ""