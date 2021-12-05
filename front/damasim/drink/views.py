from django.shortcuts import render
from .models import Bev14Prep
from django.db import connection
import random
import json
from .recsys import Recsys

# Create your views here.
def index(request):
    return render(request, 'drink/index.html')

def survey(request):
    curs = connection.cursor() #커서 연결
    sqlstr = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='rec' AND `TABLE_NAME`='db';" #Mysql Query
    curs.execute(sqlstr)
    columnnames_tp = curs.fetchall() #튜플 형태로 컬럼명을 받아옴
    columnname_list = [x[0] for x in columnnames_tp] #list comprehension
    # print(columnname_list)
    COL_SIZE = len(columnname_list) - 1 # Id컬럼을 제외한 아이템 수
    RAND_SIZE = 20 #랜덤하게 뽑을 숫자의 수

    random_index = random.sample(range(1,COL_SIZE + 1), RAND_SIZE) #랜덤하게 가져올 인덱스 숫자
    columnname_list_shuffled = []

    for i in range(0, RAND_SIZE):
        # print(f'{columnname_list[random_index[i]]} 는 {random_index[i]}번째')
        columnname_list_shuffled.append(columnname_list[random_index[i]])
        # columnname_list_shuffled.append(columnname_list[i])2
    connection.close()
    # print(columnname_list_shuffled)

    drink_List=zip(random_index, columnname_list_shuffled)
    # 랜덤하게 10개 받아서 인덱스 저장해놓고, 프론트로 그거로 html출력
    # 그 인덱스대로 점수 저장할 예정

    return render(request, 'drink/survey.html', {'drink_List':drink_List})

def recommend(request):
    curs = connection.cursor() #커서 연결
    sqlstr = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='rec' AND `TABLE_NAME`='db';" #Mysql Query
    curs.execute(sqlstr)
    columnnames_tp = curs.fetchall() #튜플 형태로 컬럼명을 받아옴
    columnname_list = [x[0] for x in columnnames_tp] #list comprehension
    connection.close()

    RECOMMEND_NO = 15 # 추천할 아이템의 갯수

    if request.method == 'POST':

        bevQueryDict = request.POST
        bevDict = bevQueryDict.dict()
        result = Recsys(bevDict, RECOMMEND_NO)
        drink_List=[]
        for index, score in result.items():
            drink_List.append(columnname_list[index]) # 점수 상위 15개 음료수 이름목록
        print(drink_List)
        return render(request, 'drink/recommend.html', {'result': result, 'drink_List':drink_List})


# def dbtest(request):

#     curs = connection.cursor() #커서 연결
#     sqlstr = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='rec' AND `TABLE_NAME`='db';" #Mysql Query
#     curs.execute(sqlstr)
#     columnnames_tp = curs.fetchall() #튜플 형태로 컬럼명을 받아옴
#     columnname_list = [x[0] for x in columnnames_tp] #list comprehension
#     # print(columnname_list)
#     COL_SIZE = len(columnname_list) - 1 # Id컬럼을 제외한 아이템 수
#     RAND_SIZE = 20 #랜덤하게 뽑을 숫자의 수

#     random_index = random.sample(range(1,COL_SIZE + 1), RAND_SIZE) #랜덤하게 가져올 인덱스 숫자
#     columnname_list_shuffled = []

#     for i in range(1, RAND_SIZE):
#         print(f'{columnname_list[random_index[i]]} 는 {random_index[i]}번째')
#         columnname_list_shuffled.append(columnname_list[random_index[i]])
#         # columnname_list_shuffled.append(columnname_list[i])
#     connection.close()

#     # print(columnname_list_shuffled)

#     drink_List=zip(random_index, columnname_list_shuffled)
#     # 랜덤하게 10개 받아서 인덱스 저장해놓고, 프론트로 그거로 html출력
#     # 그 인덱스대로 점수 저장할 예정

#     # return render(request, 'drink/dbtest.html', {'index':random_index, 'drink_List': columnname_list_shuffled})
#     return render(request, 'drink/dbtest.html', {'List':drink_List})
#     # return render(request, 'drink/dbtest.html')

