from django.contrib import admin
from studentPortal.models import Analysis, Resume, User_Profile
# Register your models here.
admin.site.register(User_Profile)
admin.site.register(Analysis)
admin.site.register(Resume)
