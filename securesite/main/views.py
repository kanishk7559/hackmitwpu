from django.shortcuts import render

# Create your views here.
from django.http.request import QueryDict
from django.shortcuts import render
from django.http import HttpResponse
from extractor import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def getPredictions_random(p1):
    import joblib
    import numpy as np
    model = joblib.load('model/forest.pkl')
    if (len(p1)<=29):
        return("-1")
        
    else:
        arr = np.array([p1])
        prediction = model.predict(arr)
        if prediction == -1:
            return "-1"
        elif prediction == 1:
            return "1"
        else:
            return "error"

def result(request):
    url_01 = str(request.POST['url'])
    p1=generate_data_set(url_01)
    res = getPredictions_random(p1)
    context = {
        'result': res
        }
    return render(request, 'result.html', context)