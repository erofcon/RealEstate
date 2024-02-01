from django.http import JsonResponse

from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return JsonResponse('Success', status=200, safe=False)
        else:
            return JsonResponse('Something went wrong', status=400, safe=False)
    else:
        return JsonResponse('Method not allowed', status=405, safe=False)
