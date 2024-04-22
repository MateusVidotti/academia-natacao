from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime


from student_management_app.models import CustomUser, Courses


def admin_home(request):
    return render(request, 'hod_templates/home_content.html')


def add_staff(request):
    return render(request, 'hod_templates/add_staff_template.html')


def add_course(request):
    return render(request, 'hod_templates/add_course_template.html')


def add_student(request):
    courses = Courses.objects.all()
    return render(request, 'hod_templates/add_student_template.html', {'courses': courses})


def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        try:
            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                  email=email, password=password, user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request, 'Funcionário Adicionado com Sucesso')
            return HttpResponseRedirect('/add_staff')
        except:
            messages.error(request, 'Falha em Adicionar')
            return HttpResponseRedirect(request, '/add_staff')


def add_course_save(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed')
    else:
        course = request.POST.get('course')
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, 'Curso Adicionado com Suacesso')
            return HttpResponseRedirect('/add_course')
        except:
            messages.error(request, 'Falha em Adicionar')
            return HttpResponseRedirect('/add_course')


def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        course = request.POST.get('course')
        gender = request.POST.get('gender')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')

        try:
            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                  email=email, password=password, user_type=3)
            user.students.address = address
            course_obj = Courses.objects.get(id=course)
            user.students.course_id = course_obj
            user.students.session_start_year = session_start
            user.students.session_end_year = session_end
            user.students.gender = gender
            user.students.profile_pic = ''

            user.save()
            messages.success(request, 'Estudante Adicionado com sucesso')
            return HttpResponseRedirect('/add_student')
        except:
            messages.error(request, 'Falha em Adicionar')
            return HttpResponseRedirect(request, '/add_student')



