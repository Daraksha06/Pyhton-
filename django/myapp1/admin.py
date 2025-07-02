from django.contrib import admin
from myapp1.models import *
# Register your models here.
admin.site.register(Student)

# now makemigrations and migrate after registering the model
