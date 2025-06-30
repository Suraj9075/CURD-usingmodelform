from django.shortcuts import render , HttpResponseRedirect,redirect
from .froms import StudentRegistration
from .models import User
# This funtion will add new item and show all items
def add_show(request):
    if request.method== 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            redirect('/')
    else:
        fm = StudentRegistration()
    stud=User.objects.all()
    return render (request,'enroll/addandshow.html', {'form':fm, 'stu':stud })

# this funtion will delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# this funtion will Update /Edit
def update_data(request, id):
    pi = User.objects.get(pk=id)
    
    if request.method == 'POST':
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi =User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    return render(request, 'enroll/updatestudent.html', {'form': fm})
