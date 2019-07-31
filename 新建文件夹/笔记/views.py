from django.shortcuts import render

# Create your views here.

data = []
for i in range(1, 302):
    tmp = {"id": i, "name": "alex-{}".format(i)}
    data.append(tmp)
# data


# def user_list(request):
#     try:
#         page_num = int(request.GET.get("page"))  # 字符串类型，所以要转成int
#     except Exception as e:
#         page_num = 1
#     # 没有传页码， 默认展示第一页
#     # if not page_num:
#     #     page_num = 1
#     # 每一页显示10条记录
#     per_page_num = 10
#     # user_list = data[0:10]  1  (1-1) *10   1*10
#     # user_list = data[10:20] 2  (2-1) *10   2*10
#     # user_list = data[20:30] 3   (n-1)*10   n*10
#
#     # 总数据个数
#     total_count = len(data)
#     # 总共有多少页
#     total_page_num, more = divmod(total_count, per_page_num)
#     if more:
#         total_page_num += 1
#     # 如果你输入的页码数超过我的总页数，我默认返回最后一页
#     if page_num > total_page_num:
#         page_num = total_page_num
#
#     # 最多显示多少页码
#     max_show = 11
#     half_show = int((max_show-1)/2)
#     # 页面上页码从哪儿开始
#     page_start = page_num - half_show
#     # 页面上页码最多展示到哪一个
#     page_end = page_num + half_show
#
#     # 如果当前页小于等于half_show, 默认从第一页展示到max_show
#     if page_num <= half_show:
#         page_start = 1
#         page_end = max_show
#     # 如果当前页大于等于总页数-half_show
#     if page_num >= total_page_num - half_show:
#         page_end = total_page_num
#         page_start = total_page_num - max_show
#
#     # 生成前页码的HTML
#     page_html_list = []
#     # 放置一个首页按钮
#     page_first_tmp =  '<li><a href="/user_list/?page=1">首页</a></li>'
#     page_html_list.append(page_first_tmp)
#
#     # 加上一页按钮
#     if page_num - 1 <= 0:  # 表示没有上一页
#         page_prev_tmp = '<li class="disabled" ><a href="#">上一页</a></li>'
#     else:
#         page_prev_tmp = '<li><a href="/user_list/?page={}">上一页</a></li>'.format(page_num - 1)
#     page_html_list.append(page_prev_tmp)
#
#     for i in range(page_start, page_end+1):
#         # 如果是当前页，就加一个active的样式
#         if i == page_num:
#             tmp = '<li class="active"><a href="/user_list/?page={0}">{0}</a></li>'.format(i)
#         else:
#             tmp = '<li><a href="/user_list/?page={0}">{0}</a></li>'.format(i)
#         page_html_list.append(tmp)
#     # 加下一页按钮
#     if page_num+1 > total_page_num:
#         page_next_tmp = '<li class="disabled"><a href="#">下一页</a></li>'
#     else:
#         page_next_tmp = '<li><a href="/user_list/?page={}">下一页</a></li>'.format(page_num+1)
#     page_html_list.append(page_next_tmp)
#     # 添加一个尾页
#     page_last_tmp = '<li><a href="/user_list/?page={}">尾页</a></li>'.format(total_page_num)
#     page_html_list.append(page_last_tmp)
#
#     page_html = "".join(page_html_list)
#
#     # 去数据库取数据
#     start = (page_num - 1) * per_page_num
#     end = page_num * per_page_num
#
#     user_list = data[start:end]
#
#     return render(request, "user_list.html", {"user_list": user_list, "page_html": page_html})


def user_list(request):
    page_num = request.GET.get("page")
    path = request.path_info
    # request.get_full_path()  # 带参数的URL
    from tools.mypage import MyPage
    page = MyPage(page_num, len(data), path)
    page_html = page.page_html()
    return render(request, "user_list.html", {"user_list": data[page.start:page.end], "page_html": page_html})


