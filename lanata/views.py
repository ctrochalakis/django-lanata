from django.contrib.syndication.views import feed
from django.views.generic.simple import redirect_to

def slug_feed(request, slug=None, param='', feed_dict=None):
    if slug:
        url = "%s/%s" % (slug, param)
    else:
        url = param
    return feed(request, url, feed_dict)

def alias_redirect(request, base, suffix):
    return redirect_to(request, base + suffix)
