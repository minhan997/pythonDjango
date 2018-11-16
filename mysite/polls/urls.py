from django.urls import  path
from django.views.generic import  TemplateView
from . import  views

app_name = 'polls'

urlpatterns = [
    path('details/<int:question_id>',views.detailView,name = 'details'),
    path('list_quest/',views.viewlist,name='view_list'),
    path('',views.index,name='index'),
    path('<int:question_id>',views.vote,name='vote'),
]
