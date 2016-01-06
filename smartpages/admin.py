from django.contrib import admin
from .forms import SmartPageForm
from .models import SmartPage
from parler.admin import TranslatableAdmin

# from django.utils.translation import ugettext_lazy as _


@admin.register(SmartPage)
class SmartPageAdmin(TranslatableAdmin):
    form = SmartPageForm
    fieldsets = (
        (None, {'fields': ('code', 'url', 'title', 'content', )}),
    )
    # fieldsets = (
    #     (None, {'fields': ('code', 'url', 'title', 'content', )}),
    #     # (_('Advanced options'), {
    #     #     'classes': ('collapse',),
    #     #     'fields': ('registration_required', 'template_name'),
    #     # }),
    # )
    list_display = ('title', 'all_languages_column', )
    # list_filter = ('sites', 'registration_required')
    search_fields = ('title', )
    readonly_fields = ('code', )
