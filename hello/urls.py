from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("dinhthai",views.dinhthai,name="dinhthai"),
    path("<str:name>", views.greet, name="greet")
]