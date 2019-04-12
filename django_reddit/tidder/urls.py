from django.urls import path, include
from . import views
from rest_framework import routers

router = router.DefaultRouter()
router.register('posts', views.PostView)
router.register('comments', views.CommentsView)
router.register('users', views.UserView)
router.register('profiles', views.ProfileView)

urlpatterns = [
  path('', include(router.urls))

]