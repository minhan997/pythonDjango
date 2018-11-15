from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse
from .models import Question
# Create your views here.

def index(request):
    myname = "Minh An"
    profile1 = ["Điện thoại","máy tính","Máy bay","nhiều tiền"]
    context = {"name":myname,"profile" :profile1}
    return render(request, "polls/index.html",context)

def viewlist(request):
    list_question = get_object_or_404(Question, pk = 1)
    context = {"list_quest":list_question}
    return render(request,"polls/question_List.html",context)

