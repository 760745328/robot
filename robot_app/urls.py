from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('upload_audio/',views.upload)

]
