from django.shortcuts import render
from .models import Bev14Prep
from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'drink/index.html')

def survey(request):
    return render(request, 'drink/survey.html')

def dbtest(request):
    #beverages = Bev14Prep.objects.all()

    #coke = beverages.filter(myunknowncolumn=0)

    cokescore = Bev14Prep.objects.values("coca_cola_classic_coke")

    return render(request, 'drink/dbtest.html', {'cokescore': cokescore})

    """
    try:
        cursor = connection.cursor()

        strSql = "SELECT 코카콜라_coca_cola_classic_coke_field FROM beverage14.bev14_prep"
        result = cursor.execute(strSql)
        bevCoke = cursor.fetchall()

        connection.commit()
        connection.close()

    except:
        connection.rollback()
        print("Failed selecting in beverage14.bev14_prep")

    return render(request, 'dbtest.html', {'bevCoke': bevCoke})
    """