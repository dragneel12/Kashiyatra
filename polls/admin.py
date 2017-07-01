from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Question,Choice,UserProfile

class QuestionAdmin(admin.ModelAdmin):
    field = ('question_text','pub_date')
    date_hierarchy = 'pub_date'

# class UserProfileInline(admin.StackedInline):
#     model = UserProfile
#     can_delete=False
#     verbose_name="userprofile"
#
# class BaseUserAdmin(UserAdmin):
#     inline=(UserProfileInline,)


# admin.site.register(User)
admin.site.register(UserProfile)


admin.site.register(Question,QuestionAdmin)

admin.site.register(Choice)
