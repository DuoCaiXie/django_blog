from django.conf.urls import url

from comments import views

urlpatterns = [
    url(r'^comment/(?P<post_pk>[0-9]+)/$' ,views.post_comment, name='post_comment')
]