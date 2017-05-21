from django.contrib import admin
from .models import User, Thread, Postings,  Category

admin.site.register(User)
admin.site.register(Thread)
admin.site.register(Postings)
admin.site.register(Category)
