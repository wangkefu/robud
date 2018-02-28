# -*- coding: utf-8 -*-
import json

from django.db.models import QuerySet, Sum, Count
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from django.views.decorators.csrf import csrf_exempt
from robud_website.models import ApplyAge, Category, RobudProduct, VideoType, Videos, CustomerWorkType, CustomerWork, IpSet, SecondTitle


def index(request):
    return render(request, 'robud_website/index.html')


def aboutus_story(request):
    return render(request, 'robud_website/aboutus.html',{'scroll':False})


def aboutus_team(request):
    return render(request, 'robud_website/aboutus.html',{'scroll':True, 'top':json.dumps(['850'])})


def aboutus_promise(request):
    return render(request, 'robud_website/aboutus.html',{'scroll':True, 'top':json.dumps(['2500'])})


def purchasechannels(request):
    return render(request, 'robud_website/purchasechannels.html')


def news_index(request):
    return render(request, 'robud_website/news_index.html')


# 小小艺术家
def customer_work(request):
    # 获取访问者的ip
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    data = {}
    arr = []
    # 获取作品分类名
    for i in CustomerWorkType.objects.all():
        arr.append({
            'id': i.id,
            'name': i.name
        })
    data['cate'] = arr
    data['month'] = CustomerWork.Month
    arr = []
    for i in CustomerWork.objects.filter(type_id=1):
        arr.append({
            'image': i.image.url,
            'likes': i.like_ips.count(),   # 点赞数
            'author': i.author,
            'age': i.age,
            'id': i.id,
            'visitor_like': True if i.like_ips.filter(ip_number=ip) else False
        })
    data['images'] = arr
    return render(request, 'robud_website/customer_work.html', data)


# 点赞
@csrf_exempt
def like(request):
    like_id = request.POST['id']
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    # 判断此ip是否已存在于数据库中,若不在，把ip加入到数据库，并直接点赞，
    # 若在，判断此图是否被此ip点赞过,若点过，则取消点赞，若没有，则点赞
    if IpSet.objects.filter(ip_number=ip):
        like_work = CustomerWork.objects.get(id=like_id)
        user_ip = IpSet.objects.get(ip_number=ip)
        if user_ip in like_work.like_ips.all():
            like_work.like_ips.remove(user_ip)
            print 'dianguo quxiao'
        else:
            like_work.like_ips.add(user_ip)
            like_work.save()
            print 'meidian zan'
    else:
        new_ip = IpSet()
        new_ip.ip_number = ip
        new_ip.save()
        like_work = CustomerWork.objects.get(id=like_id)
        like_work.like_ips.add(new_ip)
        like_work.save()
        print 'first dian'

    like_work = CustomerWork.objects.get(id=like_id)
    data = {
        'likes': like_work.like_ips.count(),  # 点赞数
        'id': like_work.id,
        'visitor_like': True if like_work.like_ips.filter(ip_number=ip) else False
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


# 小小艺术家 点击分类获取图片
@csrf_exempt
def get_artists_work(request):
    type = request.GET['type']
    month = request.GET.get('month')
    results = CustomerWork.objects.filter(type_id=type)
    if month:
        results = results.filter(month=month)
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    arr = []
    data = {}
    for i in results:
        arr.append({
            'image': i.image.url,
            'likes': i.like_ips.count(),   # 点赞数
            'author': i.author,
            'age': i.age,
            'id': i.id,
            'visitor_like': True if i.like_ips.filter(ip_number=ip) else False
        })
    data['images'] = arr
    return HttpResponse(json.dumps(data), content_type='application/json')


def video_index(request, id=None):
    data = {}
    arr = []
    # 视频分类的获取
    for i in VideoType.objects.all():
        arr.append({
            'id': i.id,
            'name': i.name
        })
    data['video_type'] = arr
    if id:
        videos = Videos.objects.filter(type_id=id)
    else:
        videos = Videos.objects.filter(type_id=1)
    data['videos'] = videos
    return render(request, 'robud_website/video_index.html', data)


def contact(request):
    return render(request, 'robud_website/contact.html')


def products(request, key=None, id=None):
    print key, id
    data = {}
    arr = []
    # label数据获取
    for i in ApplyAge.objects.all():
        arr.append({
            'id':i.id,
            'name':i.name,
            'type':'age'
        })
    data['label_age'] = arr
    arr = []
    for i in Category.objects.all():
        arr.append({
            'id': i.id,
            'name': i.name,
            'type': 'category'
        })
    data['label_category'] = arr
    if key and id:
        if key == 'age':
            products = RobudProduct.objects.filter(age_id=id)
        else:
            products = RobudProduct.objects.filter(category_id=id)
    else:
        products = RobudProduct.objects.filter(category_id=Category.objects.all()[0].id)
    query = products.values_list('title_id').annotate(s_count=Count('id'))

    a = []
    for i in query:
        results = {
            'name': SecondTitle.objects.get(id=i[0]).name,
            'images': products.filter(title_id=i[0])
        }
        a.append(results)
    data['products'] = a
    # print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '), encoding="utf-8", ensure_ascii=False)
    return render(request, 'robud_website/products.html', data)


# 获取labels
def get_labels(request):
    data = {}
    arr = []
    for i in ApplyAge.objects.all():
        arr.append({
            'id':i.id,
            'name':i.name,
            'type':'age'
        })
    data['label_age'] = arr
    arr = []
    for i in Category.objects.all():
        arr.append({
            'id': i.id,
            'name': i.name,
            'type': 'category'
        })
    data['label_category'] = arr
    arr = []
    for i in VideoType.objects.all():
        arr.append({
            'id': i.id,
            'name': i.name
        })
    data['video_type'] = arr
    return HttpResponse(json.dumps(data), content_type='application/json')
