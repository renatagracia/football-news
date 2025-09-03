from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406399705',
        'name': 'Renata Gracia Adli',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)