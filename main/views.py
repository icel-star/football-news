from django.shortcuts import render


def show_main(request):
    context = {
        'npm' : '2406415116',
        'name': 'giselle julia reyna',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)