from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from .models import Job
import datetime

@login_required(redirect_field_name='next', login_url='login')
def search(request):
    import requests
    import json
    api_key = '842b7b02-1d3f-48fd-8e73-1b599b0bce57'

    greeting = 'Good '
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        greeting += 'morning'
    elif hour < 18:
        greeting += 'afternoon'
    else:
        greeting += 'evening'

    if request.method == 'POST':
        jobs = Job.objects.filter(user=request.user).values_list('jobId', flat=True)
        keywords = request.POST['keywords']
        locationName = request.POST['locationName']
        api_request = requests.get(f'https://{api_key}:@www.reed.co.uk/api/1.0/search?keywords={keywords}&locationName={locationName}&distanceFromLocation=10')
        listings = json.loads(api_request.content)

        context = {
            'keywords': keywords,
            'locationName': locationName,
            'listings': listings,
            'jobs': jobs
        }
        
        return render(request, 'jobs/listings.html', context)
    else:
        context = {
            'greeting': greeting
        }
        return render(request, 'jobs/search.html', context)

@login_required(redirect_field_name='next', login_url='login')
def detail(request, job_id):
    import requests
    import json
    api_key = '842b7b02-1d3f-48fd-8e73-1b599b0bce57'
    api_request = requests.get(f'https://{api_key}:@www.reed.co.uk/api/1.0/jobs/{job_id}')
    listing = json.loads(api_request.content)
    user = request.user

    context = {
        'listing': listing,
        'user': user
    }

    return render(request, 'jobs/detail.html', context)
    

@login_required(redirect_field_name='next', login_url='login')
def share_job(request):
    if request.method == 'POST':
        subject = 'You\'ve been sent a job from jobsearch.co.uk'
        email_from = request.POST['email-from']
        email_to = request.POST['email-to']
        job_title = request.POST['job-title']
        location = request.POST['location']
        salary = request.POST['salary']
        job_url = request.POST['job-url']
        job_description = request.POST['job-description']

        context = {
            'emailFrom': email_from,
            'jobTitle': job_title,
            'location': location,
            'salary': salary,
            'jobUrl': job_url,
            'jobDescription': job_description
        }

        html_message = render_to_string('emails/share_job_email.html', context)
        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            email_from,
            [email_to,],
            html_message=html_message
        )
    return HttpResponse(status=204)

def listings(request):
    return render(request, 'jobs/listings.html', {})

@login_required(redirect_field_name='next', login_url='login')
def shortlist(request):
    jobs = Job.objects.filter(user=request.user).order_by('-saveDate')
    return render(request, 'jobs/shortlist.html', {'jobs': jobs})


@login_required(redirect_field_name='next', login_url='login')
def delete(request, job_id):
    job = Job.objects.get(pk=job_id)
    job.delete()
    return redirect('shortlist')


@login_required(redirect_field_name='next', login_url='login')
def remove_from_shortlist(request, job_id):
    job = Job.objects.get(jobId=job_id)
    job.delete()
    return HttpResponse(status=204)


@login_required(redirect_field_name='next', login_url='login')
def add_to_shortlist(request, job_id):
    import requests
    import json
    api_key = '842b7b02-1d3f-48fd-8e73-1b599b0bce57'
    api_request = requests.get(f'https://{api_key}:@www.reed.co.uk/api/1.0/jobs/{job_id}')
    listing = json.loads(api_request.content)
    job = Job()
    job.user = request.user
    job.jobTitle = listing['jobTitle']
    job.jobId = listing['jobId']
    job.locationName=listing['locationName']
    job.employerName=listing['employerName']
    job.jobUrl=listing['jobUrl']
    job.save()
    return HttpResponse(status=204)
