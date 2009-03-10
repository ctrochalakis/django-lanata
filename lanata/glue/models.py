from django.contrib import admin
from django.db.models import get_model

admin.autodiscover()

Post = get_model('blog','post')
PostAdmin = type(admin.site._registry[Post])

class NewPostAdmin(PostAdmin):
    class Media:
        js = ('js/wmd/wmd.js',)

admin.site.unregister(Post)
admin.site.register(Post, NewPostAdmin)

