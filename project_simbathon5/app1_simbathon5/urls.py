from django.urls import path
from .views import *
from app1_simbathon5 import views
app_name = "app1_simbathon5"
urlpatterns = [
    path('', showmain, name= "showmain"),
    path('FAQ/', frequentlyaskedquestions , name= "frequentlyaskedquestions"),
    path('<str:id>', views.detail, name="detail"),
]