from django.contrib import admin

from .models import User, Item, Bid, Comment

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','user','minimum','category')
    search_fields = ('user','category','name')
    # readonly_fields = ('user',)

    filter_horizontal =()
    list_filter = ()
    fieldsets = ()

class BidAdmin(admin.ModelAdmin):
    list_display = ('name','user','minimum','category')
    search_fields = ('user','category','name')
    # readonly_fields = ('user',)

    filter_horizontal =()
    list_filter = ()
    fieldsets = ()

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','item','comment')


admin.site.register(User)
admin.site.register(Item, ItemAdmin)
admin.site.register(Bid)
admin.site.register(Comment)