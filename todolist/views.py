from django.shortcuts import render, redirect
from .models import TodoItems

# Create your views here.
def index(request):
    todo_list = TodoItems.objects.all()
    data = {
        "todo_list": todo_list
    }
    return render(request, "index.html", data)

def addTodo(request):
    item = TodoItems(content=request.POST['item'])
    item.save()
    return redirect("index")

def deleteTodo(request, id):
    item_delete = TodoItems.objects.get(id=id)
    item_delete.delete()
    return redirect("index")