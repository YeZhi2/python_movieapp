from django.urls import  path
from moviesapp import views
urlpatterns=[
    path('getbyid/',views.getbyid),
    path('all/',views.getall),
    path('new/',views.newmovie),
    path('save/',views.save),
    path('alljson/',views.get_json),
    path('delete/',views.delete),
    path('do_delete/',views.do_del),
    path('update/',views.update),
    path('updatemovie/',views.updatemovie),
    path('search/',views.search),
]