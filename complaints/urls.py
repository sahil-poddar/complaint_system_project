from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_complaint, name='submit_complaint'),
    path('list/', views.complaint_list, name='complaint_list'),
    path('update/<int:pk>/', views.update_status, name='update_status'),
    path('delete/<int:pk>/', views.delete_complaint, name='delete_complaint'),
]
