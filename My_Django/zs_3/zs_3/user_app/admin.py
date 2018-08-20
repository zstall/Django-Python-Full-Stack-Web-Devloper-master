from django.contrib import admin
from user_app.models import User, Username, Email
# Register your models here.
admin.site.register(User)
admin.site.register(Username)
admin.site.register(Email)
