This is the code of my weblog, feel free to use!

It consists of a few bits of code plus some templates.

The weblog uses some great apps developed by other djangonauts,
some of these apps are slightly modified for my needs, most of the
patches have been sent upstream.

Requirements
  * blog
  * tagging
  * threadedcomments
  * comment_utils
  * localdates
  * markuputils

Templates

The templates use the blueprint css framework. You have to install in
order to use them.

All these apps are loosely-coupled and it's easy to remove anything 
you don't find useful.

Any ideas/patches/bugs-reports are more than welcome.

Instalation

$ easy_install Django django-localdates feedparser \
markdown2 pygments markuputils

$ easy_install -f \
http://www.crummy.com/software/BeautifulSoup/download/3.x/ \
'Beautifuoup==3.0.7a'

$ easy_install -f http://ctrochalakis.org/basket/ basic \
tagging template_utils comment_utils-lanata django-threadedcomments-lanata

$ easy_install -f http://code.google.com/p/django-comment-utils/downloads/list comment_utils

#Devel
$ easy_install -f http://ctrochalakis.org/basket/ django_extensions
$ easy_install Werkzeug

-- 
Christos Trochalakis <yatiohi /at/ ideopolis.gr>
