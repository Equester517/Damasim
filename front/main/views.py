from django.shortcuts import render # django.shorcuts패키지에있는 render라는 함수를 사용

def mainPage(request):
    return render(request,'main/mainpage.html')

# def 함수이름(인자):
# 함수를 호출했을 때 실행될 코드