from django.urls import path
# from student import views
from . import views
urlpatterns = [
    path("", views.index),
    path("base/", views.BaseDBView.as_view()),
    path("db/", views.DBView.as_view()),
]
