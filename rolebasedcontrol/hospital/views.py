from django.shortcuts import render, HttpResponse,redirect
from .models import user_type,NewUser,Patients
from django.contrib.auth import authenticate, login
from .form import PatientForm, SurgeonForm

def dashboard(request):
    return render(request,'users/dashboard.html')

def signup(request,name):

    if request.method == 'POST':
        name1 = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(name1,email,password)
        user = NewUser.objects.create_user(
            email=email,
            user_name=name1,

            password=password,
        )
        user.set_password(password)
        user.save()
        usert = None

        if name == 'doctor':
            usert = user_type(user=user, is_doctor=True)

        elif name == 'nurse':
            usert = user_type(user=user, is_nurse=True)

        else:
            usert = user_type(user=user, is_surgeon=True)


        usert.save()
        # Successfully registered. Redirect to homepage
        return redirect('dashboard')

    return render(request, 'users/signup.html')

def loginpage(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')  # Get email value from form
        password = request.POST.get('password')  # Get password value from form
        print(email,password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            print(1)
            login(request, user)
            type_obj = user_type.objects.get(user=user)
            if(type_obj.is_doctor or type_obj.is_nurse or type_obj.is_surgeon):
                print(1)
            if user.is_authenticated and type_obj.is_doctor:
                return redirect('doctor')
            if user.is_authenticated and type_obj.is_nurse:
                return redirect('nurse')
            if user.is_authenticated and type_obj.is_surgeon:
                return redirect('surgeon')


    return render(request, 'users/login.html')

def doctor(request):
    all = Patients.objects.all()

    return render(request,'users/view.html',{'all':all})

def nurse(request):
    all = Patients.objects.all()

    return render(request,'users/viewnurse.html',{'all':all})

def surgeon(request):
    all = Patients.objects.all()

    return render(request,'users/viewsurgeon.html',{'all':all})

def createuserbyd(request):
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('doctor')

    context = {'form':form}
    return render(request,'users/form.html',context)


def createuserbyn(request):
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('nurse')

    context = {'form': form}
    return render(request, 'users/form.html', context)



def updateuserbyd(request,pk):
    user = Patients.objects.get(id=pk)

    form = PatientForm(instance=user)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=user)
        if form.is_valid:
            form.save()
            return redirect('doctor')
    context = {'form': form}
    return render(request, 'users/form.html', context)

def updateuserbyn(request,pk):
    user = Patients.objects.get(id=pk)

    form = PatientForm(instance=user)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=user)
        if form.is_valid:
            form.save()
            return redirect('nurse')
    context = {'form': form}
    return render(request, 'users/form.html', context)

def updateuserbys(request,pk):
    user = Patients.objects.get(id=pk)

    form = SurgeonForm(instance=user)
    if request.method == 'POST':
        form = SurgeonForm(request.POST, instance=user)
        if form.is_valid:
            form.save()
            return redirect('surgeon')
    context = {'form': form}
    return render(request, 'users/form.html', context)

def deleteuser(request,pk):
    user = Patients.objects.get(id=pk)
    user.delete()
    return redirect('doctor')


