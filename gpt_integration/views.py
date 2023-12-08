# Create your views here.
from django.http import JsonResponse
from django.views import View
import openai


class GptTellStory(View):
    def get(self, request, *args, **kwargs):
        prompt = "make me a filling gap exercice"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[

                {"role": "user", "content": prompt},
            ],
        )

        generated_text = response['choices'][0]['message']

        return JsonResponse({'generated_text': generated_text})


class GptQuiz(View):
    def get(self, request, *args, **kwargs):
        prompt = "make me a filling gap exercice"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[

                {"role": "user", "content": prompt},
            ],
        )

        generated_text = response['choices'][0]['message']

        return JsonResponse({'generated_text': generated_text})


class GptFillGaps(View):
    def get(self, request, *args, **kwargs):
        prompt = "make me a filling gap exercice"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[

                {"role": "user", "content": prompt},
            ],
        )

        generated_text = response['choices'][0]['message']

        return JsonResponse({'generated_text': generated_text})


class GptGradeEssay(View):
    def get(self, request, *args, **kwargs):
        prompt = request.POST.get('prompt', '')
        if not prompt:
            return JsonResponse({'error': 'Prompt is required in the POST request'}, status=400)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[

                {"role": "user", "content": prompt},
            ],
        )

        generated_text = response['choices'][0]['message']

        return JsonResponse({'generated_text': generated_text})
