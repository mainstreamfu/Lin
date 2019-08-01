from django.shortcuts import render,redirect,HttpResponse

# Create your views here.


def index(request):
    return render(request,"index.html")


def ajax_handle(request):
    return HttpResponse("Ajax")


def cal(request):
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    ret = int(num1)+int(num2)
    return HttpResponse(str(ret))


def jiaoyan_user(request):
    # response = {"is_reg":True,"error_msg":""}
    response = {"is_reg": True}
    user = request.POST.get("user")
    if user == "yuan":
        pass
        # response["error_msg"] = "该用户已经注册"
    else:
        response["is_reg"] = False
    import json
    return HttpResponse(json.dumps(response))

def btn(request):
    response = {"d":None}
    useralex = request.POST.get("useralex")
    password = request.POST.get("password")
    print(useralex)
    print(password)
    if useralex == "alex" and password == "123456":
        response["d"] = False
    else:
        response["d"] = True
    import json
    return HttpResponse(json.dumps(response))