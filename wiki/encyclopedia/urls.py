from django.urls import path

from . import views
app_name="MyApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("newpage",views.newpage,name="newpage"),
    path("<str:title>",views.entry_page,name="entries"), 
    path("search/q",views.search,name="search"),
    path("hey",views.hey,name="hey")
]

