from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def askForm(request):
    return render(request, 'askForm.html')
def question(request):
    return render(request, 'question.html')
def settings(request):
    return render(request, 'settings.html')
def tag(request):
    return render(request, 'tag.html')