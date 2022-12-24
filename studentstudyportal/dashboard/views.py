from django.shortcuts import render,redirect
from .form import *
from django.contrib import messages
from django.views import generic
from youtubesearchpython import VideosSearch
from django.contrib.auth.decorators import login_required 

# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

@login_required
def notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user , title=request.POST['title'] , description=request.POST['description'])
            notes.save()
        messages.success(request,f'Notes Added From {request.user.username} Successfully!')
    else:
        form = NotesForm
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)

@login_required
def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('notes')


class NotesDetailView(generic.DetailView):
    model = Notes

@login_required
def homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False

            homeworks = Homework(
                user = request.user,
                subject = request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished
            )
            homeworks.save()
            messages.success(request,f'HomeWork Added From {request.user.username}!!')
    else:
        form = HomeworkForm()
    homework = Homework.objects.filter(user = request.user)

    # This Content Use any homework is pending it will show on top if all hw are complete it will say (all completed)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False
    # End of thid content and pass the variable in context

    context = {
        'homeworks':homework,
        'homeworks_done':homework_done,
        'form':form
    }
    return render(request,'dashboard/homework.html',context)


# def update_homework(request,pk=None):
#     homework = Homework.objects.get(id=pk)
#     if homework.is_finished == True:
#         homework.is_finished == False
#     else:
#         homework.is_finished == True
#     homework.save()
#     return redirect('homework')

@login_required
def delete_homework(request,pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')

@login_required
def youtube(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text,limit=10)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input' : text,
                'title' : i['title'],
                'duration' : i['duration'],
                'thumbnail' : i['thumbnails'][0]['url'],
                'channel' : i['channel']['name'],
                'link' : i['link'],
                'views' : i['viewCount']['short'],
                'published': i['publishedTime']
            } 
            result_list.append(result_dict)
            context = {'form':form , 'results':result_list}
        return render(request,'dashboard/youtube.html',context)
    else:
        form = DashboardForm()
    context = {'form':form}
    return render(request,'dashboard/youtube.html',context)

@login_required
def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            todos = Todo (
                user = request.user,
                title = request.POST['title'],
                is_finished = finished
            )
            todos.save()
            messages.success(request,f'Todo Added From {request.user.username}!!')
    else:
        form = TodoForm
    todo = Todo.objects.filter(user=request.user)
    if len(todo) == 0:
        todos_done = True
    else:
        todos_done = False
    context = {
        'todos' : todo,
        'form' : form,
        'todos_done' : todos_done
    }
    return render(request,'dashboard/todo.html',context)


# def update_todo(request,pk=None):
#     todo = Todo.objects.get(id=pk)
#     if todo.is_finished == True:
#         todo.is_finished = False
#     else:
#         todo.is_finished == True
#     todo.save()
#     return redirect('todo')

@login_required
def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('todo')


def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created For {username}!!')
            return redirect('login')
    else:
        form = UserRegisterationForm()
    context = {'form':form}
    return render(request,'dashboard/register.html',context)

@login_required
def profile(request):
    homeworks = Homework.objects.filter(is_finished=False,user=request.user)
    todos = Todo.objects.filter(is_finished=False,user=request.user)
    if len(homeworks) == 0:
        homework_done = True
    else:
        homework_done = False
    if len(todos) == 0:
        todos_done = True
    else:
        todos_done = False
    context = {
        'homeworks' : homeworks,
        'todos' :  todos,
        'homework_done' : homework_done,
        'todos_done' : todos_done
    }
    return render(request,'dashboard/profile.html',context)