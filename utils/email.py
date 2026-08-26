from django.core.mail import send_mail
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def sending_email(current_user,email_subject,template):
    message = render_to_string(template,{
        'user' : current_user,
    }) ## its convert the template into string and pass the context data into the template, so we can use the context data in the template. Here we pass the current user object into the template, so we can access the current user data in the template.
    to_email = current_user.email ## current_user email address
    
    send_email = EmailMultiAlternatives(email_subject, '', to=[to_email]) ## EmailMultiAlternatives is a class that allows you to send emails with both plain text and HTML content. It takes the subject, message, from email, and a list of recipient email addresses as parameters.
    send_email.attach_alternative(message,'text/html') ## attach_alternative() method is used to attach an alternative version of the email content, in this case, HTML content. The first argument is the content of the alternative version, and the second argument specifies the MIME type of the content,
    send_email.send() ## send() method is called to actually send the email. It sends
    