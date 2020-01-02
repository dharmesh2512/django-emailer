from django.db import models

# from multi_email_field.fields import MultiEmailField

# Create your models here.


class Email(models.Model):
    # emails = MultiEmailField()
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField(blank=False, null=False)
    created_date_time = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Sent', 'Sent'),
        ('Failed', 'Failed'),
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    message_id = models.CharField(max_length=255, blank=True, null=True)

    @staticmethod
    def get_email(email_id):
        obj = None
        try:
            obj = Email.objects.get(id=email_id)
        except:
            obj = None
        return obj

    @staticmethod
    def get_pending_emails():
        emails = Email.objects.filter(status='Pending')
        return emails
