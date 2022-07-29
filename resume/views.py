from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from .models import Skill, Education, Experience


# Create your views here.
def index(request):
    contact_form = ContactForm()
    skills_list = Skill.objects.all().order_by("-rating")
    education = Education.objects.all()
    experience = Experience.objects.all()
    skill_divider = int(len(skills_list) / 2)
    skills = {
        "skill1": skills_list[:skill_divider],
        "skill2": skills_list[skill_divider:]
    }
    context = {
        "contact_form": contact_form,
        "skills": skills,
        "education": education,
        "experience": experience
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

