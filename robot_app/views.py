from django.shortcuts import render
import os
# Create your views here.
def home(request):
    return render(request,'robot/index.html')
def upload(request):
    print(request.POST)
    file_name =os.path.join('catch',request.POST['name'])
    file = request.FILES['file']
    with open(file_name,'wb') as f:
        f.write(file.read())
    return render(request, 'robot/index.html')