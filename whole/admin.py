from django.contrib import admin
from .models import Feedback
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('feedtime', 'feedpersonname', 'status')
	list_filter = ('status',)

admin.site.register(Feedback, FeedbackAdmin)