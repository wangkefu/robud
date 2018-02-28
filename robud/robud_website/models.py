# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ApplyAge(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)

    class Meta:
        verbose_name = '产品适用年龄'
        verbose_name_plural = "产品适用年龄"

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)

    class Meta:
        verbose_name = '产品品种'
        verbose_name_plural = "产品品种"

    def __unicode__(self):
        return self.name


class SecondTitle(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = '二级标题'
        verbose_name_plural = "二级标题"

    def __unicode__(self):
        return self.name


class RobudProduct(models.Model):
    category_id = models.ForeignKey(Category, null=True, verbose_name='所属品种')
    age_id = models.ForeignKey(ApplyAge, null=True, verbose_name='适用年龄')
    title_id = models.ForeignKey(SecondTitle, null=True, verbose_name='二级标题')
    name = models.CharField(max_length=120, verbose_name='产品名')
    size = models.CharField(max_length=120, null=True, blank=True, verbose_name='组装尺寸')
    pack_size = models.CharField(max_length=120, null=True, blank=True, verbose_name='包装尺寸')
    wood_qty = models.IntegerField(null=True, blank=True, verbose_name='木片数量')
    image = models.ImageField(blank=True, upload_to='products_images/%Y%m%d', verbose_name='产品图')

    class Meta:
        verbose_name = '所有产品'
        verbose_name_plural = "所有产品"

    def __unicode__(self):
        return self.name


class VideoType(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)

    class Meta:
        verbose_name = '视频所属类型'
        verbose_name_plural = "视频所属的类型、分类"

    def __unicode__(self):
        return self.name


class Videos(models.Model):
    name = models.CharField(max_length=120, verbose_name='视频名字')
    type_id = models.ForeignKey(VideoType, null=True, verbose_name='所属品种')
    video = models.FileField(blank=True, upload_to='videos/%Y%m%d', verbose_name='视频')
    image = models.ImageField(blank=True, upload_to='video_cover/%Y%m%d', verbose_name='视频表层图')

    class Meta:
        verbose_name = '所有视频'
        verbose_name_plural = "所有视频"

    def __unicode__(self):
        return self.name


class IpSet(models.Model):
    ip_number = models.GenericIPAddressField()

    def __unicode__(self):
        return self.ip_number


class CustomerWorkType(models.Model):
    name = models.CharField(max_length=120, verbose_name='小艺术家作品类型')

    class Meta:
        verbose_name = '小艺术家作品类型'
        verbose_name_plural = "小艺术家作品类型"

    def __unicode__(self):
        return self.name


class CustomerWork(models.Model):
    Month = (
        (1, u'1月'),
        (2, u'2月'),
        (3, u'3月'),
        (4, u'4月'),
        (5, u'5月'),
        (6, u'6月'),
        (7, u'7月'),
        (8, u'8月'),
        (9, u'9月'),
        (10, u'10月'),
        (11, u'11月'),
        (12, u'12月'),
    )
    author = models.CharField(max_length=120, verbose_name='作者')
    age = models.CharField(max_length=120, verbose_name='作者年龄')
    name = models.CharField(max_length=120, verbose_name='作品名字')
    type_id = models.ForeignKey(CustomerWorkType, null=True, verbose_name='作品类型')
    month = models.IntegerField(verbose_name='月份', choices=Month)
    like_ips = models.ManyToManyField(IpSet, verbose_name='点赞ip', blank=True,)
    image = models.ImageField(blank=True, upload_to='customer_work/%Y%m%d', verbose_name='小艺术家作品')

    class Meta:
        verbose_name = '小艺术家作品'
        verbose_name_plural = "小艺术家作品"

    def __unicode__(self):
        return self.name



