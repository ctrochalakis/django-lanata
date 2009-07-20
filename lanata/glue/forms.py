from threadedcomments.forms import FreeThreadedCommentForm
from threadedcomments.models import FreeThreadedComment

class NoMarkupForm(FreeThreadedCommentForm):
    class Meta:
        model = FreeThreadedComment
        fields = ('comment', 'name', 'website', 'email',)
