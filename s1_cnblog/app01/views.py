from django.shortcuts import render,HttpResponse,redirect
from .models import UserInfo
from django.contrib import auth
from .models import *
from django.db.models import Count
from app01.forms import RegisterForm
# Create your views here.
# from utils.random_code import *


#构建查询分类数据
# def get_achive(username):
#     user = UserInfo.objects.filter(username=username).first()
#     #当前站点
#     blog = user.blog
#
#     # 筛选当前站点的所有文章
#     # Article.objects.filter(user_id=user.nid)
#     # article_list = Article.objects.filter(user=user)  # 直接赋值一个对象
#      #查询当前站点的所有分类
#     # category_list = Category.objects.filter(blog_id=blog.nid)
#     # category_list = Category.objects.filter(blog_id=blog.pk)
#     # pk就是primary_key，不管是id还是nid，每个表只有一个主键值，因此可改为xxx.pk
#     #category_list = Category.objects.filter(blog=blog)#直接赋值一个对象
#
#     #查询当前站点的每一个分类名称及对应的文章数
#
#     cate_list = Category.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title","c")
#     # print(ret)
#     #查询当前站点每一个标签名称以及对应的文章数
#     tag_list = Tag.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title","c")
#     # print(tag_list)
#
#     #日期归档
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
#     date_list = Article.objects.filter(user=user)\
#         .extra(select={"standard_time":"date_format(create_time,'%%Y年%%m月')"})\
#         .values("standard_time")\
#         .annotate(c=Count("nid"))\
#         .values_list("standard_time","c")
#
#
#     # print(date_list)
#     return {"cate_list":cate_list,"tag_list":tag_list,"date_list":date_list}

def log_in(request):
    if request.is_ajax():
        print(request.POST)
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        valid_code=request.POST.get("valid_code")
        code_str=request.session.get("random_code_str")
        '''
        1 sessionID=request.COOKIE.get("sessionID) # 123456abc
        2 django-session表
           session-key   session-data
           123456abc      {"random_code_str":"abc12"}
           360000abc      {"random_code_str":"abc45"}
           obj=django-session.objects.filter(session-key=123456abc)
        3  obj.session-data.get("random_code_str")  # abc12
        '''
        print("random_code_str",code_str)

        login_response={"user":None,"error_msg":""}

        if valid_code.upper()==code_str.upper():
            user=auth.authenticate(username=user,password=pwd)
            if user:
                login_response["user"]=user.username
                auth.login(request,user) # 1  {"user_id":1}  2 request.user=user
                print("===",request.session.get("random_code_str"))
            else:
                login_response["error_msg"] ="username or password error!"
        else:
            login_response["error_msg"]="valid code error!"

        import json
        return HttpResponse(json.dumps(login_response))

    return render(request,"login.html")


def index(request):
    # print("random_code_str",request.session.get("random_code_str"))
    # username = request.user
    article_list = Article.objects.all()
    return render(request,"index.html",locals())


def log_out(request):
    auth.logout(request)
    return redirect("/login/")

def get_valid_img(request):
    # from utils.random_code import get_random_code
    #
    # data=get_random_code()
    #
    # print()

    # import random
    # def get_random_color():
    #     return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    #
    #
    # # 方式1：
    # # f=open("egon.jpg","rb")
    # # data=f.read()
    #
    # # 方式2;
    # from PIL import Image
    # # from io import BytesIO
    # #
    # # image=Image.new(mode="RGB",size=(120,80),color=get_random_color())
    # # f=open("code.png","wb")
    # # image.save(f,"png")
    # #
    # # f=open("code.png","rb")
    # # data=f.read()
    #
    # # 方式3：
    # # from io import BytesIO
    # # image = Image.new(mode="RGB", size=(120, 80), color=get_random_color())
    # # f=BytesIO()
    # # image.save(f, "png")
    # # data=f.getvalue()
    #
    #
    # # 方式4：
    # from io import BytesIO
    # from PIL import ImageDraw, ImageFont
    # f = BytesIO()
    #
    # image = Image.new(mode="RGB", size=(120, 80), color=get_random_color())
    # draw = ImageDraw.Draw(image)
    # font = ImageFont.truetype("app01/static/font/kumo.ttf", size=36)
    #
    # temp = []
    # for i in range(5):
    #     random_char = random.choice(
    #         [str(random.randint(0, 9)), chr(random.randint(65, 90)), chr(random.randint(97, 122))])
    #     draw.text((i * 24, 26), random_char, get_random_color(), font=font)
    #     temp.append(random_char)
    #
    # width = 120
    # height = 80
    #
    # # for i in range(80):
    # #     draw.point((random.randint(0,width),random.randint(0,height)),fill=get_random_color())
    # #
    # # for i in range(10):
    # #     x1=random.randint(0,width)
    # #     x2=random.randint(0,width)
    # #     y1=random.randint(0,height)
    # #     y2=random.randint(0,height)
    # #     draw.line((x1,y1,x2,y2),fill=get_random_color())
    # # for i in range(40):
    # #     draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
    # #     x = random.randint(0, width)
    # #     y = random.randint(0, height)
    # #     draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())
    # image.save(f, "png")
    # data = f.getvalue()
    #
    # #######保存随机字符串
    # # global random_code_str
    # # random_code_str = "".join(temp)
    # # print("random_code_str",random_code_str)
    # #######
    #
    # request.session["random_code_str"]="".join(temp)
    # #request.session["a"]="pp"
    # #request.session["3"]="bbbnnnnnnnn"
    # #del request.session["random_code_str"]
    '''
    if cookie.get(sesssion):更新

    1 生成随机字符串
    2 响应set_cookie {"sessionId":"123456abc"}
    3 在django-session表中插入一条记录
       session-key   session-data
       123456abc      {"random_code_str":"abc12"}
    '''
    '''
    :param:request:
    :get_valid_img:生成验证码，返回图片数据
    :return:
    '''
    from app01.utils.valid_code import get_valid_img
    info = get_valid_img(request)
    request.session["random_code_str"] = "".join(info[1])
    return HttpResponse(info[0])

def register(request):
    if request.is_ajax():
        register_form = RegisterForm(request.POST)
        reg_response = {"user":None,"error_msg":None}
        if register_form.is_valid():
            user = register_form.cleaned_data.get("user")
            pwd = register_form.cleaned_data.get("pwd")
            email = register_form.cleaned_data.get("email")
            avatar_obj = request.FILES.get("avatar")            #图片对象
            user_obj = UserInfo.objects.create_user(username=user,password=pwd,email=email,avatar=avatar_obj)
            reg_response["user"] = user_obj.username
        else:
             reg_response["error_msg"] = register_form.errors
        import json
        return HttpResponse(json.dumps(reg_response))

        # user = request.POST.get("user")
        # user = request.POST.get("pwd")
        # user = request.POST.get("repeat_pwd")
        # user = request.POST.get("email")
        # user = request.POST.get("avatar")
    register_form = RegisterForm()
    return render(request,"register.html",locals())

##############################################个人站点：home_site#################

# def home_site(request,username,**kwargs):
#     print(kwargs)
#     #判断用户是否存在
#     user = UserInfo.objects.filter(username=username).first()
#
#     if not user:
#         return render(request,"app01/not_found.html")
#     #当前站点
#     blog = user.blog
#
#     # 筛选当前站点的所有文章
#     # Article.objects.filter(user_id=user.nid)
#     # article_list = Article.objects.filter(user=user)  # 直接赋值一个对象
#     if not kwargs:
#         article_list = Article.objects.filter(user=user)#直接赋值一个对象
#     else:#归档跳转标签请求,对article_list过滤
#         condition=kwargs.get("condition")
#         params = kwargs.get("params")
#         if condition=="cate":
#             article_list = Article.objects.filter(user=user).filter(homeCategory__title=params)
#         elif condition=="tag":
#             article_list = Article.objects.filter(user=user).filter(tags__title=params)
#         else:
#             year=params[0:4]
#             month = params[5:7]
#             print(year,month)
#             article_list = Article.objects.filter(user=user).filter(create_time__year=year,create_time__month=month)
#
#
#
#
#         #查询当前站点的所有分类
#     # category_list = Category.objects.filter(blog_id=blog.nid)
#     # category_list = Category.objects.filter(blog_id=blog.pk)
#     # pk就是primary_key，不管是id还是nid，每个表只有一个主键值，因此可改为xxx.pk
#     #category_list = Category.objects.filter(blog=blog)#直接赋值一个对象
#
#     #查询当前站点的每一个分类名称及对应的文章数
#
#     cate_list = Category.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title","c")
#     # print(ret)
#     #查询当前站点每一个标签名称以及对应的文章数
#     tag_list = Tag.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title","c")
#     # print(tag_list)
#
#     #日期归档
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
#     date_list = Article.objects.filter(user=user)\
#         .extra(select={"standard_time":"date_format(create_time,'%%Y年%%m月')"})\
#         .values("standard_time")\
#         .annotate(c=Count("nid"))\
#         .values_list("standard_time","c")
#
#
#     # print(date_list)
#
#     return render(request,"app01/home_site.html",locals())

########################################个人站点：home_site   简化版

    # print(kwargs)
    #判断用户是否存在
    # user = UserInfo.objects.filter(username=username).first()
    #
    # if not user:
    #     return render(request,"app01/not_found.html")
    # #当前站点
    # blog = user.blog

    # 筛选当前站点的所有文章
    # Article.objects.filter(user_id=user.nid)
    # article_list = Article.objects.filter(user=user)  # 直接赋值一个对象
    # user = UserInfo.objects.filter(username=username).first()
    # if not kwargs:
    #     article_list = Article.objects.filter(user=user)#直接赋值一个对象
    # else:#归档跳转标签请求,对article_list过滤
    #     condition=kwargs.get("condition")
    #     params = kwargs.get("params")
    #     if condition=="cate":
    #         article_list = Article.objects.filter(user=user).filter(homeCategory__title=params)
    #     elif condition=="tag":
    #         article_list = Article.objects.filter(user=user).filter(tags__title=params)
    #     else:
    #         year=params[0:4]
    #         month = params[5:7]
    #         print(year,month)
    #         article_list = Article.objects.filter(user=user).filter(create_time__year=year,create_time__month=month)
    #



        #查询当前站点的所有分类
    # category_list = Category.objects.filter(blog_id=blog.nid)
    # category_list = Category.objects.filter(blog_id=blog.pk)
    # pk就是primary_key，不管是id还是nid，每个表只有一个主键值，因此可改为xxx.pk
    #category_list = Category.objects.filter(blog=blog)#直接赋值一个对象

    #查询当前站点的每一个分类名称及对应的文章数
    #
    # cate_list = Category.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title","c")
    # # print(ret)
    # #查询当前站点每一个标签名称以及对应的文章数
    # tag_list = Tag.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title","c")
    # # print(tag_list)
    #
    # #日期归档
    # # date_list = []
    # # for obj in article_list:
    # #     print("create_time:",type(obj.create_time))
    # #     temp = []
    # #     s = "%s-%s"%(obj.create_time.year,obj.create_time.month)
    # #     count = Article.objects.filter(user=user,create_time__year=obj.create_time.year,create_time__month=obj.create_time.month).count()
    # #     print(count,type(count))
    # #     temp.append(s)
    # #     temp.append(count)
    # #     if temp not in date_list:
    # #
    # #         date_list.append(temp)
    # #
    # # print(date_list)
    #
    #
    # # date_list = []
    # # for obj in article_list:
    # #     temp = []
    # #     cts = obj.create_time.strftime('%Y-%m-%d %H:%M:%S')
    # #     s = cts[0:7]
    # #     count = Article.objects.filter(user=user,create_time__contains=s).count()
    # #     temp.append(s)
    # #     temp.append(count)
    # #     if temp not in date_list:
    # #
    # #         date_list.append(temp)
    # #
    # # print(date_list)
    #
    # date_list = Article.objects.filter(user=user)\
    #     .extra(select={"standard_time":"date_format(create_time,'%%Y年%%m月')"})\
    #     .values("standard_time")\
    #     .annotate(c=Count("nid"))\
    #     .values_list("standard_time","c")
    #
    #
    # # print(date_list)
def home_site(request, username, **kwargs):
        # print(kwargs)
        #判断用户是否存在
        user = UserInfo.objects.filter(username=username).first()

        if not user:
            return render(request,"app01/not_found.html")
        #当前站点
        blog = user.blog

        # 筛选当前站点的所有文章
        # Article.objects.filter(user_id=user.nid)
        # article_list = Article.objects.filter(user=user)  # 直接赋值一个对象
        if not kwargs:
            article_list = Article.objects.filter(user=user)#直接赋值一个对象
        else:#归档跳转标签请求,对article_list过滤
            condition=kwargs.get("condition")
            params = kwargs.get("params")
            if condition=="cate":
                article_list = Article.objects.filter(user=user).filter(homeCategory__title=params)
            elif condition=="tag":
                article_list = Article.objects.filter(user=user).filter(tags__title=params)
            else:
                year=params[0:4]
                month = params[5:7]
                print(year,month)
                article_list = Article.objects.filter(user=user).filter(create_time__year=year,create_time__month=month)




            #查询当前站点的所有分类
        # category_list = Category.objects.filter(blog_id=blog.nid)
        # category_list = Category.objects.filter(blog_id=blog.pk)
        # pk就是primary_key，不管是id还是nid，每个表只有一个主键值，因此可改为xxx.pk
        #category_list = Category.objects.filter(blog=blog)#直接赋值一个对象

        #查询当前站点的每一个分类名称及对应的文章数

        cate_list = Category.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title","c")
        # print(ret)
        #查询当前站点每一个标签名称以及对应的文章数
        tag_list = Tag.objects.filter(blog=blog).annotate(c=Count("article")).values_list("title","c")
        # print(tag_list)

        #日期归档
        # date_list = []
        # for obj in article_list:
        #     print("create_time:",type(obj.create_time))
        #     temp = []
        #     s = "%s-%s"%(obj.create_time.year,obj.create_time.month)
        #     count = Article.objects.filter(user=user,create_time__year=obj.create_time.year,create_time__month=obj.create_time.month).count()
        #     print(count,type(count))
        #     temp.append(s)
        #     temp.append(count)
        #     if temp not in date_list:
        #
        #         date_list.append(temp)
        #
        # print(date_list)


        # date_list = []
        # for obj in article_list:
        #     temp = []
        #     cts = obj.create_time.strftime('%Y-%m-%d %H:%M:%S')
        #     s = cts[0:7]
        #     count = Article.objects.filter(user=user,create_time__contains=s).count()
        #     temp.append(s)
        #     temp.append(count)
        #     if temp not in date_list:
        #
        #         date_list.append(temp)
        #
        # print(date_list)

        date_list = Article.objects.filter(user=user)\
            .extra(select={"standard_time":"date_format(create_time,'%%Y年%%m月')"})\
            .values("standard_time")\
            .annotate(c=Count("nid"))\
            .values_list("standard_time","c")

        return render(request,"app01/home_site.html",locals())


# def article_detail(request,username,article_id):
#     # c =  get_achive(username)
#
#     return render(request,"app01/article_detail.html",c)

def article_detail(request,username,article_id):

    article_obj = Article.objects.filter(pk=article_id).first()
    comment_list = Comment.objects.filter(article_id=article_id)
    return render(request,"app01/article_detail.html",locals())

######################文章详细页#######################################
from django.db.models import F
# from django.db import transaction
# from django.http import JsonResponse
#
# def digg(request):
#     article_id = request.POST.get("article_id")
#     user_id = request.user.pk
#     response = {"state":True}
#     try:
#         with transaction.atomic():#事务处理
#             obj = ArticleUpDown.objects.create(user_id=user_id,article_id=article_id)
#             Article.objects.filter(pk=article_id).update(up_count=F("up_count")+1)
#     except Exception as e:
#         response["state"]=False
#
#     return JsonResponse(response)#等同于json.dumps


from django.db.models import F
from django.db import transaction

from django.http import JsonResponse
import json

def digg(request):
    print(request.POST)
    article_id=request.POST.get("article_id")
    is_up = json.loads(request.POST.get("is_up"))
    user_id=request.user.pk
    response={"state":True,"first_updown":None}
    try:
        with transaction.atomic(): #  事务处理
            obj=ArticleUpDown.objects.create(user_id=user_id,article_id=article_id,is_up=is_up)
            if is_up:
                Article.objects.filter(nid=article_id).update(up_count=F("up_count")+1)
            else:
                Article.objects.filter(nid=article_id).update(down_count=F("down_count")+1)
    except Exception as e:
        first_updown = ArticleUpDown.objects.filter(user_id=user_id, article_id=article_id).values("is_up").first().get("is_up")
        response["state"]=False
        response["first_updown"] = first_updown #标志第一次做了点赞还是踩灭
    return JsonResponse(response)


def comment(request):
    print(request.POST)
    content = request.POST.get("content")
    article_id = request.POST.get("article_id")
    user_id=request.user.pk
    pid = request.POST.get("pid")
    comment_response={}
    with transaction.atomic(): #  事务处理
        if pid:#子评论
            comment = Comment.objects.create(content=content,article_id=article_id,user_id=user_id,parent_comment_id=pid)
        else:#跟评论
            comment = Comment.objects.create(content=content, article_id=article_id, user_id=user_id)
        Article.objects.filter(pk=article_id).update(comment_count=F("comment_count")+1)
    comment_response["create_time"]=comment.create_time.strftime("%Y-%m-%d %H:%M")
    comment_response["content"]=comment.content
    return HttpResponse(json.dumps(comment_response))

def backend(request,username):

    article_list = Article.objects.filter(user__username=username)
    return render(request,"app01/backend_index.html",{"username":username,"article_list":article_list})


def backend_add_article(request,username):
    return render(request,"app01/backend_add_article.html",locals())


def upload_file(request):
    print(request.FILES)
    #保存上传到指定路径
    obj = request.FILES.get("upload_img")
    from s1_cnblog import settings
    import os
    path = os.path.join(settings.MEDIA_ROOT,"article_img",obj.name)
    with open(path,"wb") as f_write:
        for chunk in obj.chunks():
    # chunks代表不按照行读，chunks可以指定一次读多少默认读64位
            f_write.write(chunk)
    #给文本编辑器返回json字符串
    upload_response={
        "error":0,
        "url":"/media/article_img/%s"%obj.name
    }
    #"error":0没有错误成功
    return HttpResponse(json.dumps(upload_response))

def get_comment_tree(request,article_id):
    """
    传两个参数
    需要拿到一个article_id,筛选当前所有文章的comment
    :param request:
    :param a:
    :return:
    """
    #下面这段内容无法json序列化，需要先转成列表
    comment_list = list(Comment.objects.filter(article_id=article_id).values("nid","content","parent_comment_id","user__username"))
    from django.http import JsonResponse
    #设置safe=False避免一些问题
    return JsonResponse(comment_list,safe=False)