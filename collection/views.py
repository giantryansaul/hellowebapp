from django.shortcuts import render

# Create your views here.
def index(request):
    # This is your new view
    return render(request, 'index.html')
