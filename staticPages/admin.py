"""
Admin configuration for staticPages app.

This module registers the Collection and Piece models
with the Django admin site.
"""

from django.contrib import admin
from .models import Collection,Piece
# Register your models here.
admin.site.register(Collection)
admin.site.register(Piece)
