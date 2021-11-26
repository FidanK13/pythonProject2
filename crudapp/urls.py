from django.urls import path
from .views import index_view, post_create_view, post_read_view, post_update_view, post_delete_view, login_view, register_view

urlpatterns = [
    path('', index_view, name='home_page'),
    path('post-create/', post_create_view,name='post_create_page'),
    path('post-read/<int:post_id>', post_read_view, name='post_read_page'),
    path('post-update/<int:post_id>', post_update_view, name='post_update_page'),
    path('post-delete/<int:post_id>', post_delete_view, name='post_delete_page'),
    path('login/', login_view.as_view(), name='login_page'),
    path('register/', register_view.as_view(), name='register_page'),

]