from django.urls import path
from. import views

urlpatterns=[
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:category_slug>/', views.category_detail, name='category_detail'),
]
