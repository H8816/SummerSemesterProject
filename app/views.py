from django.http import HttpResponse
from django.template import loader
from .models import User, Thread, Category, Postings

# Index View
def index(request):
    #Load template
    template = loader.get_template('app/index.html')
    context = {

    }
    # Return the template and data imported from database
    return HttpResponse(template.render(context, request))

# Login view
def login(request):

        template = loader.get_template('app/login.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

# List all threads
def threads(request):

        threads = Thread.objects.all()
        template = loader.get_template('app/threads.html')

        context = {
            'threads' : threads,
        }
        return HttpResponse(template.render(context, request))

#View a thread
def detailed_view(request, thread_id):

    threads = Thread.objects.all()
    comments = Postings.objects.all()
    template = loader.get_template('app/details.html')

    context = {
        'threads' : threads,
        'comments' : comments,
    }
    return HttpResponse(template.render(context, request))
