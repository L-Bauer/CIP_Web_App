from django.contrib import admin
from .models import Associate, Status, Dept, cipIdea, Asset

# Register your models here.
admin.site.register(Dept)
admin.site.register(Status)

# Define the admin class
@admin.register(Associate)
class AssociateAdmin(admin.ModelAdmin):
    list_display = ("emp_id", "first_name", "last_name", "dept")
    fields = ['emp_id', ('first_name', 'last_name'), 'dept']

# Register the Admin classes for Asset using the decorator
@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ["asset_num", "dept"]
    fields = [('asset_num', 'dept')]

# Register the Admin classes for cip idea using the decorator
@admin.register(cipIdea)
class cipIdeaAdmin(admin.ModelAdmin):
    
    fieldsets = (
        (None, {
            'fields': ('originator', 'assets')
        }),
        ('Status & Dates', {
            'fields': ('status', 'completed_date')
        }),
        ('Other', {
            'fields': ('summary', 'eng_support', 'annual_savings')
        })
    )
