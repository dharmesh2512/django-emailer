from django.contrib import admin

# Register your models here.
from emailer.models import Email

from .tasks import celery_check_status, celery_send_email


class EmailAdmin(admin.ModelAdmin):

    def date_time(self, obj):
        return obj.created_date_time.strftime("%d-%b-%Y %H:%M:%S")

    date_time.admin_order_field = 'created_date_time'
    date_time.short_description = 'Date Time'

    list_display = ['date_time', 'email', 'subject', 'status', 'message_id']

    fieldsets = (
        (None, {
            'fields': ('email', 'subject', 'content', 'status',),
        }),
    )

    def save_model(self, request, obj, form, change):
        super(EmailAdmin, self).save_model(request, obj, form, change)
        celery_send_email.delay(obj.id, obj.email, obj.subject, obj.content)


admin.site.register(Email, EmailAdmin)
