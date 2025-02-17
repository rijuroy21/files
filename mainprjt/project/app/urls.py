from django.urls import path
from. import views

urlpatterns=[
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('how_it_works/', views.how_it_works, name='how_it_works'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('subcategories/<int:subcategory_id>/', views.subcategory_detail, name='subcategory_detail'),
    path('join/',views.join,name='join'),
    path('profile/<int:freelancer_id>/',views.profile,name='profile'),
]