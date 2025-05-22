from django.contrib import admin
from .models import Ad, ExchangeProposal

@admin.register(Ad)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'condition', 'created_at')

@admin.register(ExchangeProposal)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('ad_sender', 'ad_receiver', 'status', 'created_at')
