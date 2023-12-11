from django.contrib import admin

# Register your models here.
# myapp/admin.py


from .models import addList
from .models import Student

@admin.register(addList)
class AddListAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_name', 'roll')
    # Add other configurations or customizations if needed




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'roll_number', 'email', 'phone_number', 'date_of_birth', 'major', 'graduation_year', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'roll_number', 'email')
    list_filter = ('major', 'graduation_year', 'created_at', 'updated_at')

    fieldsets = (
        ('Basic Information', {'fields': ('first_name', 'last_name', 'roll_number')}),
        ('Contact Information', {'fields': ('email', 'phone_number')}),
        ('Academic Details', {'fields': ('date_of_birth', 'major', 'graduation_year')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )

