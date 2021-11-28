from django.shortcuts import render
from .models import Bev14Prep
from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'drink/index.html')

def survey(request):
    return render(request, 'drink/survey.html')

def dbtest(request):

    cokescore = Bev14Prep.objects.values("coca_cola_classic_coke")
    cokezeroscore = Bev14Prep.objects.values("coca_cola_zero_sugar")

    return render(request, 'drink/dbtest.html', {'cokescore': cokescore, 'cokezeroscore':cokezeroscore})
