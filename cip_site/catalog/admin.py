from django.contrib import admin
from .models import Associate, Status, Dept, cipClassification, cipIdea, Asset

# Register your models here.
# admin.site.register(Associate)
admin.site.register(Dept)
admin.site.register(cipClassification)
admin.site.register(Status)
# admin.site.register(cipIdea)
#admin.site.register(Asset)

# Define the admin class
@admin.register(Associate)
class AssociateAdmin(admin.ModelAdmin):
    list_display = ("emp_id", "name", "dept")
    fields = [('emp_id', 'name'), 'dept']

# Register the Admin classes for Asset using the decorator
@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ["asset_num", "dept"]
    fields = [('asset_num', 'dept')]

# Register the Admin classes for cip idea using the decorator
@admin.register(cipIdea)
class cipIdeaAdmin(admin.ModelAdmin):
    list_filter = ('status', 'cip_class')
    
    fieldsets = (
        (None, {
            'fields': ('id', 'originator', 'assets')
        }),
        ('Status and Classification', {
            'fields': ('status', 'cip_class')
        }),
        ('Other', {
            'fields': ('summary', 'eng_support', 'annual_savings')
        })
    )
