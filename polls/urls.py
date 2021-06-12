from django.urls import path

from polls.views import hello, animals, polls, questions, answers, index_polls, PollView, PollTemplateView, PollListView
from polls.views import AnswerView, AnswerTemplateView, AnswerListView
from polls.views import QuestionView, QuestionTemplateView, QuestionListView
from polls.views import get_name, poll_form, question_form, answer_form, QuestionFormView, PollFormView, AnswerFormView
from polls.views import PollFormMethodView, QuestionFormMethodView, AnswerFormMethodView
from polls.views import QuestionCreateView, PollCreateView, AnswerCreateView
from polls.views import QuestionDetailView, PollDetailView, AnswerDetailView
from polls.views import QuestionGenericDetailView, PollGenericDetailView, AnswerGenericDetailView
from polls.views import QuestionUpdateView, PollUpdateView, AnswerUpdateView
from polls.views import QuestionGenericUpdateView, PollGenericUpdateView, AnswerGenericUpdateView
from polls.views import QuestionDeleteView, PollDeleteView, AnswerDeleteView
from polls.views import QuestionListAPIView, QuestionsDetailAPIView, PollListAPIView, PollsDetailAPIView
from polls.views import AnswersListAPIView, AnswersDetailAPIView

app_name = "polls"

urlpatterns = [
    path('', index_polls, name='index'),



    path('hello/<str:s0>/', hello),
    path('animals/', animals),

    path('polls1/', polls, name='polls'),
    path('questions1/', questions, name='questions'),
    path('answers1/', answers, name='answers'),

    path('polls-class/', PollView.as_view(), name='polls-class'),
    path('polls-template/', PollTemplateView.as_view(), name='polls-template'),
    path('polls-list/', PollListView.as_view(), name='polls-list'),

    path('answers-class/', AnswerView.as_view(), name='answers-class'),
    path('answers-template/', AnswerTemplateView.as_view(), name='answers-template'),
    path('answers-list/', AnswerListView.as_view(), name='answers-list'),

    path('questions-class/', QuestionView.as_view(), name='questions-class'),
    path('questions-template/', QuestionTemplateView.as_view(), name='questions-template'),
    path('questions-list/', QuestionListView.as_view(), name='questions-list'),

    path('my-name-form/', get_name),
    path('my-poll-form/', poll_form),
    path('my-question-form/', question_form),
    path('my-answer-form/', answer_form),

    path('my-poll-form-view/', PollFormView.as_view(), name='poll-view'),
    path('my-question-form-view/', QuestionFormView.as_view(), name='questions-view'),
    path('my-answer-form-view/', AnswerFormView.as_view(), name='answer-view'),

    path('my-poll-form-method-view/', PollFormMethodView.as_view(), name = 'my-poll-form-method-view'),
    path('my-question-form-method-view/', QuestionFormMethodView.as_view(), name = 'my-question-form-method-view'),
    path('my-answer-form-method-view/', AnswerFormMethodView.as_view(), name = 'my-answer-form-method-view'),

    path('poll-create-view/', PollCreateView.as_view(), name = 'poll-create-view'),
    path('question-create-view/', QuestionCreateView.as_view(), name = 'question-create-view'),
    path('answer-create-view/', AnswerCreateView.as_view(), name = 'answer-create-view'),

    path('poll-detail-view/<pk>/', PollDetailView.as_view(), name = 'poll-detail-view'),
    path('question-detail-view/<pk>/', QuestionDetailView.as_view(), name = 'question-detail-view'),
    path('answer-detail-view/<pk>/', AnswerDetailView.as_view(), name = 'answer-detail-view'),

    path('poll-generic-detail-view/<pk>/', PollGenericDetailView.as_view(), name = 'poll-generic-detail-view'),
    path('question-generic-detail-view/<pk>/', QuestionGenericDetailView.as_view(), name = 'question-generic-detail-view'),
    path('answer-generic-detail-view/<pk>/', AnswerGenericDetailView.as_view(), name = 'answer-generic-detail-view'),

    path('poll-update-view/<pk>/', PollUpdateView.as_view(), name = 'poll-update-view'),
    path('question-update-view/<pk>/', QuestionUpdateView.as_view(), name = 'question-update-view'),
    path('answer-update-view/<pk>/', AnswerUpdateView.as_view(), name = 'answer-update-view'),

    path('poll-generic-update-view/<pk>/', PollGenericUpdateView.as_view(), name = 'poll-generic-update-view'),
    path('question-generic-update-view/<pk>/', QuestionGenericUpdateView.as_view(), name = 'question-generic-update-view'),
    path('answer-generic-update-view/<pk>/', AnswerGenericUpdateView.as_view(), name = 'answer-generic-update-view'),

    path('poll-delete-view/<pk>/', PollDeleteView.as_view(), name = 'poll-delete-view'),
    path('question-delete-view/<pk>/', QuestionDeleteView.as_view(), name = 'question-delete-view'),
    path('answer-delete-view/<pk>/', AnswerDeleteView.as_view(), name = 'answer-delete-view'),

    path('questions/', QuestionListAPIView.as_view(), name='questions-list'),
    path('questions/<pk>/', QuestionsDetailAPIView.as_view(), name='questions-detail'),

    path('polls/', PollListAPIView.as_view(), name='polls-list'),
    path('polls/<pk>/', PollsDetailAPIView.as_view(), name='polls-detail'),

    path('answers/', AnswersListAPIView.as_view(), name='answers-list'),
    path('answers/<pk>/', AnswersDetailAPIView.as_view(), name='answers-detail'),
]