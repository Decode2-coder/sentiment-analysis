from django.shortcuts import render
from .models import SentimentModel
from .forms import SentimentForm
from englishcode import predictType
from hindicode import predictHindi
from marathicode import predictMarathi

# Create your views here.
def SentimentApp(request):
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            sent = form.cleaned_data.get('Sentence')
            textAns = predictType(sent)
            return render(request, 'app.html', {'form': form, 'text': textAns, 'sentence': sent})
    else:
        form = SentimentForm()
    
    return render(request, 'app.html', {'form': form})


def hindi_page(request):
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            sent = form.cleaned_data.get('Sentence')
            textAns = predictHindi(sent)
            return render(request, 'hindi.html', {'form': form, 'text': textAns, 'sentence': sent})
    else:
        form = SentimentForm()
    
    return render(request, 'hindi.html', {'form': form})


def marathi_page(request):
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            sent = form.cleaned_data.get('Sentence')
            textAns = predictMarathi(sent)
            return render(request, 'marathi.html', {'form': form, 'text': textAns, 'sentence': sent})
    else:
        form = SentimentForm()
    
    return render(request, 'marathi.html', {'form': form})



