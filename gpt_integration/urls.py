# gpt_integration/urls.py
from django.urls import path
from .views import GptFillGaps, GptTellStory, GptQuiz, GptGradeEssay

urlpatterns = [
    path('tell_story/', GptTellStory.as_view(), name='gpt-tell-story'),
    path('quiz/', GptQuiz.as_view(), name='gpt-quiz'),
    path('grade_essay/', GptGradeEssay.as_view(), name='gpt-grade-essay'),
    path('fill_gaps/', GptFillGaps.as_view(), name='gpt-fill-gaps'),
]
