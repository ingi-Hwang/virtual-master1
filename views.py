from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .form import QuestionForm
from datetime import timezone
from .models import *
# Create your views here.

# def index(request):
#     if request.method == 'POST':
#         user = User()
#         user.name = request.POST['name']
#         user.age = request.POST['age']
#         user.gender = request.POST['gender']
#         user.date = request.POST.get('date')
#         user.time = request.POST.get('time')
#         user.save()
#         print(user.name,'\n')
#         print(user.age,'\n')
#         print(user.gender,'\n')
#         print(user.date,'\n')
#         print(user.time)
#         return redirect('user')
#     else:
#         user = User.objects.all()
#         return render(request, 'community/index.html', {'user':user})
#
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.name = request.POST['name']
            user.age = request.POST['age']
            user.gender = request.POST['gender']
            user.save()
            return redirect('community:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'community/index.html', context)
