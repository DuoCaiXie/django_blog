from django.conf.urls import url

from blog import views
from blog.feeds import AllPostsRssFeed

'''
对于类视图
第二个参数传入的值必须是一个函数。而 IndexView 是一个类，
不能直接替代 index 函数。好在将类视图转换成函数视图非常简单
'''
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    # url(r'^/index/$',views.index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^categorys/$', views.categorys, name='categorys'),
    url(r'^tags/$', views.tags, name='tags'),
    url(r'^search/$', views.search, name='search'),
    # url(r'^all/rss/$', AllPostsRssFeed(), name='rss')
]

