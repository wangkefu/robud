from django.contrib import admin

# Register your models here.
from robud_website.models import ApplyAge, Category, RobudProduct, VideoType, Videos, CustomerWork, CustomerWorkType, SecondTitle

admin.site.register(ApplyAge)
admin.site.register(Category)
admin.site.register(RobudProduct)
admin.site.register(VideoType)
admin.site.register(Videos)
admin.site.register(CustomerWork)
admin.site.register(CustomerWorkType)
admin.site.register(SecondTitle)