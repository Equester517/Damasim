from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'drink/index.html')

def survey(request):
    return render(request, 'drink/survey.html')