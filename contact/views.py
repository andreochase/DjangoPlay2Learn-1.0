from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email]
            send_mail(email_subject, email_message, to_email, from_email, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
            return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)

