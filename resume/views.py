from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


# Create your views here.
def index(request):
    contact_form = ContactForm()
    context = {
        "contact_form": contact_form,
    }
    return render(request, 'resume/index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            print(form.cleaned_data)
            body = {
                'name': form.cleaned_data['name'],
                'subject': form.cleaned_data['subject'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return HttpResponse("Your query has been sent.", status=200)
            return HttpResponse("Message sent successfully", status=200)

    form = ContactForm()
    return render(request, 'aiprizm/index.html', {'form': form})

