from django import template
from lanata.glue.forms import NoMarkupForm

def do_get_nomarkup_comment_form(parser, token):
    """
    Gets a NoMarkupCommentForm and inserts it into the context.
    """
    error_message = "%r tag must be of format {%% %r as CONTEXT_VARIABLE %%}" % (token.contents.split()[0], token.contents.split()[0])
    try:
        split = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, error_message
    if split[1] != 'as':
        raise template.TemplateSyntaxError, error_message
    if len(split) != 3:
        raise template.TemplateSyntaxError, error_message
    return ThreadedCommentFormNode(split[2])

class ThreadedCommentFormNode(template.Node):
    def __init__(self, context_name):
        self.context_name = context_name

    def render(self, context):
        context[self.context_name] = NoMarkupForm()
        return ''

register = template.Library()
register.tag('get_nomarkup_comment_form', do_get_nomarkup_comment_form)
