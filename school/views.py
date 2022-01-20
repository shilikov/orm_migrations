from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students_qwery = Student.objects.all().\
        prefetch_related('teachers').order_by(ordering)
    context = {'object_list': students_qwery}

    return render(request, template, context)
