#coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
import logging
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    # return HttpResponse("<html><h1>hello django!</h1></html>")
    return render(request, "index.html")


def login_action(request):
    if request.method == "GET":
        pass
    if request.method == "POST":
        page_username = request.POST.get("username")  # admin
        page_password = request.POST.get("password")  # admin123456
        if page_username == "" or page_password == "":
            error = "username or password null."
            return render(request, "index.html", {'index_error': error})

        user = auth.authenticate(username=page_username, password=page_password)
        if user is not None:
            auth.login(request, user)   # 登录
            response = HttpResponseRedirect('/event_manage/')
            request.session['user'] = page_username   # 将session 信息记录到浏览器
            return response
        else:
            error = 'username or password error!'
            return render(request, 'index.html', {'index_error': error})
    else:
        return render(request, 'index.html')


@login_required
def event_manage(request):
    events = Event.objects.all()
    # username = request.COOKIES.get('user', '') # 读取浏览器 cookie
    username = request.session.get('user', '')  # 读取浏览器 session
    return render(request, "event_manage.html", {"user": username,
                                                 "events_list": events})


@login_required
def search_name(request):
    search_name  = request.GET.get("name", '')
    if search_name == '':
        events = Event.objects.all()
    else:
        events = Event.objects.filter(name__contains=search_name)
    username = request.session.get('user', '') 
    return render(request, "event_manage.html", {"user": username,
                                                 "events_list":events})


@login_required
def guest_manage(request):
    username = request.session.get('user', '')  # 读取浏览器 session

    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)  #按照2行数所分一页
    page = request.GET.get('page')   # page 得到的是页数 1，2，3
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username,
                                                 "guests_list": contacts})



@login_required
def search_phone(request):
    phone_number  = request.GET.get("phone_number", '')
    if phone_number == '':
        events = Guest.objects.all()
    else:
        events = Guest.objects.filter(phone=phone_number)
    username = request.session.get('user', '')
    return render(request, "guest_manage.html", {"user": username,
                                                 "guests_list":events})



@login_required
def sign_index(request,event_id):
    username = request.session.get('user', '')
    print(event_id)
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html', {'event': event,
                                               "user": username})



@login_required
def sign_index_action(request,event_id):

    event = get_object_or_404(Event, id=event_id)
    phone = request.POST.get('phone','')

    result = Guest.objects.filter(phone = phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event,
                                                'hint': 'phone error.'})
    
    result = Guest.objects.filter(phone=phone,event_id=event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event,
                                               'hint': 'event id or phone error.'})
    
    result = Guest.objects.get(phone=phone,event_id=event_id)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': "user has sign in."})
    else:
        Guest.objects.filter(phone=phone,event_id=event_id).update(sign = '1')
    return render(request, 'sign_index.html', {'event': event,
                                               'hint':'sign in success!',
                                               'guest': result})



def logout(request):
    auth.logout(request) #退出登录
    response = HttpResponseRedirect('/index/')
    return response


'''
浏览器：                   服务器
user input "admin"
cookie = "admin"
page  "admin"

user input 'admin'
cookie = sessionid        =>"admin"
page    <=                 "admin"



python 编程语言django  ---> mysql驱动  --->    mysql 数据库
1、安装mysql数据库，wampserver（MySQL）
2, python安装pymysql驱动
3，django settings.py 设置mysql链接，guest/__init__.py


发布会管理系统：发布会管理，嘉宾管理，签到页面

MVC <--> java/php/python  Web框架
models  数据层
views  视图层
control  控制层


Django MTV
---------
models  数据层
views  视图层
templates 模板层

'''