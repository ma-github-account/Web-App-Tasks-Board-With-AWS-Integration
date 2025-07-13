from django.shortcuts import render, redirect

from .models import Todolist

from .forms import TodoListForm

from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    todo_items = Todolist.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_items' :todo_items, 'form' : form}
    return render(request,'todolist/index.html', context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)

    if form.is_valid():
        new_todo = Todolist(name=request.POST['name'],description=request.POST['description'])
        new_todo.save()
    
    return redirect('index')

def setStatusToInProgress(request, todo_id):  
    todo = Todolist.objects.get(pk=todo_id)
    todo.status = "In Progress"
    todo.save()

    return redirect('index')

def setStatusToDone(request, todo_id):  
    todo = Todolist.objects.get(pk=todo_id)
    todo.status = "Done"
    todo.save()

    return redirect('index')

def deleteTask(request, todo_id):  
    todo = Todolist.objects.get(pk=todo_id).delete()

    return redirect('index')

def deleteDoneTasks(request):
    Todolist.objects.filter(status__exact="Done").delete()

    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()

    return redirect('index')
