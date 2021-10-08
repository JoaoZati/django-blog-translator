from django.shortcuts import render

from .translator import translate


def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        if not original_text:
            return render(
                request,
                'translator.html',
            )
        output_text = translate(original_text)
        return render(
            request,
            'translator.html',
            {'original_text': original_text, 'output_text': output_text}
        )
    return render(
        request,
        'translator.html',
    )
