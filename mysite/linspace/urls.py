from django.urls import path
from . import views

urlpatterns = [
    path('', views.MLIGSolverPage),
    path('MLIGSolverPage', views.MLIGSolverPage, name='MLIGSolverPage'),
    path('MLIGSolver', views.MLIGSolver, name='MLIGSolver'),

    path('LincombinationSolverPage', views.LincombinationSolverPage, name='LincombinationSolverPage'),
    path('LincombinationSolver', views.LincombinationSolver, name='LincombinationSolver'),

    path('LinDependenceSolverPage', views.LinDependenceSolverPage, name='LinDependenceSolverPage'),
    path('LinDependenceSolver', views.LinDependenceSolver, name='LinDependenceSolver'),

    path('BasisTransSolverPage', views.BasisTransSolverPage, name='BasisTransSolverPage'),
    path('BasisTransSolver', views.BasisTransSolver, name='BasisTransSolver'),
]