from django.contrib import admin
from sendmail.models import FeedbackStatus


class FeedbackStatusAdmin(admin.ModelAdmin):
    list_display = ('fds_content', 'fds_from', 'fds_status', 'fds_create_time', )


admin.site.register(FeedbackStatus, FeedbackStatusAdmin)
