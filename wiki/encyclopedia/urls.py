from django.urls import path

from . import views
app_name="MyApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/q",views.search,name="search"),
    path("newpage",views.newpage,name="newpage"),
    path("random",views.random_page,name="random"),
    path("edit/<str:title>",views.edit,name="edit"), 
    path("<str:title>",views.entry_page,name="entries")
    
]
   

