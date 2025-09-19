import csv
import os
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

# helper to call ValueSERP API for a single query
def call_valueserp(api_key, query):
    # Endpoint example - adjust per your ValueSERP plan/documentation
    url = 'https://api.valueserp.com/search'
    params = {
        'q': query,
        'engine': 'google',
        'api_key': api_key,
        'num': 5,
    }
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()

def index(request):
    return render(request, 'searchapp/index.html')

def results(request):
    if request.method != 'POST':
        return redirect('index')

    api_key = request.POST.get('api_key','').strip()
    queries = [request.POST.get(f'query{i}','').strip() for i in range(1,6)]
    queries = [q for q in queries if q]

    errors = []
    results = []

    if not api_key:
        errors.append('API key is required.')
    if not queries:
        errors.append('At least one query is required.')

    if errors:
        return render(request, 'searchapp/index.html', {'errors': errors, 'api_key': api_key, 'queries': queries})

    for q in queries:
        try:
            data = call_valueserp(api_key, q)
        except requests.exceptions.HTTPError as e:
            errors.append(f'API error for query "{q}": {str(e)}')
            continue
        except Exception as e:
            errors.append(f'Network/error for query "{q}": {str(e)}')
            continue

        # Safety: this parsing expects a typical structure; adapt to real ValueSERP response
        items = []
        # Try common keys in valueserp responses
        serp = data.get('organic_results') or data.get('search_results') or data.get('results') or []
        for item in serp:
            title = item.get('title') or item.get('name') or ''
            link = item.get('link') or item.get('url') or item.get('displayed_link') or ''
            snippet = item.get('snippet') or item.get('snippet_text') or item.get('description') or ''
            items.append({'query': q, 'title': title, 'link': link, 'snippet': snippet})
        if not items:
            errors.append(f'No results for query "{q}".')
        results.extend(items)

    # store results in session for CSV download
    request.session['valueserp_results'] = results
    return render(request, 'searchapp/results.html', {'results': results, 'errors': errors})

def download_csv(request):
    results = request.session.get('valueserp_results', [])
    if not results:
        return HttpResponse('No results to download.', status=400)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="valueserp_results.csv"'

    writer = csv.writer(response)
    writer.writerow(['query','title','link','snippet'])
    for r in results:
        writer.writerow([r.get('query'), r.get('title'), r.get('link'), r.get('snippet')])

    return response
