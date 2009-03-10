from django.conf.urls.defaults import * 
from django.conf import settings
from basic.blog.models import Post
from basic.blog.feeds import BlogPostsFeed
from feeds import CategoryPostFeed, TagPostFeed
from tagging.views import tagged_object_list

from django.contrib import admin
admin.autodiscover()

feeds = {
    'posts': BlogPostsFeed,
    'categories': CategoryPostFeed,
    'tags': TagPostFeed,
}

def published_posts():
    return Post.objects.published()

urlpatterns = patterns('',
    ('^$', 'django.views.generic.simple.redirect_to', {'url' : '/blog/'}),
    (r'^admin/(.*)', admin.site.root),
    url(r'^blog/tags/(?P<tag>[^/]+)/$',
        tagged_object_list,
        dict(queryset_or_model=published_posts(), paginate_by=10, allow_empty=True, template_name='blog/tag_detail.html'),
        name='tag_index'
    ),
    url(r'^blog/', include('basic.blog.urls')),
    (r'^threadedcomments/', include('threadedcomments.urls')),
    (r'^(?P<url>pages/.*/)$', 'django.contrib.flatpages.views.flatpage'),
    url(r'^feeds/posts/$', 'views.slug_feed',
        {'feed_dict': feeds, 'slug': 'posts'}, name='bblog_posts_feed'),
    url(r'^feeds/categories/(?P<param>.*)/$', 'views.slug_feed',
        {'feed_dict': feeds, 'slug':'categories'}, name='bblog_category_feeds'),
    url(r'^feeds/tags/(?P<param>.*)/$', 'views.slug_feed',
        {'feed_dict': feeds, 'slug':'tags'}, name='bblog_tag_feeds'),
    (r'^i18n/', include('django.conf.urls.i18n')),
)

if settings.SERVE_STATIC:
    urlpatterns += patterns('',
        (r'static/css/bp/(?P<suffix>.*)$', 'lanata.views.alias_redirect',
            {'base' : 'http://blueprintcss.org/blueprint/'}
        ),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),
    )

