
from django.urls import path
from . import views

urlpatterns = [
    path('', views.EigenValueSolverPage, name='EigenValueSolverPage'),

    path('EigenValueSolverPage', views.EigenValueSolverPage, name='EigenValueSolverPage'),
    path('EigenValueSolver', views.EigenValueSolver, name='EigenValueSolver'),

    path('EigenVectorSolverPage', views.EigenVectorSolverPage, name='EigenVectorSolverPage'),
    path('EigenVectorSolver', views.EigenVectorSolver, name='EigenVectorSolver'),

    path('DiagSymmetricSolverPage', views.DiagSymmetricSolverPage, name='DiagSymmetricSolverPage'),
    path('DiagSymmetricSolver', views.DiagSymmetricSolver, name='DiagSymmetricSolver'),
]
