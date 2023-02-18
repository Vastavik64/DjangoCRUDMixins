from django.contrib import admin

# Register your models here.
from .models import user

# Register your models here.
@admin.register(user)
class useradmin(admin.ModelAdmin):
    '''
    Created user model is registered to be reflected in database
    '''
    list_display = ['id','name','birthdate','gender','created_at','updated_at','is_active','is_delete']