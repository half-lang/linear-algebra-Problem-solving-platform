
from django.urls import path
from . import views

urlpatterns = [
    path('',views.determinant,name='determinant'),
    path('answer', views.answer, name='answer'),

]

urlpatterns = [
    path('Determinantcalculator',views.HOME,name='HOME')
]

urlpatterns = [
    path('Eigenvalue',views.eigenvalue,name='eigenvalue')
]