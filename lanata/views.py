from django.contrib.syndication.views import feed

def slug_feed(request, slug=None, param='', feed_dict=None):
    if slug:
        url = "%s/%s" % (slug, param)
    else:
        url = param
    return feed(request, url, feed_dict)

