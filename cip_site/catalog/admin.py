from django.contrib import admin
from .models import Associate, Shift, Dept, Status, CIP_Classification, CIP_Idea, Asset

# Register your models here.
admin.site.register(Associate)
admin.site.register(Shift)
admin.site.register(Dept)
admin.site.register(Status)
admin.site.register(CIP_Classification)
admin.site.register(CIP_Idea)
admin.site.register(Asset)