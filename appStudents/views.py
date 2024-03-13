from django.shortcuts import render



def students(request):
    students_list = [
        {"id": 1, "name": "John", "score": 23},
        {"id": 2, "name": "Smith", "score": 40},
        {"id": 3, "name": "Alice", "score": 54},
        {"id": 4, "name": "Jack", "score": 33},
    ]
    context = {"students_list": students_list}
    return render(request, "students.html", context)