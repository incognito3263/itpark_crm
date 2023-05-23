from django.urls import path
from clinet import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('category_list/', views.category_list, name="category_list"),
    path('category_create/', views.category_create, name="category_create"),
    path('<int:pk>category_edit/', views.category_edit, name="category_edit"),
    path('<int:pk>/category_delete/', views.category_delete, name="category_delete"),

    path('courses_list/', views.courses_list, name="courses_list"),
    path('courses_create/', views.courses_create, name="courses_create"),
    path('<int:pk>courses_edit/', views.courses_edit, name="courses_edit"),
    path('<int:pk>/courses_delete/', views.courses_delete, name="courses_delete"),

    path('teacher_create/', views.teacher_create, name="teacher_create"),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('<int:pk>/teacher_edit/', views.teacher_edit, name="teacher_edit"),
    path('<int:pk>/teacher_delete/', views.teacher_delete, name="teacher_delete"),

    path('grup_create/', views.grup_create, name="grup_create"),
    path('grup_list/', views.grup_list, name='grup_list'),
    path('<int:pk>/grup_edit/', views.grup_edit, name="grup_edit"),
    path('<int:pk>/grup_delete/', views.grup_delete, name="grup_delete"),
    path('<int:id>/grup_info/', views.grup_info, name="grup_info"),
    path('users_per/', views.users_per, name="users_per"),
    path('<int:id>/grup_mouht/', views.grup_mouht, name="grup_mouht"),

    path('teacher_create/', views.teacher_create, name="teacher_create"),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('<int:pk>/teacher_edit/', views.teacher_edit, name="teacher_edit"),
    path('<int:pk>/teacher_delete/', views.teacher_delete, name="teacher_delete"),

    path('users_create/', views.users_create, name="users_create"),
    path('users_list/', views.users_list, name='users_list'),
    path('<int:pk>/users_edit/', views.users_edit, name="users_edit"),
    path('<int:pk>/users_delete/', views.users_delete, name="users_delete"),
    path('<int:id>/user_info/', views.user_info, name="user_info"),

    path('month_create/', views.month_create, name="month_create"),
    path('month_list/', views.month_list, name='month_list'),
    path('<int:pk>/month_edit/', views.month_edit, name="month_edit"),
    path('<int:pk>/month_delete/', views.month_delete, name="month_delete"),



]
