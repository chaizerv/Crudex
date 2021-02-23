from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_form, name='create'),
    path('read/', views.read, name='read'),
    path('<int:id>/', views.create_form, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

]