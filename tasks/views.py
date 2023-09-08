from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import request
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

tasks = ["bar", "foo", "fo"]


class NewTask(forms.Form):
    task = forms.CharField(label="New tasks")
    # priority = forms.IntegerField(label="priority", min_value=1, max_value=4)


def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add(request):
    print(0)
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return render(request, "tasks/index.html", {
                "tasks": tasks
            })
        else:
            print("2")
            return HttpResponseRedirect(reverse("tasks:index"))
    print(3)
    return render(request, "tasks/add.html", {
        "form": NewTask()
    })
