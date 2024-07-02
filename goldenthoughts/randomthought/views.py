from django.shortcuts import render
import random

# Create your views here.
def thought(request):
     return render(
         request,
         'thought.html', context={"thought":random.choice(THOUGHT_LIST)}
     )

THOUGHT_LIST = [
   "Nasze życie jest takim, jakim uczyniły je nasze myśli.",
   "Sztuka trwa długo, życie krótko.",
   "Przeszłość organizuje się wciąż na nowo wraz z teraźniejszością."
]