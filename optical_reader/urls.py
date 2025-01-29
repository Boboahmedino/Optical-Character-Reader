from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name = 'upload_image'),
    path('upload_pdf', views.upload_pdf, name = 'upload_pdf')
]