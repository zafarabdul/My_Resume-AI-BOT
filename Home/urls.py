from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("send-message/", views.send_message, name="send_message"),
]
