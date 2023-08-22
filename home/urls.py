from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header="Login to Anurag's Admin Panel"
admin.site.site_title="Anurag's Admin Panel"
admin.site.index_title="Welcome to admin portal"

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('project/',views.project,name="project"),
    path('contact/',views.contact,name="contact"),
]