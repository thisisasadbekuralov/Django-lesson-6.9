from django.shortcuts import render
import os



filename = 'themes.txt'
def index(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'themes.txt')
    with open(file_path, 'r') as data_file:
        data = data_file.readlines()

    context = {'themes': data}
    return render(request, 'themes.html', context)

