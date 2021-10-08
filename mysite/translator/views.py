from django.shortcuts import render


def translator_view(request):
    return render(request, 'translator.html')
