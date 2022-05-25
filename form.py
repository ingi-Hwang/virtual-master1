from django import forms
from community.models import *


class QuestionForm(forms.ModelForm):
    class Meta:
        model = User  # 사용할 모델
        fields = ['name', 'age', 'gender']  # QuestionForm에서 사용할 Question 모델의 속성

class InputForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = ['user_id', 'tag', 'startperiod', 'endperiod', 'area']