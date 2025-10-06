# 180295818
from django.contrib import admin
from .models import CSMediaPost, CSMediaComment, CSMediaLike
# Register your models here.

admin.site.register(CSMediaPost)
admin.site.register(CSMediaComment)
admin.site.register(CSMediaLike)