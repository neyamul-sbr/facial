from django.urls import path
from .import views

urlpatterns = [
    path("",views.upload_img, name="UploadImage"),
    path("success", views.result, name="result")


]