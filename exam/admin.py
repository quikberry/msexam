from django.contrib import admin
from .models import smexam

@admin.register(smexam)
class SMExamAdmin(admin.ModelAdmin):
    list_display = ("title", "exam_date", "created_at", "is_public")
    list_filter = ("is_public", "created_at", "exam_date")
    search_fields = ("title", "students__email")
    filter_horizontal = ("students",)