from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Portofolio, SkillImage, Contact

# Home
admin.site.register(Home)

# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
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

# Portofolio
admin.site.register(Portofolio)

# SkillImage
admin.site.register(SkillImage)

# Contact
admin.site.register(Contact)