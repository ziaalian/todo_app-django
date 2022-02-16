from multiprocessing import context
from turtle import title
from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        todos = Todo(
            title = request.POST['title']
        )
        todos.save()
        return redirect('/')
    context = {
        "todoz": todo
    }
    return render(request, 'index.html', context)

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

