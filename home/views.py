from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import SavedRequest, Student,Request
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django import forms
from .models import Student
from .forms import StudentForm

def hello(request):
    return HttpResponse("Hello World 👋!")
def index(request):
    return render(request, 'index.html')

# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # ✅ PUT IT HERE
            return redirect('dashboard')

        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

# ---------------- REGISTER ----------------
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        roll = request.POST['roll']
        branch = request.POST['branch']

         # Create user
        user=User.objects.create_user(
            username=username, 
            password=password,
            email=email
        )
        # Save extra data in Student model
        Student.objects.create(
            user=user, 
            name=username,
            roll=roll,
            branch=branch,
            email=email
        )
        return redirect('login')

    return render(request, 'register.html')

# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect('home')

def send_requests(request, target_user_id):
    target_user= User.objects.get(id=target_user_id)

    if not Request.objects.filter(
        sender=request.user,
        receiver=target_user).exists():
            Request.objects.create(
                sender=request.user,
                receiver=target_user,
                status='Pending'
            )

            # ✅ SEND EMAIL
            send_mail(
                'Request from CampDesk',
                f'Hello {target_user.username}, you received a request.',
                '24b01a12i0@svecw.edu.in',
                [target_user.email],
                fail_silently=False,
            )
    return redirect('dashboard')

def saved_list(request):
    saved = SavedRequest.objects.filter(user=request.user)
    return render(request, 'saved.html', {'saved': saved,'count': saved.count })

def save_student(request, id):
    student = Student.objects.get(id=id)

    # avoid duplicates
    if not SavedRequest.objects.filter(user=request.user, student=student).exists():
        SavedRequest.objects.create(user=request.user, student=student)

    #SavedRequest.objects.create(
     #   user=request.user,
     #   student=student
    #)

    return redirect('saved_list')

def dashboard(request):
    sent = Request.objects.filter(sender=request.user)
    received = Request.objects.filter(receiver=request.user,status='Pending')

    return render(request, 'dashboard.html', {
        'sent': sent,
        'received': received,
        'sent_count': sent.count(),
        'received_count': received.count()
    })

def remove_saved(request, id):
    SavedRequest.objects.get(id=id).delete()
    return redirect('saved_list')

@require_POST
def accept_request(request, id):
    req = get_object_or_404(Request, id=id)
    if req.receiver == request.user and req.status == 'Pending':
        req.status = 'accepted'
        req.save()
    return redirect('dashboard')

@require_POST
def reject_request(request, id):
    req = get_object_or_404(Request, id=id)
    if req.receiver == request.user and req.status == 'Pending':
        req.status = 'rejected'
        req.save()
    return redirect('dashboard')

def students(request):
    students = Student.objects.all()

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()

    return render(request, 'students.html', {
        'students': students,
        'form': form,
        'count': students.count()
    })


# UPDATE
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit.html', {'form': form})


# DELETE
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('students')
