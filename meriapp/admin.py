from django.contrib import admin
from .models import Emailspam
from .models import Contact

# Register your models here.
admin.site.register(Emailspam)
admin.site.register(Contact)
