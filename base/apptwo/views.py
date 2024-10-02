from django.shortcuts import render

def home(request):
    return render(request, 'apptwo/home.html')

def enroll(request):
    return render(request, 'apptwo/enroll.html')

def feedback(request):
    return render(request, 'apptwo/feedback.html')

