from django.shortcuts import render

def index(request):
    context = {}
    context["test"] = "test"
    return render(request,"index.html",context)


