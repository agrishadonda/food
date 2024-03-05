from django.urls import path
from.import views

urlpatterns = [
    path("",views.hotel.as_view(),name='hotel'),
    path("about/",views.about.as_view(),name='about'),
    path("menu/",views.menu.as_view(),name='menu'), 
    path("blog/",views.blog.as_view(),name='blog'),
    path("contact/",views.contact.as_view(),name='contact'),
    path("form/",views.form,name = 'form')
   
]
