from django.contrib.sites.models import Site
from django.contrib.syndication.feeds import Feed
from django.core.urlresolvers import reverse
from tagging.models import Tag, TaggedItem
from blog.models import Post, Category
import datetime

class BasePostFeed(Feed):
  _site = Site.objects.get_current()

  title_template = 'feeds/posts_title.html'
  description_template = 'feeds/posts_description.html'

  def _site_name(self):
    return BasePostFeed._site.name

  def item_pubdate(self, item):
    return item.publish

class CategoryPostFeed(BasePostFeed):

  def get_object(self, bits):
    if len(bits) != 1:
      raise ObjectDoesNotExist
    return Category.objects.get(slug__exact=bits[0])

  def title(self, obj):
    return "%s: %s" % (BasePostFeed._site.name, obj.title)

  def description(self, obj):
    return "%s: %s posts feed." % (BasePostFeed._site.name, obj.title)

  def link(self, obj):
    return obj.get_absolute_url()

  def items(self, obj):
    return obj.post_set.published()[:10]

class TagPostFeed(BasePostFeed):

  def get_object(self, bits):
    if len(bits) != 1:
      raise ObjectDoesNotExist
    tags = bits[0].split('+')
    self.tags_exist = (Post.tagging.filter(name__in=tags).count() == len(tags))
    return tags

  def title(self, obj):
    return "%s: %s" % (BasePostFeed._site.name, ', '.join(obj))

  def description(self, obj):
    return "%s: %s posts feed." % (BasePostFeed._site.name, ', '.join(obj))

  def link(self, obj):
    return reverse('tag_index', None, {'tag': '+'.join(obj)} )

  def items(self, obj):
    # `with_all()` method doesn't check if the supplied tags are valid,
    # it silently doesn't use them. The results are broken.
    # We workaround the issue by using `tags_exist`.
    if self.tags_exist:
      posts = Post.tagged.with_all(obj).filter(
        status__gte=2, publish__lte=datetime.datetime.now())
    else:
      posts = []
    return posts

