from django.shortcuts import render
from .models import Bev14Prep
from django.db import connection
import random
import json

# Create your views here.
def index(request):
    return render(request, 'drink/index.html')

def survey(request):
    return render(request, 'drink/survey.html')

def dbtest(request):

    curs = connection.cursor() #커서 연결
    sqlstr = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='beverage14' AND `TABLE_NAME`='bev14_prep';" #Mysql Query
    curs.execute(sqlstr)
    columnnames_tp = curs.fetchall() #튜플 형태로 컬럼명을 받아옴
    columnname_list = [x[0] for x in columnnames_tp] #list comprehension

    COL_SIZE = len(columnname_list) - 1 # Id컬럼을 제외한 아이템 수
    RAND_SIZE = 10 #랜덤하게 뽑을 숫자의 수

    random_index = random.sample(range(1,COL_SIZE + 1), RAND_SIZE) #랜덤하게 가져올 인덱스 숫자
    columnname_list_shuffled = []

    for i in range(1, RAND_SIZE):
        #print(f'{columnname_list[random_index[i]]} 는 {random_index[i]}번째')
        columnname_list_shuffled.append(columnname_list[random_index[i]])
    connection.close()

    print(columnname_list_shuffled)

    #랜덤하게 10개 받아서 인덱스 저장해놓고, 프론트로 그거로 html출력
    #그 인덱스대로 점수 저장할 예정

    return render(request, 'drink/dbtest.html', {'random_index': random_index})

def post(request):

    if request.method =='POST':

        #from .recsys import Recsys #.recsys 파일에서 Recsys 함수 import
        #JSON 형태의 값 N개를 받아서, recsys.py에서 실행

        #input = json.loads(request.body)["bev"]["score"]

        #result = Recsys.USERMETHOD(input)
        #context = {
        # 'result' : result
        #}
        #return render(request, result.html,context)

        return render(request, 'drink/dbtest.html', '')