from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, FormView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

def homepage(request):
    return render(request, template_name="homepage.html")

from polls.models import Poll, Questions, Answer
from polls.forms import NameForm, PollForm, QuestionForm, AnswerForm, QuestionModelForm, PollModelForm, AnswerModelForm

class UserNameContainsIMixin(UserPassesTestMixin):
    def test_func(self):
        return "i"in self.request.user.username

class UserNameUpperFirstMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.username[0].isupper()

class UserNameLenBigger5Mixin(UserPassesTestMixin):
    def test_func(self):
        return len(self.request.user.username[0]) <= 5

def hello(request, s0):
    s1 = request.GET.get("s1", "")
    return render(request, template_name='hello.html', context={'adjectives': [s0, s1, 'beautiful', 'wonderful']})

def animals(request):
    animals_str = request.GET.get("animals","")
    return render(request, template_name='my_template.html', context={'animals': animals_str.split(",")})

@login_required(login_url="/accounts/login/")
def polls(request):
    return render(request, template_name="polls.html", context={"polls": Poll.objects.all()})

def questions(request):
    return render(request, template_name="questions.html", context={"questions": Questions.objects.all()})

def answers(request):
    return render(request, template_name="answers.html", context={"answers": Answer.objects.all()})


def index_polls(request):
    return render(request, template_name="index_polls.html")

class PollView(View):

    def get(self, request):
        return render(request, template_name="polls.html", context={"polls": Poll.objects.all()})


class PollTemplateView(TemplateView):
    template_name = "polls.html"
    extra_context = {"polls": Poll.objects.all()}


class PollListView(PermissionRequiredMixin,UserNameContainsIMixin, ListView):
    permission_required = ['polls.view_poll', ]
    template_name = "polls.html"
    model = Poll


class AnswerView(View):

    def get(self, request):
        return render(request, template_name="answers.html", context={"answers": Answer.objects.all()})


class AnswerTemplateView(TemplateView):
    template_name = "answers.html"
    extra_context = {"answers": Answer.objects.all()}


class AnswerListView(PermissionRequiredMixin,UserNameUpperFirstMixin, ListView):
    permission_required = ['polls.view_answer', ]
    template_name = "answers.html"
    model = Answer


class QuestionView(View):

    def get(self, request):
        return render(request, template_name="questions.html", context={"questions": Questions.objects.all()})


class QuestionTemplateView(TemplateView):
    template_name = "questions.html"
    extra_context = {"questions": Questions.objects.all()}


class QuestionListView(PermissionRequiredMixin, UserNameLenBigger5Mixin, ListView):
    permission_required = ['polls.view_answer', ]
    template_name = "questions.html"
    model = Questions

def get_name(request):
    form = NameForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            return HttpResponse('IT WORKED')
    return render(request, template_name='form.html', context={'form': form})

def poll_form(request):
    form = PollForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        Poll.objects.create(name=name)
        return HttpResponse('IT WORKED')
    return render(request, template_name='form.html', context={'form': form})

def question_form(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        questions_text = form.cleaned_data["questions_text"]
        pub_date = form.cleaned_data["pub_date"]
        poll = form.cleaned_data["poll"]
        Questions.objects.create(questions_text=questions_text, pub_date=pub_date, poll=poll)
        return HttpResponse("IT WORKED!")
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )

def answer_form(request):
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        answer_text = form.cleaned_data["answer_text"]
        question = form.cleaned_data["question"]
        Answer.objects.create(answer_text=answer_text, question=question)
        return HttpResponse("IT WORKED!")
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )

class PollFormView(FormView):
    template_name = "form.html"
    form_class = PollModelForm
    success_url = reverse_lazy("polls:index")

    def form_valid(self,form):
        result = super().form_valid(form)
        name = form.cleaned_data['name']
        Poll.objects.create(name=name)
        return result

    def form_invalid(self, form):
        return super().form_invalid(form)

class QuestionFormView(FormView):
    template_name = "form.html"
    form_class = QuestionModelForm
    success_url = reverse_lazy("polls:index")

    def form_valid(self,form):
        result = super().form_valid(form)
        questions_text = form.cleaned_data["questions_text"]
        pub_date = form.cleaned_data["pub_date"]
        poll = form.cleaned_data["poll"]
        Questions.objects.create(questions_text=questions_text, pub_date=pub_date, poll=poll)
        return result

    def form_invalid(self, form):
        return super().form_invalid(form)


class AnswerFormView(FormView):
    template_name = "form.html"
    form_class = AnswerModelForm
    success_url = reverse_lazy("polls:index")

    def form_valid(self,form):
        result = super().form_valid(form)
        answer_text = form.cleaned_data["answer_text"]
        question = form.cleaned_data["question"]
        Answer.objects.create(answer_text=answer_text, question=question)
        return result

    def form_invalid(self, form):
        return super().form_invalid(form)


class PollFormMethodView(View):
    def get(self, request):
        form = PollForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )
    def post(self, request):
        form = PollForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            Poll.objects.create(name=name)
            return HttpResponseRedirect(reverse("polls:index"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )

class QuestionFormMethodView(View):
    def get(self, request):
        form = QuestionForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )
    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            questions_text = form.cleaned_data["questions_text"]
            pub_date = form.cleaned_data["pub_date"]
            poll = form.cleaned_data["poll"]
            Questions.objects.create(questions_text=questions_text, pub_date=pub_date, poll=poll)
            return HttpResponseRedirect(reverse("polls:index"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )


class AnswerFormMethodView(View):
    def get(self, request):
        form = AnswerForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )
    def post(self, request):
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer_text = form.cleaned_data["answer_text"]
            question = form.cleaned_data["question"]
            Answer.objects.create(answer_text=answer_text, question=question)
            return HttpResponseRedirect(reverse("polls:index"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )

class PollCreateView(PermissionRequiredMixin,CreateView):
    permission_required = ['polls.add_poll',]
    model = Poll
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("polls:index")


class QuestionCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['polls.add_question', ]
    model = Questions
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("polls:index")


class AnswerCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['polls.add_answer', ]
    model = Answer
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("polls:index")


class PollDetailView(View):
    def get(self, request, pk):
        obj = get_object_or_404(Poll, pk=pk)
        return render(
            request,
            template_name="poll.html",
            context={"poll": obj}
        )

class QuestionDetailView(View):
    def get(self, request, pk):
        obj = get_object_or_404(Questions, pk=pk)
        return render(
            request,
            template_name="question.html",
            context={"question": obj}
        )

class AnswerDetailView(View):
    def get(self, request, pk):
        obj = get_object_or_404(Answer, pk=pk)
        return render(
            request,
            template_name="answer.html",
            context={"answer": obj}
        )

class PollGenericDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['polls.view_poll', ]
    model = Poll
    template_name = "poll.html"

class QuestionGenericDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['polls.view_question', ]
    model = Questions
    template_name = "question.html"

class AnswerGenericDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['polls.view_answer', ]
    model = Answer
    template_name = "answer.html"

class PollUpdateView(View):

    def get(self,request, pk):
        form = PollForm()
        return render(request, template_name="form.html", context={"form":form})

    def post(self,request, pk):
        form = PollForm(request.POST or None)
        if form.is_valid():
            q = get_object_or_404(Poll, pk=pk)
            q.name = form.cleaned_data["name"]
            q.save()
            return HttpResponseRedirect(reverse("polls:index"))
        return render(request, template_name="form.html", context={"form": form})

class QuestionUpdateView(View):

    def get(self,request, pk):
        form = QuestionForm()
        return render(request, template_name="form.html", context={"form":form})

    def post(self,request, pk):
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            q = get_object_or_404(Questions, pk=pk)
            q.questions_text = form.cleaned_data["questions_text"]
            q.pub_date = form.cleaned_data["pub_date"]
            q.save()
            return HttpResponseRedirect(reverse("polls:index"))
        return render(request, template_name="form.html", context={"form": form})

class AnswerUpdateView(View):

    def get(self,request, pk):
        form = AnswerForm()
        return render(request, template_name="form.html", context={"form":form})

    def post(self,request, pk):
        form = AnswerForm(request.POST or None)
        if form.is_valid():
            q = get_object_or_404(Answer, pk=pk)
            q.answer_text = form.cleaned_data["answer_text"]
            q.date_added = form.cleaned_data["date_added"]
            q.save()
            return HttpResponseRedirect(reverse("polls:index"))
        return render(request, template_name="form.html", context={"form": form})

class PollGenericUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['polls.view_poll', 'polls.add_poll']
    model = Poll
    fields = ("name",)
    template_name = "form.html"
    success_url = reverse_lazy("polls:index")

class QuestionGenericUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['polls.view_question', 'polls.add_question']
    model = Questions
    fields = ("questions_text",)
    template_name = "form.html"
    success_url = reverse_lazy("polls:index")

class AnswerGenericUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['polls.view_answer', 'polls.add_answer']
    model = Answer
    fields = ("answer_text",)
    template_name = "form.html"
    success_url = reverse_lazy("polls:index")

class PollDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['polls.delete_poll', ]
    model = Poll
    template_name = "delete_form.html"
    success_url = reverse_lazy("polls:index")

class QuestionDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['polls.delete_question', ]
    model = Questions
    template_name = "delete_form.html"
    success_url = reverse_lazy("polls:index")

class AnswerDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['polls.delete_answer', ]
    model = Answer
    template_name = "delete_form.html"
    success_url = reverse_lazy("polls:index")

# REST API
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class QuestionListAPIView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

    def get(self, request):
        # serialized_response = serializers.serialize('json', Questions.objects.all())
        questions = list(Questions.objects.all().values('id', 'questions_text', 'poll'))
        return JsonResponse({'questions': questions})

    def post(self, request):
        body = request.POST
        questions_text = body.get('questions_text')
        poll_id = body.get('poll_id')
        if not questions_text:
            return JsonResponse({"error": "question_text field required"}, status=400)
        if not poll_id:
            return JsonResponse({"error": "poll_id field required"}, status=400)
        try:
            poll = Poll.objects.get(id=poll_id)
        except Poll.DoesNotExist:
            response_data = {
                "error": f"Object with pk {poll_id} does not exists!"
            }
            return JsonResponse(response_data, status=404)
        else:
            q = Questions.objects.create(questions_text=questions_text, poll=poll)
            status = 201
        return JsonResponse({"id": q.id}, status=status)

class QuestionsDetailAPIView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        try:
            question = Questions.objects.get(pk=pk)
        except Questions.DoesNotExist:
            response_data = {"error": f"Object with pk {pk} does not exists!"}
            return JsonResponse(response_data, status=404)
        else:
            response_data = {
                "id": question.id,
                "questions_text": question.questions_text,
                "poll": question.poll.id
            }
        return JsonResponse(response_data)

    def delete(self, request, pk):
        try:
            question = Questions.objects.get(pk=pk)
        except Questions.DoesNotExist:
            response_data = {"error": f"Object with pk {pk} does not exists!"}
            return JsonResponse(response_data, status=404)
        question.delete()
        return JsonResponse({})

    def put(self, request, pk):
        from django.http import QueryDict
        put_params = QueryDict(request.body)
        questions_text = put_params.get("questions_text")
        poll_id = put_params.get("poll_id")
        try:
            question = Questions.objects.get(pk=pk)
        except Questions.DoesNotExist:
            response_data = {"error": f"Object with pk {pk} does not exists!"}
            return JsonResponse(response_data, status=404)
        try:
            poll = Poll.objects.get(id=poll_id)
        except Poll.DoesNotExist:
            response_data = {
                "error": f"Object with pk {poll_id} does not exists!"
            }
            return JsonResponse(response_data, status=404)
        question.questions_text = questions_text
        question.poll = poll
        question.save()

        question.refresh_from_db()

        response_data = {
            "id": question.id,
            "questions_text": question.questions_text,
            "poll": question.poll.id
        }

        return JsonResponse(response_data)


class PollListAPIView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

    def get(self, request):
        polls = list(Poll.objects.all().values('id', 'name'))
        return JsonResponse({'polls': polls})

    def post(self, request):
        body = request.POST
        name = body.get("name")
        if not name:
            return JsonResponse({"error": "name field required"}, status=400)
        p = Poll.objects.create(name=name)
        return JsonResponse({"id": p.id}, status=201)


class PollsDetailAPIView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        try:
            poll = Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            response_data = {"error": f"Object with pk {pk} does not exists!"}
            return JsonResponse(response_data, status=404)
        else:
            response_data = {
                "id": poll.id,
                "name": poll.name
            }
        return JsonResponse(response_data)

    def delete(self, request, pk):
        try:
            poll = Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            response_data = {"error": f"Object with pk {pk} does not exists!"}
            return JsonResponse(response_data, status=404)
        poll.delete()
        return JsonResponse({})

    def put(self, request, pk):
        from django.http import QueryDict
        put_params = QueryDict(request.body)
        name = put_params.get("name")
        try:
            poll = Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            response_data = {"error": f"Object with pk {pk} does not exists!"}
            return JsonResponse(response_data, status=404)

        poll.name = name
        poll.save()

        poll.refresh_from_db()

        response_data = {
            "id": poll.id,
            "name": poll.name
        }

        return JsonResponse(response_data)


class AnswersListAPIView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

    def get(self, request):
        answers = list(Answer.objects.all().values('id', 'answer_text', 'question'))
        return JsonResponse({'answers': answers})

    def post(self, request):
        body = request.POST
        answer_text = body.get("answer_text")
        question_id = body.get('question_id')
        if not answer_text:
            return JsonResponse({"error": "answer_text field required"}, status=400)
        if not question_id:
            return JsonResponse({"error": "question_id field required"}, status=400)
        try:
            question = Questions.objects.get(id=question_id)
        except Questions.DoesNotExist:
            response_data = {
                "error": f"Object with pk {question_id} does not exists!"
            }
            return JsonResponse(response_data, status=404)
        else:
            a = Answer.objects.create(answer_text=answer_text, question=question)
            status = 201
        return JsonResponse({"id": a.id}, status=status)


class AnswersDetailAPIView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        try:
            answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            response_data = {"error": f"Object with pk {pk} does not exists!"}
            return JsonResponse(response_data, status=404)
        else:
            response_data = {
                "id": answer.id,
                "answer_text": answer.answer_text,
                "question": answer.question.questions_text,
            }
        return JsonResponse(response_data)

    def delete(self, request, pk):
        try:
            answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            response_data = {"error": f"Object with pk {pk} does not exists!"}
            return JsonResponse(response_data, status=404)
        answer.delete()
        return JsonResponse({})

    def put(self, request, pk):
        from django.http import QueryDict
        put_params = QueryDict(request.body)
        answer_text = put_params.get("answer_text")
        question_id = put_params.get("question_id")
        try:
            answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            response_data = {"error": f"Object with pk {pk} does not exists!"}
            return JsonResponse(response_data, status=404)
        try:
            question = Questions.objects.get(id=question_id)
        except Questions.DoesNotExist:
            response_data = {
                "error": f"Object with pk {question_id} does not exists!"
            }
            return JsonResponse(response_data, status=404)
        answer.answer_text = answer_text
        answer.question = question
        answer.save()

        answer.refresh_from_db()

        response_data = {
            "id": answer.id,
            "questions_text": answer.answer_text,
            "poll": answer.question.questions_text
        }

        return JsonResponse(response_data)