from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from myapp.models import User, Yyzz
from functions.decorators import login_required
import re


# 主页
@login_required
def index(request):
    return render(request, 'myapp/index.html', locals())


# 个人信息
@login_required
def person(request):
    username = request.session.get('username')
    print("username------------", username)
    student = User.objects.get(username=username)
    if request.method == 'GET':
        return render(request, 'myapp/person.html', locals())
    elif request.method == 'POST':
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # 保存数据
        student.gender = gender
        student.phone = phone
        student.email = email
        student.save()
        return redirect('myapp:person')


# 上传电子证照信息
@login_required
def upload(request):
    if request.method == 'GET':
        return render(request, 'myapp/upload.html', locals())
    elif request.method == 'POST':
        img_name = request.POST.get('img_name')
        img_gender = request.POST.get("img_gender")
        img_addr = request.POST.get('img_addr')
        img_sfz = request.POST.get('img_sfz')
        # 1.获取上传的图片
        img_img = request.FILES['pic']
        # 2.创建一个新文件
        save_path = '%s/img/%s' % (settings.MEDIA_ROOT, img_img.name)
        with open(save_path, 'wb') as f:
            # 3.获取上传文件的内容并写到创建的文件中
            for content in img_img.chunks():
                f.write(content)
        # 4.在数据库中保存上传记录
        passport_id = request.session.get('passport_id')
        # 存储到数据库
        user = User.objects.get(id=passport_id)
        user.img_url = 'img/%s' % img_img.name
        user.img_name = img_name
        user.img_gender = img_gender
        user.img_addr = img_addr
        user.img_sfz = img_sfz
        user.save()
        # 5.返回
        return redirect('myapp:see')


# 查看电子证照信息
def see(request):
    passport_id = request.session.get('passport_id')
    user = User.objects.get(id=passport_id)
    return render(request, 'myapp/see.html', locals())


# 上传身份证信息
@login_required
def upload_sfz(request):
    if request.method == 'GET':
        return render(request, 'myapp/upload_sfz.html', locals())
    elif request.method == 'POST':
        # 1.获取上传的图片
        img_img = request.FILES['pic']
        # 2.创建一个新文件
        save_path = '%s/img/%s' % (settings.MEDIA_ROOT, img_img.name)
        with open(save_path, 'wb') as f:
            # 3.获取上传文件的内容并写到创建的文件中
            for content in img_img.chunks():
                f.write(content)

        # 调用百度ai
        # -*-coding:utf-8-*-
        # 作者：   29511
        # 文件名:  识别身份证信息.py
        # 当前系统日期时间：2020/4/30，11:16
        from aip import AipOcr

        """ 你的 APPID AK SK 文字识别工具"""
        APP_ID = '19671350'
        API_KEY = 'FiAZeLqgSstP8t8WqpGIKwEu'
        SECRET_KEY = 'gKXuA0Va7EPL0MG9qsGbqDIqvjb03AnA'
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        image = content
        idCardSide = "front"

        """ 调用身份证识别 """
        # print(client.idcard(image, idCardSide))
        result = client.idcard(image, idCardSide)
        result_ = ''
        if result['image_status'] == 'normal':
            # for key, val in result['words_result'].items():
            #     result_ += key + ':' + val['words'] + '\n'
            # print(result_)

            # 4.在数据库中保存上传记录
            passport_id = request.session.get('passport_id')
            # 存储到数据库
            user = User.objects.get(id=passport_id)
            user.img_url = 'img/%s' % img_img.name
            user.img_name = result['words_result']['姓名']['words']
            user.img_gender = result['words_result']['性别']['words']
            user.img_addr = result['words_result']['住址']['words']
            user.img_sfz = result['words_result']['公民身份号码']['words']
            user.save()
            # 5.返回
            return render(request, 'myapp/see_sfz.html', locals())


# 查看身份证信息
def see_sfz(request):
    passport_id = request.session.get('passport_id')
    user = User.objects.get(id=passport_id)
    print(user.status)
    if user.status == '通过':
        return render(request, 'myapp/see_sfz.html', locals())
    else:
        return HttpResponse("请上传正确的身份证信息, 等待管理员审核! ")
    # return render(request, 'myapp/see_sfz.html', locals())


# 上传营业执照信息
@login_required
def upload_yyzz(request):
    if request.method == 'GET':
        passport_id = request.session.get('passport_id')
        print("passport_id------------", passport_id)
        Yyzz.objects.update_or_create(user_id=passport_id)
        return render(request, 'myapp/upload_yyzz.html', locals())
    elif request.method == 'POST':
        # 1.获取上传的图片
        img_img = request.FILES['pic']
        # 2.创建一个新文件
        save_path = '%s/img/%s' % (settings.MEDIA_ROOT, img_img.name)
        with open(save_path, 'wb') as f:
            # 3.获取上传文件的内容并写到创建的文件中
            for content in img_img.chunks():
                f.write(content)

        # 调用百度ai
        from aip import AipOcr

        """ 你的 APPID AK SK 文字识别工具"""
        APP_ID = '19680327'
        API_KEY = 'L9uO5hq1DHG58Q3QsNDuwgQc'
        SECRET_KEY = 'zkwlIKXwv8GIsPLKjVR3UIn0q8g9ZEPU'
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        image = content

        """ 调用营业执照识别 """
        result = client.businessLicense(image)
        print(result['words_result']['单位名称']['words'])
        print(result['words_result']['法人']['words'])
        print(result['words_result']['地址']['words'])
        print(result['words_result']['成立日期']['words'])
        print(result['words_result']['经营范围']['words'])
        print(result['words_result']['类型']['words'])
        print(result['words_result']['有效期']['words'])
        print(result['words_result']['组成形式']['words'])
        print(result['words_result']['证件编号']['words'])
        print(result['words_result']['社会信用代码']['words'])
        print(result['words_result']['注册资本']['words'])

        # 4.在数据库中保存上传记录
        # 存储到数据库
        passport_id = request.session.get('passport_id')
        user = Yyzz.objects.get(user_id=passport_id)
        user.img_url = 'img/%s' % img_img.name
        user.dwmc = result['words_result']['单位名称']['words']
        user.fr = result['words_result']['法人']['words']
        user.dz = result['words_result']['地址']['words']
        user.clrq = result['words_result']['成立日期']['words']
        user.jyfw = result['words_result']['经营范围']['words']
        user.lx = result['words_result']['类型']['words']
        user.yxq = result['words_result']['有效期']['words']
        user.zcxs = result['words_result']['组成形式']['words']
        user.zjbh = result['words_result']['证件编号']['words']
        user.shxydm = result['words_result']['社会信用代码']['words']
        user.zczb = result['words_result']['注册资本']['words']
        user.save()
        # 5.返回
        return render(request, 'myapp/see_yyzz.html', locals())


# 查看营业执照信息
def see_yyzz(request):
    passport_id = request.session.get('passport_id')
    user = Yyzz.objects.get(user_id=passport_id)
    print(user.status)
    if user.status == '通过':
        return render(request, 'myapp/see_yyzz.html', locals())
    else:
        return HttpResponse("请上传正确的营业执照信息, 等待管理员审核! ")


# 注册
def register(request):
    return render(request, 'myapp/register.html')


# 提交注册页的表单
def register_handle(request):
    # 获取数据
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    # 校正数据
    # 数据有空
    if not all([username, password, email]):
        return render(request, 'myapp/register.html', {'errmsg': '参数不能为空'})
    # 判断邮箱是否合法
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'myapp/register.html', {'errmsg': '邮箱不正确'})
    # 业务处理，向系统中添加账户
    try:
        User.objects.add_one_passport(
            username=username,
            password=password,
            email=email
        )
    # 打印异常
    except Exception as e:
        print("e:", e)
        return render(request, 'myapp/register.html', {'errmsg': '用户名已存在'})
    # 注册完返回登录页
    return render(request, 'myapp/login.html')


# 显示登录页面
def login(request):
    # 如果能从cookies中获取到username则表示点击过“保存用户名”
    if request.COOKIES.get('username'):
        username = request.COOKIES.get('username')
        checked = 'checked'
    else:
        username = ''
        checked = ''
    context = {
        'username': username,
        'checked': checked,
    }
    return render(request, 'myapp/login.html', context)


# 验证登录
def login_check(request):
    # 1.获取数据
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')

    # 2.验证数据
    if not all([username, password, remember]):
        # 有数据为空
        return JsonResponse({"res": 2})

    # 3.进行处理：根据用户名和密码查找账户信息
    passport = User.objects.get_one_passport(username=username, password=password)
    if passport:
        turn_to = reverse('myapp:index')
        jres = JsonResponse({"res": 1, "turn_to": turn_to})

        # 是否记住用户名
        if remember == 'true':
            jres.set_cookie('username', username, max_age=7 * 24 * 3600)
        else:
            jres.delete_cookie('username')

        # 记住用户的登录状态
        request.session['islogin'] = True
        request.session['username'] = username
        request.session['passport_id'] = passport.id
        return jres
    else:
        # 用户名密码错误
        return JsonResponse({"res": 0})


# 登出
def logout(request):
    # 清除session信息
    request.session.flush()
    return redirect(reverse('myapp:login'))
