from django.conf.urls.defaults import * 
from django.conf import settings
from blog.models import Post
from blog.feeds import BlogPostFeed
from feeds import CategoryPostFeed, TagPostFeed
from tagging.views import tagged_object_list

feeds = {
    'posts': BlogPostFeed,
    'categories': CategoryPostFeed,
    'tags': TagPostFeed,
}

urlpatterns = patterns('',
    ('^$', 'django.views.generic.simple.redirect_to', {'url' : '/blog/'}),
    (r'^admin/', include('django.contrib.admin.urls')),
    url(r'^blog/tags/(?P<tag>[^/]+)/$',
        tagged_object_list,
        dict(queryset_or_model=Post.objects.published(), paginate_by=10, allow_empty=True, template_name='blog/tag_detail.html'),
        name='tag_index'
    ),
    (r'^blog/', include('blog.urls')),
    (r'^threadedcomments/', include('threadedcomments.urls')),
    (r'^(?P<url>pages/.*/)$', 'django.contrib.flatpages.views.flatpage'),
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}, name='bblog_feeds'),
    (r'^i18n/', include('django.conf.urls.i18n')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),
    )
