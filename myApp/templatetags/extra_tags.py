from django import template

register = template.Library()

@register.filter(name = "cut")

def cut(value, arg):

	""" 
	Cuts the given value from the variable provided
	"""

	return value.replace(arg, "")