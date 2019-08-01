from django import template

from django.utils.safestring import mark_safe

from app01.models import *
from django.db.models import Count

register = template.Library()    #register名字是固定的，不能改变





@register.inclusion_tag("app01/archive.html")
def get_archive_style(username):
    user = UserInfo.objects.filter(username=username).first()
    blog = user.blog
    cate_list = Category.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title", "c")
    tag_list = Tag.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title", "c")

    date_list = Article.objects.filter(user=user).extra(select={"create_time_ym": "date_format(create_time,'%%Y/%%m')"})\
        .values("create_time_ym").annotate(c=Count("nid")).values_list("create_time_ym", "c")

    return {"cate_list": cate_list, "tag_list": tag_list, "date_list": date_list, "username": username}


# @register.inclusion_tag("app01/content.html")
# def get_archive_content(username,**kwargs):
#     print(kwargs)
#     # 判断用户是否存在
#     user = UserInfo.objects.filter(username=username).first()
#
#     if not user:
#         return render(request, "app01/not_found.html")
#     # 当前站点
#     blog = user.blog
#
#     # 筛选当前站点的所有文章
#     # Article.objects.filter(user_id=user.nid)
#     # article_list = Article.objects.filter(user=user)  # 直接赋值一个对象
#     if not kwargs:
#         article_list = Article.objects.filter(user=user)  # 直接赋值一个对象
#     else:  # 归档跳转标签请求,对article_list过滤
#         condition = kwargs.get("condition")
#         params = kwargs.get("params")
#         if condition == "cate":
#             article_list = Article.objects.filter(user=user).filter(homeCategory__title=params)
#         elif condition == "tag":
#             article_list = Article.objects.filter(user=user).filter(tags__title=params)
#         else:
#             year = params[0:4]
#             month = params[5:7]
#             print(year, month)
#             article_list = Article.objects.filter(user=user).filter(create_time__year=year, create_time__month=month)
#
#         # 查询当前站点的所有分类
#     # category_list = Category.objects.filter(blog_id=blog.nid)
#     # category_list = Category.objects.filter(blog_id=blog.pk)
#     # pk就是primary_key，不管是id还是nid，每个表只有一个主键值，因此可改为xxx.pk
#     # category_list = Category.objects.filter(blog=blog)#直接赋值一个对象
#
#     # 查询当前站点的每一个分类名称及对应的文章数
#
#     cate_list = Category.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title", "c")
#     # print(ret)
#     # 查询当前站点每一个标签名称以及对应的文章数
#     tag_list = Tag.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title", "c")
#     # print(tag_list)
#
#     # 日期归档
#     # date_list = []
#     # for obj in article_list:
#     #     print("create_time:",type(obj.create_time))
#     #     temp = []
#     #     s = "%s-%s"%(obj.create_time.year,obj.create_time.month)
#     #     count = Article.objects.filter(user=user,create_time__year=obj.create_time.year,create_time__month=obj.create_time.month).count()
#     #     print(count,type(count))
#     #     temp.append(s)
#     #     temp.append(count)
#     #     if temp not in date_list:
#     #
#     #         date_list.append(temp)
#     #
#     # print(date_list)
#
#     # date_list = []
#     # for obj in article_list:
#     #     temp = []
#     #     cts = obj.create_time.strftime('%Y-%m-%d %H:%M:%S')
#     #     s = cts[0:7]
#     #     count = Article.objects.filter(user=user,create_time__contains=s).count()
#     #     temp.append(s)
#     #     temp.append(count)
#     #     if temp not in date_list:
#     #
#     #         date_list.append(temp)
#     #
#     # print(date_list)
#
#     date_list = Article.objects.filter(user=user) \
#         .extra(select={"standard_time": "date_format(create_time,'%%Y年%%m月')"}) \
#         .values("standard_time") \
#         .annotate(c=Count("nid")) \
#         .values_list("standard_time", "c")
#     return {"article_list":article_list,"username":username}
# @register.filter
# def filter_multi(v1,v2):
#     return v1*v2
#
# @register.simple_tag
# def simple_tag_multi(v1,v2):
#     return v1*v2