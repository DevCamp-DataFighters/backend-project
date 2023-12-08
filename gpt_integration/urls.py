# gpt_integration/urls.py
from django.urls import path
from .views import GPT3PromptView

urlpatterns = [
    path('gpt3/', GPT3PromptView.as_view(), name='gpt3-prompt'),
]
