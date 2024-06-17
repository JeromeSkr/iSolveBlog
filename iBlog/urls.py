from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('register/',views.register, name='register'),
    path('login_page/',views.login_page, name='login_page'),
    path('logout_page/', views.logout_page, name='logout_page'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('details/<int:post_id>', views.details, name='details')
]