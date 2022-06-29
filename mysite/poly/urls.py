from django.urls import path
from . import views

urlpatterns = [
    path('',views.PolySolverPage),
    path('PolySolver', views.PolySolver, name='PolySolver'),
    path('PolySolverPage', views.PolySolverPage, name='PolySolverPage'),

    path('SchmidtPolySolver', views.SchmidtPolySolver, name='SchmidtPolySolver'),
    path('SchmidtPolySolverPage', views.SchmidtPolySolverPage, name='SchmidtPolySolverPage'),
]