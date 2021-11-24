
from django.urls import path
from . import views

urlpatterns = [
    path('',views.determinant,name='determinant'),
    path('answer', views.answer, name='answer'),
    path('test', views.test),
    path('csrf', views.csrftest),
]
