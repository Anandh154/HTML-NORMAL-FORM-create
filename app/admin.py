from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Topic)
admin.site.register(Form)
admin.site.register(Webpage)
admin.site.register(AccessRecord)