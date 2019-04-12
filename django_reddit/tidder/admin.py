from django.contrib import admin
from .models import Post, Comment, User, Profile
# Register your models here.

admin.site.register([Post, Comment, User, Profile])