from django.shortcuts import render
from django.http import  HttpResponse
from .models import Question
# Create your views here.

def index(request):
    myname = "Minh An"
    profile1 = ["Điện thoại","máy tính","Máy bay","nhiều tiền"]
    context = {"name":myname,"profile" :profile1}
    return render(request, "polls/index.html",context)

def viewlist(request):
    list_question = Question.objects.all()
    context = {"list_quest":list_question}
    return render(request,"polls/question_List.html",context)

def detailView(requset,question_id):
    q = Question.objects.get(pk = question_id)
    return render(requset,'polls/details_question.html',{'qs' : q})

def vote(request,question_id):
    q = Question.objects.get(pk = question_id)
    try:
        data = request.POST["choice"]
        c = q.choice_set.get(pk=data)
    except:
        HttpResponse("Loi khong co choicce")
    c.vote = c.vote + 1
    c.save()
    return render(request,'polls/result.html',{'q' : q})

