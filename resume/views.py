from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

from .forms import ContactForm
from .models import Skill, Education, Experience, Portfolio, ProjectCategory


# Create your views here.


@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")


def index(request):
    contact_form = ContactForm()
    skills_list = Skill.objects.all().order_by("-rating")
    education = Education.objects.all()
    experience = Experience.objects.all()
    portfolios = Portfolio.objects.all().order_by("order")
    category = ProjectCategory.objects.all()
    skill_divider = int(len(skills_list) / 2)
    skills = {
        "skill1": skills_list[:skill_divider],
        "skill2": skills_list[skill_divider:]
    }
    context = {
        "contact_form": contact_form,
        "skills": skills,
        "education": education,
        "experience": experience,
        "portfolio": portfolios,
        "categories": category
    }
    return render(request, 'resume/index.html', context)


def portfolio(request, _id):
    try:
        data = Portfolio.objects.get(id=_id)
    except Portfolio.DoesNotExist:
        raise Http404('Data does not exist')

    context = {
        'portfolio': data
    }
    return render(request, 'resume/portfolio-details-view.html', context)


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
