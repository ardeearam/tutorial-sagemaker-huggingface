from django.http import HttpResponse
from django.shortcuts import render
from app.lib.sagemaker import SageMakerRuntime
from app.lib.processor import combine_tokens, tag_text
from pprint import pprint
import json


def home(request):
  if request.method == 'GET':

    return render(request, 'app/index.html', {})

  # POSTback (old school)
  # We can do AJAX style, but it will make this tutorial 
  # more complicated than it should be.
  elif request.method == 'POST':

    query = request.POST.get('query')
    sagemaker_runtime_client = SageMakerRuntime()
    response = sagemaker_runtime_client.invoke_endpoint({"inputs": query})
    print(response)
    
    message = tag_text(text=query, tags=combine_tokens(response))

    return render(request, 'app/index.html', {
      'query': query, 
      'message': message,
      'references': '',
      'references_count': 0
    }) 
      
