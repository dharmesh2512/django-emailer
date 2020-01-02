import time
from datetime import timedelta

from celery.decorators import periodic_task
from celery.task.schedules import crontab
from django_emailer.celery import app as celery_app
from services import mailgun

from .models import Email

sent_types = ['delivered', 'opened', 'clicked']
fail_types = ['rejected', 'failed']
pending_types = ['stored', 'accepted']


@celery_app.task(ignore_result=True)
def celery_send_email(email_id, email, subject, content):

    response = mailgun.send_email(
        email, subject, content)
    time.sleep(2)

    if response != None and 'id' in response:
        message_id = response['id'].strip('<').strip('>')

        email = Email.get_email(email_id)
        if email != None:

            email.message_id = message_id
            email.save()

        celery_check_status(email_id, message_id)


@celery_app.task(ignore_result=True)
def celery_check_status(email_id, message_id):

    response = mailgun.check_email_status(message_id)

    event_list = []
    if response != None and 'items' in response:
        items = response['items']

        for item in items:
            event_list.append(item['event'])

        if len(event_list) > 0:
            email = Email.get_email(email_id)
            if email != None:
                if(common_type(sent_types, event_list)):
                    email.status = 'Sent'
                    email.save()
                    return
                if(common_type(fail_types, event_list)):
                    email.status = 'Failed'
                    email.save()
                    return


@periodic_task(run_every=timedelta(minutes=5))
def check_pending_tasks():
    pending_emails = Email.get_pending_emails()

    for email in pending_emails:
        celery_check_status(email.id, email.message_id)


def common_type(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True
    else:
        return False
