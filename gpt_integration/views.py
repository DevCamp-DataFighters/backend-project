# Create your views here.
from django.http import JsonResponse
from django.views import View
import openai


def formatTellStroy(message):
    return


class GptTellStory(View):
    def get(self, request, *args, **kwargs):
        prompt = "generate a story for my kid with its title"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[

                {"role": "user", "content": prompt},
            ],
        )
        try:
            generated_text = response['choices'][0]['message']

            return JsonResponse(generated_text)
        except Exception as e:
            return JsonResponse({"error": str(e)})


class GptQuiz(View):
    def get(self, request, *args, **kwargs):
        prompt = "generate a new quiz for my kid"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[

                {"role": "user", "content": prompt},
            ],
        )

        try:
            generated_text = response['choices'][0]['message']

            return JsonResponse(generated_text)
        except Exception as e:
            return JsonResponse({"error": str(e)})


class GptFillGaps(View):
    def get(self, request, *args, **kwargs):
        prompt = """generate a new filling gap excercice of 3 questions 
                and their options and their answers for my kid"""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[

                {"role": "user", "content": prompt},
            ],
        )

        try:
            generated_text = response['choices'][0]['message']

            return JsonResponse(generated_text)
        except Exception as e:
            return JsonResponse({"error": str(e)})


class GptGradeEssay(View):
    def post(self, request, *args, **kwargs):
        essay = request.POST.get('essay', '')
        prompt = "grade this essay writtent by my kid: "+essay
        if not essay:
            return JsonResponse({'error': 'Essay is required in the POST request'}, status=400)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[

                {"role": "user", "content": prompt},
            ],
        )

        try:
            generated_text = response['choices'][0]['message']

            return JsonResponse(generated_text)
        except Exception as e:
            return JsonResponse({"error": str(e)})
