from django.contrib import admin

# Register your models here.
from .models import Confession
from django.contrib.auth.models import Group
from django.contrib.auth.models import User, Group

class ProfileInline(admin.StackedInline):
    model = Confession

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
#admin.site.register(Profile)
# Remove: admin.site.register(Profile)