import markdown
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from blog.models import Post, Category, Tag
from comments.forms import CommentForm
from comments.models import Comment


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    context = {
        "title": "我的博客",
        "welcome": "user",
        "post_list": post_list
    }

    return render(request, 'blog/index.html', context=context)


'''
这样我们在模板中展示 {{ post.body }} 的时候，就不再是原始的 Markdown 文本了，
而是渲染过后的 HTML 文本。注意这里我们给 markdown 渲染函数传递了额外的参数 extensions，
它是对 Markdown 语法的拓展，
这里我们使用了三个拓展，
分别是 extra、codehilite、toc。extra 本身包含很多拓展
，而 codehilite 是语法高亮拓展，这为我们后面的实现代码高亮功能提供基础，
而 toc 则允许我们自动生成目录
'''


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body, extensions={
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    })
    form = CommentForm()
    comment_list = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comment_list": comment_list,
        "form": form
    }
    return render(request, 'blog/detail.html', context=context)


#
# def archives(request,year,month):
#     # print(month)
#     post_list = Post.objects.filter(created_time__year=year,created_time__month=month).order_by('-created_time')
#     # print(post_list.ti)
#     for post in post_list:
#         print(post.title)
#     return render(request,'index.html',{'post_list':post_list})


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def categorys(request):
    category = request.GET.get('category')
    print(category)

    # post_list = Post.objects.filter(category_id=category).order_by('-created_time')
    cate = Category.objects.get(pk=category)
    post_list = cate.post_set.all().order_by('-created_time')
    print(post_list)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tags(request):
    tags_id = request.GET.get('tags_id')
    # post_list = Post.objects.filter(tags_id=tags_id).order_by('-create_time')
    tag = Tag.objects.get(pk=tags_id)
    post_list = tag.post_set.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 采用类视图的方法写
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 2


# class CategoryIndex(ListView):
#     model = Post
#     template_name = 'blog/index.html'
#     context_object_name = 'post_list'
#     def get_queryset(self):
#         cate =
def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = "请输入关键词"
        return render(request, 'blog/index.html', {'error_msg': error_msg})
    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'error_msg': error_msg, 'post_list': post_list})

