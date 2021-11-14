from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'drink/index.html')

def recommend(request):
    return render(request, 'drink/recommend.html')