from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Courses(models.Model):
    category = models.ForeignKey(Category,  null=True, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')
    name = models.TextField()
    text = models.TextField()
    price = models.BigIntegerField()

    def __str__(self):
        return self.name



class Teacher(models.Model):
    photo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.name


class Month(models.Model):
    oy = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.oy

class Day(models.Model):
    month = models.ForeignKey(Month, on_delete=models.RESTRICT, null=True, default=None, blank=True)
    day = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.day

class Grup(models.Model):
    courses = models.ForeignKey(Courses, null=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, null=True, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, null=True, on_delete=models.CASCADE),
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    number = models.CharField(max_length=20)
    price = models.BigIntegerField()
    created_date = models.DateTimeField(default=now, editable=False)


    def __str__(self):
        return self.name


class Pyment(models.Model):
    grup = models.ForeignKey(Grup, null=True, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    payment = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    created_date = models.DateTimeField(default=now, editable=False)


    def __str__(self):
        return self.name


class Users(models.Model):
    SCHOOL = 1
    THE_WORK = 2
    STUDENT = 3

    BREAND = 1
    TELEGRAM = 2
    INSTAGRAM = 3
    FRIEND = 4

    YOZILDI = 1
    KUTMOQDA = 2
    GURUH_OCHILDI = 3
    UQIYDI = 4


    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now, editable=False)
    name = models.CharField(max_length=250)
    age = models.CharField(max_length=250)
    number =  models.CharField(max_length=250)
    dad_number = models.CharField(max_length=250)
    advertising = models.SmallIntegerField(choices=(
        (BREAND, "Breand"),
        (TELEGRAM, "Telegram"),
        (INSTAGRAM, "Instagram"),
        (FRIEND, "Friend")
    ))
    now = models.SmallIntegerField(choices=(
        (SCHOOL, "School"),
        (THE_WORK, "the work"),
        (STUDENT, "student"),
    ))

    edu = models.SmallIntegerField(choices=(
        (YOZILDI, "Yozildi"),
        (KUTMOQDA, "Kutmoqda"),
        (GURUH_OCHILDI, "Guruh_ochildi"),
        (UQIYDI, "Uqiydi"),
    ))



class New(models.Model):
    photo = models.ImageField(upload_to='images/')
    name = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.name

class History(models.Model):
    users = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    grup = models.ForeignKey(Grup, null=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    text = models.TextField()




class Nimadir(models.Model):
    text = models.TextField()