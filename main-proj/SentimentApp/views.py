from django.shortcuts import render
from .models import SentimentModel
from .forms import SentimentForm
from englishcode import predictType
from hindicode import predictHindi
from marathicode import predictMarathi

# Create your views here.
def SentimentApp(request):
    form = SentimentForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            sent = form.cleaned_data.get('Sentence')    # got the sentence
            textAns = predictType(sent)
            context['text'] = textAns
        else:
            form = SentimentForm()
    
    context['form'] = form
    return render(request, 'app.html', context=context)

def hindi_page(request):
    form = SentimentForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            sent = form.cleaned_data.get('Sentence')    # got the sentence
            textAns = predictHindi(sent)
            context['text'] = textAns
        else:
            form = SentimentForm()
    
    context['form'] = form
    return render(request, 'hindi.html', context=context)


def marathi_page(request):
    form = SentimentForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            sent = form.cleaned_data.get('Sentence')    # got the sentence
            textAns = predictMarathi(sent)
            context['text'] = textAns
        else:
            form = SentimentForm()
    
    context['form'] = form
    return render(request, 'marathi.html', context=context)


