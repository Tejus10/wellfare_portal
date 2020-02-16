from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Message)
admin.site.register(models.Post)
admin.site.register(models.about)
admin.site.register(models.faq)
admin.site.register(models.counsellor)
admin.site.register(models.psychiatrist)
admin.site.register(models.chairman)
admin.site.register(models.gallery)
admin.site.register(models.announcements)
admin.site.register(models.activities)
admin.site.register(models.counsellor_timing)