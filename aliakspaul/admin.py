from django.contrib import admin
from .models import *

# Home
admin.site.register(Home)

# About
class ProfileInLine(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInLine,
    ]


# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
    ]

# Portfolio
admin.site.register(Portfolio)
