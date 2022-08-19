from celery import shared_task
from celery import app as celery_app
from django.core.mail import send_mail
from hrm import settings

@shared_task(name='send_email_task')
# def send_maildetails(email):
#     send_mail(
#    subject = "Test mail",
#    message = "this is test",
#    from_email = settings.EMAIL_HOST_USER,
#    recipient_list =[ email],
#    fail_silently = True,
#     )

def send_maildetails(email):
     send_mail(
    subject = "Test mail",
    message = "this is test",
    from_email='shisirakrishna@gmail.com',
    recipient_list =[ email],
    fail_silently = False,
    )




