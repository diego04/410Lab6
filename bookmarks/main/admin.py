
from django.contrib import admin
from main.models import Link, Tag

# Register your models here.

    
admin.site.register(Link)
admin.site.register(Tag)
"""
class LinkAdmin(admin.StackedInline):
    model = Link
    extra = 5
class TagAdmin(admin.StackedInline):
    model = Tag
    extra = 5"""
"""
class Linkmodelish(admin.StackedInline):
    model = Posts
    extra = 5
    

class AuthorAdmin(admin.ModelAdmin):
    #fields = ['author_username','registration_date', 'author_email']
    
    fieldsets = [
        (None,                 {'fields':['author_username']}),
        #('Registration Date',  {'fields':['registration_date']}),
        ('Email',              {'fields':['author_email']}),
    ]
    
   # list_display = ('author_username','registration_date','author_email')
    list_display = ('author_username','author_email')
    
    
    inlines = [PostInline]"""
    
#admin.site.register(TagAdmin)
#admin.site.register(LinkAdmin)