from django.urls import path, include
from . import views
from rest_framework import routers

router = router.DefaultRouter()
router.register('posts', views.PostView)
router.register('comments', views.CommentsView)
router.register('users', views.UserView)
router.register('profiles', views.ProfileView)
router.register('comment_votes', views.Comment_VotesView)
router.register('saves', views.SaveView)
router.register('post_votes', views.Post_VoteView)

urlpatterns = [
  path('', include(router.urls))

]