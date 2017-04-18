from django.contrib import admin
from .models import Travel
# Register your models here.
class TravelAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'publishtime', 'updatetime', 'tag', 'status')
	search_fields = ('title', 'author', 'tag', 'status')
	list_filter = ('tag', 'status')


admin.site.register(Travel, TravelAdmin)