from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Job


@login_required
def search(request):
    import requests
    import json
    api_key = '842b7b02-1d3f-48fd-8e73-1b599b0bce57'

    if request.method == 'POST':
        jobs = Job.objects.filter(user=request.user)
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
        return render(request, 'jobs/search.html', {})


def listings(request):
    return render(request, 'jobs/listings.html', {})

@login_required
def shortlist(request):
    jobs = Job.objects.filter(user=request.user).order_by('-saveDate')
    return render(request, 'jobs/shortlist.html', {'jobs': jobs})


@login_required
def delete(request, job_id):
    job = Job.objects.get(pk=job_id)
    job.delete()
    return redirect('shortlist')


@login_required
def remove_from_shortlist(request, job_id):
    job = Job.objects.get(jobId=job_id)
    job.delete()
    return HttpResponse(status=204)


@login_required
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
