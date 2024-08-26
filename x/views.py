from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        print(request.POST)
        return HttpResponseRedirect(reverse("index"))


#    elif request.method == "POST" and request.POST["2FA"]: pass
