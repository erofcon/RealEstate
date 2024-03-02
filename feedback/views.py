from django.http import JsonResponse

from telegram_bot.main_bot import send_message
from .forms import FeedbackForm


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            message = f"""
            Получено новое сообщение!\nимя: {form.data['name']}\nконтакты: {form.data['contacts']}\nсообщение: {form.data['subject']}
            """

            send_message(message)
            return JsonResponse('Success', status=200, safe=False)
        else:
            return JsonResponse('Something went wrong', status=400, safe=False)
    else:
        return JsonResponse('Method not allowed', status=405, safe=False)
