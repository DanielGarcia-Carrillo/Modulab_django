from django.shortcuts import render


def main_page(request):
    return render(request, 'frontend/landing.html')