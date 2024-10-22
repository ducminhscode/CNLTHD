from django.contrib import admin
from django.utils.safestring import mark_safe

from courses.models import Category, Course, Lesson
# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'active', 'created_data']
    search_fields = ['subject', 'content']
    list_filter = ['id','subject','created_data']
    list_per_page = 1
    list_editable = ['subject']
    readonly_fields = ['avatar']

    def avatar(self, lesson):
        return mark_safe(f"<img src ='/static/{lesson.image.name}' width='200' />")


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
