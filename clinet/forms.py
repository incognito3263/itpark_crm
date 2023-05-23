from django import forms
from main.models import Category, Courses, Teacher, New, Users, Grup, Pyment, History, Month

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category()
        fields = '__all__'

class CoursesForm(forms.ModelForm):
	class Meta:
		model = Courses()
		fields = "__all__"



class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher()
		fields = "__all__"


class UsersForm(forms.ModelForm):
	class Meta:
		model = Users()
		fields = "__all__"

class GrupForm(forms.ModelForm):
	class Meta:
		model = Grup()
		fields = "__all__"


class NewForm(forms.ModelForm):
	class Meta:
		model = New()
		fields = "__all__"


class PymentForm(forms.ModelForm):
	class Meta:
		model = Pyment()
		fields = "__all__"


class HistoryForm(forms.ModelForm):
	class Meta:
		model = History()
		fields = "__all__"

class MonthForm(forms.ModelForm):
	class Meta:
		model = Month()
		fields = "__all__"

