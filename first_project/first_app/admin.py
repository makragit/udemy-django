from django.contrib import admin
from first_app.models import AccessRecord,Topic,Webpage
from first_app.models import UserProfileInfo
from first_app.models import temp_User

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(temp_User)
admin.site.register(UserProfileInfo)
