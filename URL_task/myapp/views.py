from django.shortcuts import render
from django.http import HttpResponse

# to send HTML page:: render
# Two parameters are sent
def task(request):
    return render(request, "task.html")
    # task = Task.objects.get(id=1)

# to send String:: HttpResponse
def task1(request):
    return HttpResponse("HI")

