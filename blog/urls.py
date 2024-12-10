from django.urls import path
from .views import main, detail
# from . import views

urlpatterns = [
    path("", main, name="home"),
    path("<int:pk>", detail, name='more info'),
]