from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.decorators import login_required

from .models import User

# Customise the Admin title and header.
admin.site.site_title = "wedding-planner"
admin.site.site_header = "wedding-planner Admin"

admin.site.login = login_required(admin.site.login)

