from django.contrib import admin
from .models import Lift, Nutrition,Weight

# Register your models here.


admin.site.register(Lift)
admin.site.register(Nutrition)
admin.site.register(Weight)