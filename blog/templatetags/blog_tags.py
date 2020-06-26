from django import template
from django.db.models.aggregates import Count

from blog.models import Post, Category, Tag

register = template.Library()

'''
这里我们首先导入 template 这个模块，然后实例化了一个 template.Library 类，
并将函数 get_recent_posts 装饰为 register.simple_tag。
这样就可以在模板中使用语法 {% get_recent_posts %} 调用这个函数了。
'''
# 最新文章模板标签
@register.simple_tag
def get_recent_post(num=5):
    post_list = Post.objects.all().order_by('-created_time')[:num]
    return post_list

# 归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

# 分类模板标签
@register.simple_tag
def get_category():

    # return Category.objects.annotate(nums_post=Count('post')).filter(num_posts__gt=0)
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    # return Tag.objects.annotate(num_posts=Count('post')).filter(num_post__gt=0)
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)