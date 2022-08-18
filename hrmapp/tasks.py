# from celery.decorators import task
# from celery.utils.log import get_task_logger
# from django.core.management import call_command
from celery import shared_task
from celery import app as celery_app
# from django.core.mail import EmailMessage

from django.core.mail import send_mail
from hrm import settings

# logger = get_task_logger(__name__)


# @shared_task
# def test():
#     logger.info('test')

# fknhkdgoiihyangh


@shared_task(name='send_email_task')
def send_maildetails(email):
    send_mail(
   subject="test  mail",
   message="this is test",
   from_email=settings.EMAIL_HOST_USER,
   recipient_list=[email],
   fail_silently=True,
    )



# @app.task(name='test')
# def test():
#     logger.info('testtttttttt')


# send_mail_task.delay(your_subject, your_messaage, your_email, your_recepient_list)

# method2
# from django.core.mail import send_mail

