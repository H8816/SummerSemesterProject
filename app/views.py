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




#Register views
def register(request):

        template = loader.get_template('app/register.html')
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

def music(request):

    category = Category.objects.all()
    threads = Thread.objects.all()
    template = loader.get_template('app/music.html')
    context = {
        'threads' : threads,
    }
    return HttpResponse(template.render(context, request))

def currency(request):

    category = Category.objects.all()
    threads = Thread.objects.all()
    template = loader.get_template('app/currency.html')
    context = {
        'threads' : threads,
    }
    return HttpResponse(template.render(context, request))

def movies(request):

    category = Category.objects.all()
    threads = Thread.objects.all()
    template = loader.get_template('app/movies.html')
    context = {
        'threads' : threads,
    }
    return HttpResponse(template.render(context, request))

def love(request):

    category = Category.objects.all()
    threads = Thread.objects.all()
    template = loader.get_template('app/love.html')
    context = {
        'threads' : threads,
    }
    return HttpResponse(template.render(context, request))

def education(request):

    category = Category.objects.all()
    threads = Thread.objects.all()
    template = loader.get_template('app/education.html')
    context = {
        'threads' : threads,
    }
    return HttpResponse(template.render(context, request))

def development(request):

    category = Category.objects.all()
    threads = Thread.objects.all()
    template = loader.get_template('app/development.html')
    context = {
        'threads' : threads,
    }
    return HttpResponse(template.render(context, request))

def newThread(request):

        template = loader.get_template('app/newthread.html')
        context = {

        }
        return HttpResponse(template.render(context, request))
