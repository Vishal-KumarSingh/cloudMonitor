from django.contrib import admin
from . import models
# Register your models here.
class BookMarksAuth(admin.ModelAdmin):
    pass

admin.site.register(models.BookMarks , BookMarksAuth)