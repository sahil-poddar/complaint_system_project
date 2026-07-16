from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'complaint_type', 'status', 'created_at')
    list_filter = ('status', 'complaint_type')
    search_fields = ('name', 'email', 'subject')