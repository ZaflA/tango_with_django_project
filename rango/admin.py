from django.contrib import admin
from rango.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    #fields = ['name', 'views', 'likes']
    #list_display = ('name', 'views', 'likes')

class PageAdmin(admin.ModelAdmin):
    #fields = ['category','title', 'url', 'views']
    list_display = ('title', 'category', 'url','views')

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)