from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, mail_admins
from sendmail.models import FeedbackStatus
from mysite import settings


@login_required(login_url='signin/')
def home(request):
    return render(request, "sendmail/home.html")


def send_email(from_email, content):
    # result = mail_admins('My Feedback',
    #                      'From: ' + request.GET['email'] + '\n' + request.GET['comment'])
    result = send_mail(     # return sent emails count
        'My Feedback',
        'From: ' + from_email + '\nBody: ' + content,
        from_email,
        [admin[1] for admin in settings.ADMINS],
        fail_silently=False,
    )

    return result


def sendmail(request):
    send_email_result = send_email(request.GET['email'], request.GET['comment'])
    feedback_item = FeedbackStatus.objects.create(fds_content=request.GET['comment'],
                                                  fds_from=request.GET['email'],
                                                  fds_status=send_email_result)
    feedback_item.save()

    return render(request, "sendmail/home.html")


def signup(request, template_name):
    return render(request, template_name)
