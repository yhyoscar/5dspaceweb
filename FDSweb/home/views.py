import json 
from django.shortcuts import render
from datetime import date, datetime

# Create your views here.


def homeview(request):
    dout = {'request_time': datetime.now().isoformat()}
    for x in dir(request):
        dout[x] = str(getattr(request, x))

    return render(request, 'home.html', 
        context = {'oscar': 'hi oscar', 
            #'request': json.dumps(dout, indent=2).replace('\n', '<br>').replace(' ', '&nbsp;'),  
            'request': dout, } )
