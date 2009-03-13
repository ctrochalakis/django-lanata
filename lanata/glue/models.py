from django.contrib import admin
from django.db.models import get_model

# Markdown editor
admin.autodiscover()

Post = get_model('blog','post')
PostAdmin = type(admin.site._registry[Post])

class NewPostAdmin(PostAdmin):
    class Media:
        js = ('js/wmd/wmd.js',)

admin.site.unregister(Post)
admin.site.register(Post, NewPostAdmin)

# Comment Moderator

from threadedcomments.moderation import moderator, CommentModerator

class PostModerator(CommentModerator):
    akismet = True
    enable_field = 'allow_comments'
    allowed_markup = (1,) #Markdown

moderator.register(Post, PostModerator)
