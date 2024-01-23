from django.contrib import admin
from .models import Topico, Tag, Post

admin.site.register(Topico)
admin.site.register(Tag)
admin.site.register(Post)
