from django.shortcuts import render

from .translator import translate


def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        output_text = translate(original_text)
        return render(request, 'translator.html')
    return render(request, 'translator.html')
