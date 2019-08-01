from django.contrib import admin

from .models import *
#首先
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(ArticleDetail)
admin.site.register(Comment)
admin.site.register(ArticleUpDown)
admin.site.register(Article2Tag)
admin.site.register(Category)


