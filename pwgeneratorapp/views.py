from django.shortcuts import render
import random

# Create your views here.


def PWGenView(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.POST.get('passLength'))
    if request.POST.get('upperCheck'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.POST.get('specialCheck'):
        characters.extend(list('!@#$%^&*()'))
    if request.POST.get('numCheck'):
        characters.extend(list('012345679'))

    length = int(length)
    password = ''
    for i in range(length):
        password += random.choice(characters)

    context = {
        'password': password
    }
    return render(request, 'index.html', context)
