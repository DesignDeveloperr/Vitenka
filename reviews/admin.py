from django.contrib import admin

from reviews.models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'datetime')


admin.site.register(Reviews, ReviewsAdmin)
