from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),

    path("ajax_get_topics", views.ajax_get_topics, name="ajax_get_topics"),

    path("tag_erfassen", views.tag_erfassen, name='tag_erfassen'),
]
