from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('add',views.add,name='add'),
    path('',views.login,name='login'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('details/<int:pk>',views.details,name='details'),
    path('view_student/<int:id>',views.view_student,name='view_student'),
]