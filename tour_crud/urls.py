from django.urls import path
from . import views


urlpatterns = [
    path('company_list/', views.company_list_view, name='company_list'),
    path('create_list/', views.create_company_view, name='company_create'),
    path('update_list/<int:id>/update/', views.update_company_view, name='edit_list'),
    path('delete_list/<int:id>/delete/', views.delete_company_view, name='del_list'),
]
