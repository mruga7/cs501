from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect, request
from django.urls import reverse
import random
from markdown2 import Markdown
markdowner=Markdown()

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def search(request):
    
    e=util.list_entries()
    text=request.POST['q']
    foundentries=[]
    
    if text not in e:
        for i in e:    
            if i.startswith(text):
                foundentries.append(i)  
                print(i)
                print(foundentries)  
        if len(foundentries)!=0:                
          return render(request,"encyclopedia/index.html",{
                 "entries":foundentries
                 })
        else:
            return HttpResponse("<h1> ERROR: PAGE DOES NOT EXIST </h1> ")         

    elif text in e:
        return render(request,"encyclopedia/content.html",{
            "title":text,
            "content":markdowner.convert(util.get_entry(text))}
            )                    
               
    
    else:
        return HttpResponse("<h1>ERROR: PAGE DOES NOT EXIST </h1>")
    



    

def newpage(request):
    
    e=util.list_entries()
    
    if request.POST:
        i=request.POST['t']
        if i in e:
                
                return  HttpResponse("<h1>PAGE ALREADY EXISTS </h1>")
        else:    
                util.save_entry(request.POST['t'],request.POST['c'])  
                return HttpResponseRedirect(reverse("MyApp:index"))

            
    else:
            return render(request,"encyclopedia/newpage.html")

def edit(request,title):
    if request.POST:
        
        util.save_entry(title,request.POST['c'])  
        #return HttpResponseRedirect(reverse("MyApp:cd"))
        return render(request,"encyclopedia/content.html",{
            "title":title,
            "content":markdowner.convert(request.POST['c'])
        })
    else:
        return render(request,"encyclopedia/edit.html",
        {
        "title":title,
        "content":util.get_entry(title)
        })  

def entry_page(request,title):
    e=util.list_entries()
   
    if title in e:
        return render(request,"encyclopedia/content.html",{
                "title":title,
                "content":markdowner.convert(util.get_entry(title))

             })
    
    else:
        return HttpResponse("<h1>ERROR: PAGE DOES NOT EXIST</h1>")     

def random_page(request):
    page=random.choice(util.list_entries())
    return render(request,"encyclopedia/content.html",{
                "title":page,
                "content":markdowner.convert(util.get_entry(page))

                })

def searchresult(request,title):
    return render(request,"encyclopedia/content.html",{
                "title":title,
                "content":markdowner.convert(util.get_entry(title))

                })
