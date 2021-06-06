from django.forms import CharField, Form, DateTimeField, ModelChoiceField, TextInput, ModelForm
from polls.models import Poll, Questions,Answer
from django.core.exceptions import ValidationError
from datetime import datetime
import pytz




class PastDateField(DateTimeField):

    def validate(self, value):
        utc = pytz.utc
        super().validate(value)
        if value >= datetime.today().replace(tzinfo=utc):
            raise ValidationError('Only past dates allowed here.')


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class NameForm(Form):
    name = CharField(max_length=128)
    birth_date = DateTimeField()


class PollForm(Form):
    name = CharField(max_length=128)

    def clean_name(self):
        initial = self.cleaned_data["name"]
        return initial.upper()

class PollModelForm(ModelForm):

    class Meta:
        model = Poll
        fields = "__all__"

class QuestionForm(Form):
    questions_text = CharField(max_length=128, validators=[capitalized_validator])
    pub_date = PastDateField(label='Publication Date',widget=TextInput(attrs={'placeholder': 'eg.2006-10-25 14:30:59'}))
    poll = ModelChoiceField(queryset=Poll.objects.all())

    def clean_question_text(self):
        initial = self.cleaned_data["questions_text"]
        return initial.replace(" ", "*")

    def clean(self):
        utc = pytz.utc
        result = super().clean()
        if result["questions_text"][0] == "A" and result["pub_date"].year < 2000:
            self.add_error("questions_text", "Can't start with an A")
            self.add_error("pub_date", "Can't be before 2000")
            raise ValidationError("Don't put question text that starts with an A and a year before 2000")
        if result["questions_text"][0] == "W" and result["pub_date"] <= datetime.today().replace(tzinfo=utc):
            self.add_error("questions_text", "Can't start with an W")
            self.add_error("pub_date", "Date must be from the future")
            raise ValidationError("Don't put question text that starts with a W and a date from the past")
        return result


class QuestionModelForm(ModelForm):

    class Meta:
        model = Questions
        fields = "__all__"

class AnswerForm(Form):
    answer_text = CharField(max_length=128)
    question = ModelChoiceField(queryset=Questions.objects.all())
    date_added = PastDateField(label="Add date")

    def clean(self):
        result = super().clean()
        if result['answer_text'].isupper():
            raise ValidationError("Question name cant be uppercase")
        return result

class AnswerModelForm(ModelForm):

    class Meta:
        model = Answer
        fields = "__all__"
