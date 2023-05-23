from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from main.models import *
from .forms import *

def login_required_decorator(f):
    return login_required(f, login_url="login")

@login_required_decorator
def dashboard(request):
    return render(request, 'dashboard/index.html')


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('login')






@login_required_decorator
def category_list(request):
    categories = Category.objects.all()
    ctx = {
        'categories':categories,
        "c_active": 'active'
    }
    return render(request,'dashboard/categories/list.html',ctx)


@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/categories/form.html', ctx)


@login_required_decorator
def category_edit(request, pk):
    model = Category.objects.get(id=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/categories/form.html', ctx)


@login_required_decorator
def category_delete(request, pk):
    model = Category.objects.get(id=pk)
    model.delete()
    return redirect('category_list')




@login_required_decorator
def courses_list(request):
    courses = Courses.objects.all()
    ctx = {
        'courses':courses,
        "x_active": 'active'
    }
    return render(request,'dashboard/kurs/list.html',ctx)


@login_required_decorator
def courses_create(request):
    model = Courses()
    form = CoursesForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('courses_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/kurs/form.html', ctx)


@login_required_decorator
def courses_edit(request, pk):
    model = Courses.objects.get(id=pk)
    form = CoursesForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('courses_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/kurs/form.html', ctx)


@login_required_decorator
def courses_delete(request, pk):
    model = Courses.objects.get(id=pk)
    model.delete()
    return redirect('courses_delete')






@login_required_decorator
def teacher_list(request):
    teacher = Teacher.objects.all()
    ctx = {
        'teacher':teacher,
        "z_active": 'active'
    }
    return render(request,'dashboard/teacher/list.html',ctx)


@login_required_decorator
def teacher_create(request):
    model = Teacher()
    form = TeacherForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/teacher/form.html', ctx)


@login_required_decorator
def teacher_edit(request, pk):
    model = Teacher.objects.get(id=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/teacher/form.html', ctx)


@login_required_decorator
def teacher_delete(request, pk):
    model = Teacher.objects.get(id=pk)
    model.delete()
    return redirect('teacher_delete')





@login_required_decorator
def grup_list(request):
    grup_e = Grup.objects.all()
    categories = Courses.objects.all()
    month = Month.objects.all()
    s = 0
    for i in grup_e.values_list("price"):
        a = list(i)
        b = sum(a)
        s += b
        # s += a
    print( s)

    ctx = {
        "s":s,
        'grup_e':grup_e,
        "categories": categories,
        "q_active": 'active',
        "month": month
    }
    return render(request,'dashboard/grung/list.html',ctx)


@login_required_decorator
def grup_create(request):
    model = Grup()
    form = GrupForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('grup_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/grung/form.html', ctx)


@login_required_decorator
def grup_edit(request, pk):
    model = Grup.objects.get(id=pk)
    form = GrupForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('grup_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/grung/form.html', ctx)


@login_required_decorator
def grup_delete(request, pk):
    model = Grup.objects.get(id=pk)
    model.delete()
    return redirect('grup_delete')


def grup_info(request, id):
    grup = Grup.objects.filter(courses_id=id)
    categories = Courses.objects.all()
    month = Month.objects.all()
    s = 0
    for i in grup.values_list("price"):
        a = list(i)
        b = sum(a)
        s += b
    print(s)
    v = s * 30 // 100
    print(v)

    cxt = {
        "v": v,
        "s": s,
        "grup": grup,
        "categories": categories,
        "month": month
    }
    # print(grup_info)

    return render(request, "dashboard/grung/list_gp.html", cxt)




@login_required_decorator
def users_list(request):
    users = Users.objects.all()
    courses = Courses.objects.all()
    ctx = {
        'users': users,
        "n_active": 'active',
        "courses": courses
    }
    for i in users.values():
        a = i["now"]
        if a == 1:
            print("School")
        elif a == 2:
            print("the work")
        elif a == 3:
            print("student")
        # print(a)
    # print(Users.now())
    return render(request,'dashboard/users/list.html',ctx)


@login_required_decorator
def users_create(request):
    model = Users()
    form = UsersForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('users_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/users/form.html', ctx)


@login_required_decorator
def users_edit(request, pk):
    model = Users.objects.get(id=pk)
    form = UsersForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('users_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/users/form.html', ctx)


@login_required_decorator
def users_delete(request, pk):
    model = Users.objects.get(id=pk)
    model.delete()
    return redirect('users_delete')


def user_info(request, id):
    users = Users.objects.filter(courses_id=id)
    courses = Courses.objects.all()
    # for i in grup.values():
    #     print(i)
    # s = 0
    # for i in grup.values_list("price"):
    #     a = list(i)
    #     b = sum(a)
    #     s += b
    #     # s += a
    # print(s)
    # v = s * 30 // 100
    # print(v)

    cxt = {
        # "v": v,
        # "s": s,
        "users": users,
        "courses": courses
    }
    # print(grup_info)

    return render(request, "dashboard/users/list_user.html", cxt)



def users_per(request):
    month = Month.objects.all()

    for i in month.values():
        print(i)
        # print(i.oy)
    ctx = {
        # "i": i,
        'month': month,
        "x_active": 'active'
    }
    return render(request, "dashboard/grung/list_per.html", ctx)


def grup_mouht(request, id):
    day = Day.objects.filter(month_id=id)
    month = Month.objects.all()

    for i in day.values():
        d = i["day"]
        son = int(d)
        if son <= 7:
            print(son)
            # j = tuple(son)
            # return render(request, "dashboard/grung/list_per.html", son)
        # a = list((i))
        # b = int(a)
        # if b >= [7]:
        #     print(type(a), a)
    ctx = {
        "day": day,
        "month": month
    }
    return render(request, "dashboard/grung/list_per.html", ctx)



@login_required_decorator
def month_list(request):
    month = Month.objects.all()
    ctx = {
        'month':month,
        "x_active": 'active'
    }
    return render(request,'dashboard/manth/list.html',ctx)


@login_required_decorator
def month_create(request):
    model = Month()
    form = MonthForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('month_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/manth/form.html', ctx)


@login_required_decorator
def month_edit(request, pk):
    model = Month.objects.get(id=pk)
    form = MonthForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('month_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/manth/form.html', ctx)


@login_required_decorator
def month_delete(request, pk):
    model = Month.objects.get(id=pk)
    model.delete()
    return redirect('month_delete')

