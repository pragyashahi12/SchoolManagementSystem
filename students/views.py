from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
from django.http import HttpResponse

from django.core.mail import send_mail, BadHeaderError


def home(request):
    search = request.GET.get('search')

    if search:

        students = Student.objects.filter(name__icontains=search)

    else:

        students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'home.html', context)


def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")

        Student.objects.create(
            name=name,
            age=age,
            email=email
        )


        messages.success(request, "Student added successfully.")

        return redirect("home")

    return render(request, "add_student.html")


def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.email = request.POST.get("email")

        student.save()
        messages.success(request, "Student updated successfully.")

        return redirect("home")

    return render(request, "edit_student.html", {"student": student})


def delete_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect("home")

    return render(request, "delete_student.html", {"student": student})
def email_form(request):
    return render(request,"send-mail.html")
def sendEmail(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        recipient = [request.POST.get("to")]

        try:
            send_mail(
                subject,
                message,
                None,   # Uses DEFAULT_FROM_EMAIL
                recipient,
                fail_silently=False,
            )
            return HttpResponse("Email Sent Successfully!")

        except Exception as e:
            traceback.print_exc()
            return HttpResponse(f"Error: {e}", status=500)

    return HttpResponse("Invalid Request Method")