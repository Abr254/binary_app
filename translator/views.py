from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        binary = ' '.join(format(ord(char), '08b') for char in text)
        return render(request, 'index.html', {'binary': binary, 'text': text})
    return render(request, 'index.html')
