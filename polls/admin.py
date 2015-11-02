from django.contrib import admin
from .models import Question, Choice



# Register your models here.

#Create class for writing questions choices from admin page
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#registers question mode from models.py as an object for the admin file
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']

#make question editable from admin page
admin.site.register(Question, QuestionAdmin)
 
#makes question choices editable from admin page
admin.site.register(Choice)


