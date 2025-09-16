from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name="index"),
    path('',views.menu,name="menu"),
    path('',views.book,name="book"),
    path('',views.about,name="about"),

]
