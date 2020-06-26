from django.contrib import admin

# Register your models here.
from blog.models import Post, Tag, Category

'''
前面已经用dg
，创建了超级用户。

要在后台注册我们自己创建的几个模型，
这样 Django Admin 才能知道它们的存在，注册非常简单，只需要在 blog\admin.py 中加入下面的代码：
'''
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

class PostCatAdmin(admin.ModelAdmin):
    list_display = ['name']
class PostTagAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Post,PostAdmin)
admin.site.register(Category, PostCatAdmin)
admin.site.register(Tag,PostTagAdmin)

