#_*_coding:utf-8_*_
from django.conf.urls import url,include
from django.contrib import admin
from  . import views
from robud_website import views as website_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', website_views.index, name='index'),
    url(r'aboutus/$', website_views.aboutus_story, name='aboutus_story'),
    url(r'aboutusteam/$', website_views.aboutus_team, name='aboutus_team'),
    url(r'aboutuspromise/$', website_views.aboutus_promise, name='aboutus_promise'),
    url(r'purchasechannels/$', website_views.purchasechannels, name='purchasechannels'),
    url(r'contact/$', website_views.contact, name='contact'),
    url(r'products/$', website_views.products, name='products'),
    url(r'products/(?P<key>[a-zA-Z]+)/(?P<id>\d+)', website_views.products, name='products'),
    url(r'get_labels/$', website_views.get_labels, name='get_labels'),
    url(r'news_index/$', website_views.news_index, name='news_index'),
    url(r'video_index/(?P<id>\d+)?', website_views.video_index, name='video_index'),
    url(r'customer_work/$', website_views.customer_work, name='customer_work'),
    url(r'like/$', website_views.like, name='like'),
    url(r'get_artists_work/$', website_views.get_artists_work, name='get_artists_work'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
