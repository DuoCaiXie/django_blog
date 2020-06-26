from django.contrib.gis.feeds import Feed

from blog.models import Post


class AllPostsRssFeed(Feed):
    title = "Django 博客教程演示项目"
    # 显示在聚合阅读器上的描述信息
    description = "Django 博客教程演示项目测试文章"

    # 需要显示的内容条目
    def items(self):
        return Post.objects.all()
        # 聚合器中显示的内容条目的标题

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

        # 聚合器中显示的内容条目的描述

    def item_description(self, item):
        return item.body