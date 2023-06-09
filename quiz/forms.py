from django.forms import ModelForm
from .models import QuestionsModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username','password'}

class addQuestionForm(ModelForm):
    class Meta:
        model = QuestionsModel
        fields = "__all__"

