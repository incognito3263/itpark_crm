from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', index, name="index"),
    path('dashboard/', include('clinet.urls')),
    path('course_our/', course_our, name="course_our"),
    path("course_detail/<int:id>/", course_detail, name="course_detail"),
    path('new_blog/<int:id>/', new_blog, name="new_blog"),
    path('new/', new, name="new"),
    # path('course_01/', course_01, name="course_01"),
    # path('grid_news/', grid_news, name="grid_news"),
    # path('news_details/<int:id>/', news_details, name="news_details"),
    # path('about/', about, name="about"),
    # path('contact/', contact, name="contact" )

    #     Dashboard urls start

]
