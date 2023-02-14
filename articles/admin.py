from django.contrib import admin
from .models import Articles,Comment

admin.site.register(Comment)

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display=['title','author']# admin-panelde bu field-lerde gorunecek
    list_display_links=['title','author'] # admin-panelde bu field-lerin ustune gelende link verilmiw olur ve kecid elemek olur
    search_fields=['title'] # admin-panelde axtaris elediyimiz zaman title gore axtrarir
    list_filter=['title'] # filter eliyir
    class Meta:
        model=Articles
        
