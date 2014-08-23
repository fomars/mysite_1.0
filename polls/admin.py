from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInLine]
# class ChoiceAdmin(admin.ModelAdmin):


admin.site.register(Poll, PollAdmin)
# Register your models here.
