# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from django.contrib.messages import error

from .models import Course

def index(request):
    print "displaying index"
    context = {
        'courses' : Course.objects.all()
    }
    return render(request, "courses/index.html", context)

def create(request):
    print "creating"
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/')
    Course.objects.create(
        name = request.POST['name'],
        desc = request.POST['desc'],
    )
    return redirect('/')

def destroy(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect('/')

def delete(request, id):
    course = Course.objects.get(id = id)
    return render(request, 'courses/delete.html', {"course" : course})