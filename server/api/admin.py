from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'document', 'phone', 'registrationDate')
    search_fields = ('name', 'email', 'document', 'phone')
    list_filter = ('registrationDate',)
    ordering = ('-registrationDate',)

admin.site.register(User, UserAdmin)