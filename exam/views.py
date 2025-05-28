from django.shortcuts import render
from .models import smexam

def smexam_list(request):
    exams = smexam.objects.filter(is_public=True)
    return render(request, 'exam/smexam_list.html', {
        'exams': exams,
        'student_name': 'Сергей Мовчан',
        'group': 'УКАИбд-321',
    })