from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import re
import requests

def index(request):
    """
    Show home page
    """
    return render(request, 'scraper/index.html')

def extract_email_ajax(request):
    """
    Get URL to parse and return email found in respected url
    """

    if request.method == 'GET':
        email_regex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9.-]+
                        (\.[a-zA-Z]{2,4}))''', re.VERBOSE)

        urls = request.GET.get('URLS')

        page_data = requests.get(urls)
        page_html = str(page_data.content)
        matches = ""

        for groups in email_regex.findall(page_html):
            if matches.find(groups[0]) == -1:
                matches += groups[0] + ', '

        return JsonResponse({'extracted_emails': matches, 'for_url': urls})
