from django.template import Library

register = Library()
oldrange = range

@register.filter(name="range")
def range(value):
    """
    Filter - returns a list containing range made from given value
    Usage (in template): (verbatim tags to account for start project)
    {% verbatim %}
    <ul>{% for i in 3|range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>
    {% endverbatim %}


    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>
    Instead of 3 one may use the variable set in the views
    """
    return oldrange(value)
