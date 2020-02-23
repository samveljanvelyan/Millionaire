from django import template

register = template.Library()


@register.filter
def get_at_index(custom_l, index):
    """# Registering list indexing functionality."""
    return custom_l[index]


@register.tag('++')
def increment_var(parser, token):
    """This template tag allows to increment a variable within a template using ++ operator."""
    parts = token.split_contents()
    if len(parts) < 2:
        raise template.TemplateSyntaxError(
            "'increment' tag must be of the form:  {% increment <var_name> %}")
    return Increment(parts[1])


class Increment(template.Node):

    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        try:
            value = context[self.var_name]
            context[self.var_name] = value + 1
            return u""
        except:
            raise template.TemplateSyntaxError("The variable does not exist.")
