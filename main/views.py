from django.shortcuts import render
from main.models import Category, Courses, New,Teacher, Grup


def index(request):
    course = Courses.objects.order_by("id")[:3]
    techer = Teacher.objects.all()
    new =   New.objects.order_by("-id")[:6]
    ctx = {
        "course": course,
        "techer": techer,
        "new": new
    }

    return render(request, "main/index1.html", ctx)

def course_our(request):
    categoriya = Category.objects.all()
    course = Courses.objects.order_by("id")[:3]

    ctx = {
        "categoriya": categoriya,
        "course": course
    }

    return render(request, "main/our-courses.html", ctx)



def course_detail(request, id):
    course_detail = Courses.objects.get(id=id)
    course = Courses.objects.order_by("id")[:3]
    tech = Teacher.objects.all()
    grung = Courses.objects.all()


    ctx = {
        "course_detail": course_detail,
        "tech": tech,
        "course": course,
        "grung": grung
    }

    return render(request, "main/course-detail.html", ctx)

def new_blog(request, id):
    pass
    # new_blo = New.objects.get(id=id)
    # ctx = {
    #     "new_blo": new_blo
    # }
    # return render(request, "main/blog-large.html", ctx)


def new(request):
    new_blog = New.objects.all()
    course = Courses.objects.order_by("id")[:5]
    ctx = {
        "new_blog": new_blog,
        "course": course
    }

    return render(request, "main/blog-large.html", ctx)

# def course(request, id):
#     course_detaols = Courses.objects.get(id=id)
#     course = Courses.objects.all()
#     category = Category.objects.all()
#     new = New.objects.order_by("-id")[:4]
#     ctx = {
#         'course_detaols': course_detaols,
#         'course': course,
#         'category': category,
#         'new': new
#     }
#     return render(request, "main/course_details.html", ctx)
#
# def course_01(request):
#     course = Courses.objects.all()
#     ctx = {
#         'course': course
#     }
#     return render(request, "main/course_01.html", ctx)
#
# def grid_news(request):
#     new = New.objects.order_by("-id")
#     ctx = {
#         'new': new,
#     }
#     return render(request, "main/grid_news.html", ctx)
#
#
# def news_details(request, id):
#     category = Category.objects.filter()
#     news_details = New.objects.get(id=id)
#     course = Courses.objects.all()
#     ctx = {
#         'news_details': news_details,
#         'category': category,
#         "course": course
#     }
#     return render(request, "main/news_details.html", ctx)
#
#
# def about(request):
#     team = Team.objects.all()
#     ctx = {
#         'team': team
#     }
#     return render(request, "main/about_us.html", ctx)
#
#
# def contact(request):
#     return render(request, 'main/contact_us.html')


