from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
# from utils.random_code import *

from .models import UserInfo
from django.contrib import auth
from .models import *
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
    print("random_code_str",request.session.get("random_code_str"))
    username=request.user

    article_list=Article.objects.all()
    return render(request,"index.html",locals())


def logout(request):
    auth.logout(request)
    print("---",request.session.get("random_code_str"))
    #request.session.flush()
    return HttpResponse("OK")
    # return redirect("/login/")

def get_valid_img(request):
    # from utils.random_code import get_random_code
    #
    # data=get_random_code()
    #
    # print()

    import random
    def get_random_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    # 方式1：
    # f=open("egon.jpg","rb")
    # data=f.read()

    # 方式2;
    from PIL import Image
    # from io import BytesIO
    #
    # image=Image.new(mode="RGB",size=(120,80),color=get_random_color())
    # f=open("code.png","wb")
    # image.save(f,"png")
    #
    # f=open("code.png","rb")
    # data=f.read()

    # 方式3：
    # from io import BytesIO
    # image = Image.new(mode="RGB", size=(120, 80), color=get_random_color())
    # f=BytesIO()
    # image.save(f, "png")
    # data=f.getvalue()


    # 方式4：
    from io import BytesIO
    from PIL import ImageDraw, ImageFont
    f = BytesIO()

    image = Image.new(mode="RGB", size=(120, 80), color=get_random_color())
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("blog/static/fonts/kumo.ttf", size=36)

    temp = []
    for i in range(5):
        random_char = random.choice(
            [str(random.randint(0, 9)), chr(random.randint(65, 90)), chr(random.randint(97, 122))])
        draw.text((i * 24, 26), random_char, get_random_color(), font=font)
        temp.append(random_char)

    width = 120
    height = 80

    # for i in range(80):
    #     draw.point((random.randint(0,width),random.randint(0,height)),fill=get_random_color())
    #
    # for i in range(10):
    #     x1=random.randint(0,width)
    #     x2=random.randint(0,width)
    #     y1=random.randint(0,height)
    #     y2=random.randint(0,height)
    #     draw.line((x1,y1,x2,y2),fill=get_random_color())
    # for i in range(40):
    #     draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())
    image.save(f, "png")
    data = f.getvalue()

    #######保存随机字符串
    # global random_code_str
    # random_code_str = "".join(temp)
    # print("random_code_str",random_code_str)
    #######

    request.session["random_code_str"]="".join(temp)
    #request.session["a"]="pp"
    #request.session["3"]="bbbnnnnnnnn"
    #del request.session["random_code_str"]
    '''
    if cookie.get(sesssion):更新

    1 生成随机字符串
    2 响应set_cookie {"sessionId":"123456abc"}
    3 在django-session表中插入一条记录
       session-key   session-data
       123456abc      {"random_code_str":"abc12"}
    '''


    return HttpResponse(data)