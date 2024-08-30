from django.urls import path
from . import views

urlpatterns = [
    path('', views.kurakani_list, name = 'kurakani_list'),
    path('create/', views.kurakani_create, name = 'kurakani_create'),
    path('<int:kurakani_id>/edit/', views.kurakani_edit, name = 'kurakani_edit'),
    path('<int:kurakani_id>/delete/', views.kurakani_delete, name = 'kurakani_delete'),
]