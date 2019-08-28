""" urls za wall app """
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.reg, name="wall"),
    path('', views.start_page, name="start_page"),
    path('dodaj', views.add, name="add"),
    path('delete_all', views.delete_all, name="delete_all"),
    path('delete', views.delete, name="delete"),
    path('deleted', views.deleted, name="deleted"),
    path('edit', views.edit, name="edit"),
    path('delete_all_final', views.delete_all_final, name="delete_all_final"),
    path('ajax_update_posts', views.ajax_update_posts, name="ajax_update_posts"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('wall', views.wall, name="wall"),
    path('logout', views.logout, name="logout")
]
