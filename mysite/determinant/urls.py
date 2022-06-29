
from django.urls import path
from . import views

urlpatterns = [
    path('',views.DeterminantSolver,name='DeterminantSolver'),

    path('DeterminantSolverPage', views.DeterminantSolverPage, name='DeterminantSolverPage'),
    path('DeterminantSolver', views.DeterminantSolver, name='DeterminantSolver'),

    path('GaussDeterminantSolverPage', views.GaussDeterminantSolverPage, name='GaussDeterminantSolverPage'),
    path('GaussDeterminantSolver', views.GaussDeterminantSolver, name='GaussDeterminantSolver'),
]


