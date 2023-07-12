from django.contrib import admin
from .models import Level, Levelperprogram ,Contents


# Register your models here.


admin.site.register(Levelperprogram)
admin.site.register(Level)
admin.site.register(Contents)
