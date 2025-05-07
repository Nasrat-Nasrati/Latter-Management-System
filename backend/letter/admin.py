from django.contrib import admin
from .models import Department, Letter, LetterTracking

# ✅ Department Admin
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')
    search_fields = ('name', )
    list_filter = ('parent', )
    ordering = ('name', )
    list_per_page = 25


# ✅ Letter Admin
@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'letter_type', 'sender_department', 'receiver_department', 'create_date', 'sender_date', 'receiver_date')
    search_fields = ('subject', 'number_sadira', 'number_warida', 'sender_department__name', 'receiver_department__name')
    list_filter = ('letter_type', 'sender_department', 'receiver_department', 'create_date')
    date_hierarchy = 'create_date'
    ordering = ('-create_date', )
    list_select_related = ('sender_department', 'receiver_department')
    list_per_page = 25
    readonly_fields = ('create_date', )
    raw_id_fields = ('sender_department', 'receiver_department')


# ✅ LetterTracking Admin
@admin.register(LetterTracking)
class LetterTrackingAdmin(admin.ModelAdmin):
    list_display = ('id', 'letter', 'status', 'sender_department', 'receiver_department', 'sent_date', 'received_date')
    search_fields = ('letter__subject', 'sender_department__name', 'receiver_department__name')
    list_filter = ('status', 'sender_department', 'receiver_department', 'sent_date')
    date_hierarchy = 'sent_date'
    ordering = ('-sent_date', )
    list_select_related = ('letter', 'sender_department', 'receiver_department')
    list_per_page = 25
    raw_id_fields = ('letter', 'sender_department', 'receiver_department')
