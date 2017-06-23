from django.contrib import admin

from .models import Category, Item


# Register your models here.

# admin.site.register(Category)
admin.site.register(Item)

 # This tells Django: Item objects are edited on the Category admin page. By default, provide enough fields for 5 items (3 default).”
class ItemInline(admin.TabularInline):
    model = Item
    extra = 2

class CategoryAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['category_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
        ]
    inlines = [ItemInline]

    list_display = ('category_name', 'pub_date', 'was_published_recently')
    
    list_filter = ['pub_date'] 

    search_fields = ['category_name'] 

admin.site.register(Category, CategoryAdmin)

# class AdminClass(admin.ModelAdmin):
#     fields = ['pub_date', 'category_name']

# admin.site.register(Admin, AdminClass)
