# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['name']) < 6:
            errors['name'] = "Course name must be longer than 5 characters"
        if len(post_data['desc']) < 16:
            errors['desc'] = "Course description must be longer than 15 characters" 
        return errors

class Course(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()