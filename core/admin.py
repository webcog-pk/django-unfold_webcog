from django.contrib import admin
from core.models import (
    Comment,
)
from unfold.admin import ModelAdmin as UnfoldModelAdmin

@admin.register(Comment)
class CommentAdmin(UnfoldModelAdmin):
    list_display=('id', 'message')


# Register your models here.
