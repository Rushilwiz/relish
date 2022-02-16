from django.shortcuts import render
from .forms import ResponseForm

# Create your views here.
def index(request):
    success = False

    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = ResponseForm()

    context = {
        'form': form,
        'success': success,
    }

    return render(request, 'form/index.html', context)