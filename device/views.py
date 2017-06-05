from django.shortcuts import render


def home(request):

    return render(request, "businesses/dashboard.html")