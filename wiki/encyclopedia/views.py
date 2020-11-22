from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request,title):
   e=util.list_entries()
   for i in e:
       if i==title:
            return render(request,"encyclopedia/content.html",{
                "title":title,
                "content":util.get_entry(title)

             })
       else:
           return HttpResponse("<h1>WRONG PAGE</h1>")

 

def search(request):
    
    e=util.list_entries()
    text=request.POST['q']
    for i in e:
        if i==text:
    
            return render(request,"encyclopedia/searchresult.html",
               {
                   "title":text,
                   "content":util.get_entry(text)
               })
    else:       
          
        return  HttpResponse("<h1>WRONG PAGE</h1>")

def newpage(request):
    
    e=util.list_entries()
    
    if request.POST:
            for i in e:
                if i==request.POST['t']:
                    return  HttpResponse("<h1>Page already exists</h1>")
                else:    
                    util.save_entry(request.POST['t'],request.POST['c'])  
                    return HttpResponseRedirect(reverse("MyApp:index"))

            
    else:
            return render(request,"encyclopedia/newpage.html")

def hey(request):
    return render(request,"encyclopedia/hey.html")    
