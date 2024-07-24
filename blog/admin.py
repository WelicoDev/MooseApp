from django.contrib import admin
from .models import Category , Post , Contact , Information , Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'category', 'title', 'view_count', 'is_published', 'created_at']
    list_display_links = ('id','user', 'category','title')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' , 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'is_solved' , 'created_at']
    list_display_links = ('id', 'name', 'subject')

@admin.register(Information)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'phone', 'created_at']
    list_display_links = ('id' , 'phone' , 'address')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','is_public', 'created_at']
    list_display_links = ('id', 'user')

