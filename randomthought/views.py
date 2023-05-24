from django.shortcuts import render, redirect
import random

# Create your views here.
def thought(request):
     return render(
         request,
         'randomthought/thought.html', context={"thought":random.choice(THOUGHT_LIST)}
     )

THOUGHT_LIST = [
   "Nasze życie jest takim, jakim uczyniły je nasze myśli.",
   "Sztuka trwa długo, życie krótko.",
   "Przeszłość organizuje się wciąż na nowo wraz z teraźniejszością."
]

def create_sentence_view(request):
    if request.method == "GET":
        return render(
            request,
            'randomthought/sentence_form.html',
        )

    if request.method == "POST":
        thought = request.POST.get('thought')
        if thought:
            THOUGHT_LIST.append(thought)

        return redirect("randomthought:list_sentence_view")

def list_sentence_view(request):
    return render(
        request,
        'randomthought/sentence_list.html',
        context={
            'thought': THOUGHT_LIST,
        }
    )