from django.urls import path
from . import views

urlpatterns = [
    path('add',views.add,name='add'),
    path('detail/<int:pk>',views.detailview.as_view(),name='detail'),
    path('update/<int:pk>',views.updateview.as_view(),name='update'),
    path('delete/<int:pk>',views.deleteview.as_view(),name='delete'),
    path('new/',views.listview.as_view(),name='new'),
    path('',views.listview.as_view(),name='home')
]