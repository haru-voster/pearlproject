from tempfile import template

from django.shortcuts import render

# Create your views here.
def  home(request):
    return render(request, template_name='index.html')

def meetings(request):
    return render(request, template_name='meetings.html')

def meeting_details(request):
    return render(request, template_name='meeting_details.html')

