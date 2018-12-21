from django.shortcuts import render

# Create your views here.
def home(request):
    l = ['html', 'css', 'jquery', 'python', 'django']
    return render(request, 'home.html', {'T_list':l})