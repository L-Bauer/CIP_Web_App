from django.contrib import admin
from .models import Associate, Shift, Dept, Status, cipClassification, cipIdea, Asset

# Register your models here.
admin.site.register(Associate)
admin.site.register(Shift)
admin.site.register(Dept)
admin.site.register(Status)
admin.site.register(cipClassification)
admin.site.register(cipIdea)
admin.site.register(Asset)