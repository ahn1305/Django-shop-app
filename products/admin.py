from django.contrib import admin
from .models import Product, Comment
from .models import Offer


class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','price','stock')

class OfferAdmin(admin.ModelAdmin):
	list_display = ('code','discount')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)
admin.site.register(Comment,CommentAdmin)


