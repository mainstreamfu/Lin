# from django.contrib import admin
from django.urls import path,re_path
from app01 import views





# urlpatterns = [
#     #个人站点的url配置
#     path('admin/', admin.site.urls),
#     re_path('(?P<username>\w+)/', views.home_site),  # home_site（username="个人站点名"）
#     #path('/',views.home_site) http://127.0.0.1:8000直接跳转
#     # path('\w+/',views.home_site)   至少一个内容在就会跳转
#     re_path('(?P<username>\w+)/(?P<condition>cate|tag|date)/(?P<params>(\w+/?\w+))',views.home_site),
#     re_path('(?P<username>\w+)/articles/(?P<article_id>\d+)\.html',views.article_detail),
#
# ]


urlpatterns = [
    path('digg/',views.digg),
    path('comment/',views.comment),
    re_path('get_comment_tree/(\d+)',views.get_comment_tree),
    re_path('(?P<username>\w+)/backend/',views.backend),

    re_path('(?P<username>\w+)/backend_add_article/',views.backend_add_article),


    # path('admin/', admin.site.urls),
    re_path('(?P<username>\w+)/articles/(?P<article_id>\d+)\.html',views.article_detail),
    re_path('(?P<username>\w+)/$',views.home_site),
    re_path('(?P<username>\w+)/(?P<condition>tag|cate|date)/(?P<params>(\w+/?\w+))', views.home_site),
    #文章详细页点赞url
    # path('digg/',views.digg),

]
