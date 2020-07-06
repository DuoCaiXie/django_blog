# django_blog
It's a simple personal blog based on Django
# 安装
```
pip install -r requirements.txt
#  依赖安装不了请单独每个进行安装
```
# 创建数据库
```
CREATE DATABASE `数据库名字` CHARACTER SET 'utf8';
 # 注意要utf8格式的数据库 不然博客输入中文的时候会出问题 
```
# 迁移
```
python manage.py makemigrations
python manage.py migrate
```
# 启动
```
# 创建超级管理员
python manage.py createsuperuser
# 启动服务
python manage.py runserver

# 如在本机运行则http://localhost:8000/admin/ 进行文章的增删改查，支持markdown语法
```
