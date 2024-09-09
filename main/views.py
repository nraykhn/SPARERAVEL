from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_app' : 'SPARERAVEL',
        'npm' : '2306275701',
        'name': 'Nur Alya Khairina',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)