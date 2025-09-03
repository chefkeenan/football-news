from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406398186',
        'name': 'Ahmad Keenan Aryasatya Gamal',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
