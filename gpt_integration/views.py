
# Create your views here.
from django.http import JsonResponse
from django.views import View
import openai


class GPT3PromptView(View):
    def get(self, request, *args, **kwargs):
        # prompt = request.POST.get('prompt', '')
        prompt = "who is Lala Fatma nsoumer"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",  # Use the appropriate GPT-3 fine tuned model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )

        generated_text = response['choices'][0]['message']

        return JsonResponse({'generated_text': generated_text})
