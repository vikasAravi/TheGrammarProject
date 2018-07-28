from django.shortcuts import render
from django.forms import ModelForm
from application.models import User
from django.http import HttpResponse
from application.models import Question
from application.models import AnswerScript
from django import forms
import enchant
import re
import datetime
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','password']


def index(request):
    total = True
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = UserForm()
    context = {'form': form, 'total': total}
    return render(request,template_name = 'index2.html',context = context)


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','password']

def custom(request):
    check = False
    description = ''
    total = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            em = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            query_set = (User.objects.filter(email = em)) & (User.objects.filter(password = pwd))
            if not query_set:
                check = True
                description = "you should check your credits"
            else:
                data = Question.objects.all()
                context = {'data' : data}
                return render(request,template_name = 'index3.html',context=context)
    else:
        form = LoginForm()
    context = {'form': form, 'check':check, 'description': description,'total': total}
    return render(request,template_name = 'index.html',context = context)

class AnswerForm(ModelForm):
    class Meta:
        model = AnswerScript
        fields = ('answer_text',)



def object_specific_view(request,oid):
    object = Question.objects.filter(id = oid).first()
    check = "no"
    user_length = 0
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            # dt = datetime.datetime.now()
            check = "yes"
            data = form.cleaned_data['answer_text']
            d = enchant.Dict("en_US")
            splitted_data = re.sub('|\?|\.|\!|\/|\;|\:', '', data).split()
            for word in splitted_data:
                if(d.check(word) == False):
                    user_length += 1
                    print(word)
            form.save()
    else:   
        form = AnswerForm()
    context = {
        'object' : object,
        'form' : form,
        'user_length': user_length,
        "check": check,
    }
    return render(request, template_name = 'index4.html', context = context)