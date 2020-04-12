from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Job


@login_required
def search(request):
    import requests
    import json
    api_key = '842b7b02-1d3f-48fd-8e73-1b599b0bce57'

    if request.method == 'POST':
        keywords = request.POST['keywords']
        locationName = request.POST['locationName']
        api_request = requests.get(f'https://{api_key}:@www.reed.co.uk/api/1.0/search?keywords={keywords}&locationName={locationName}&distanceFromLocation=10')
        listings = json.loads(api_request.content)

        context = {
            'keywords': keywords,
            'locationName': locationName,
            'listings': listings
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
