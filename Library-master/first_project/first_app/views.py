from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,Webpage
# Create your views here.
def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}

    return render(request,'first_app/index.html',context=date_dict)
def cs(request):
    webpages_list=AccessRecord.objects.all()
    suggested_list=AccessRecord.objects.order_by('-date')
    date_dict={'access_records':webpages_list,'suggested_records':suggested_list}

    return render(request,'first_app/cs.html',context=date_dict)

def program(request):

        webpages_list=AccessRecord.objects.all()
        suggested_list=AccessRecord.objects.order_by('-date')
        date_dict={'access_records':webpages_list,'suggested_records':suggested_list}

        return render(request,'first_app/program.html',context=date_dict)

def allbooks(request):
    webpages_list=AccessRecord.objects.all()
    suggested_list=AccessRecord.objects.order_by('-date')
    date_dict={'access_records':webpages_list,'suggested_records':suggested_list}

    return render(request,'first_app/allbooks.html',context=date_dict)

def mech(request):
    webpages_list=AccessRecord.objects.all()
    suggested_list=AccessRecord.objects.order_by('-date')
    date_dict={'access_records':webpages_list,'suggested_records':suggested_list}

    return render(request,'first_app/mech.html',context=date_dict)

def history(request):
    webpages_list=AccessRecord.objects.all()
    suggested_list=AccessRecord.objects.order_by('-date')
    date_dict={'access_records':webpages_list,'suggested_records':suggested_list}

    return render(request,'first_app/history.html',context=date_dict)

def ece(request):
    webpages_list=AccessRecord.objects.all()
    suggested_list=AccessRecord.objects.order_by('-date')
    date_dict={'access_records':webpages_list,'suggested_records':suggested_list}

    return render(request,'first_app/ece.html',context=date_dict)
