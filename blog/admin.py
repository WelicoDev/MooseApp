from django.contrib import admin
from .models import Category , Post , Contact , Information , Comment
from datetime import datetime
from django.utils.html import format_html

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    fields = ("title","view_count", "is_published")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'preview_image', 'category', 'title', 'view_count', 'is_published', 'created_at']
    list_display_links = ('id','user', 'category','title')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ("view_count", 'is_published')
    inlines = (CommentInline, )
    search_fields = ("id", "title", "user", "view_count")

    def preview_image(self , obj):
        return format_html("<img height=80 width=80 src={}>", obj.image.url)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' , 'slug']
    prepopulated_fields = {'slug': ('name',)}
    inlines = (PostInline, )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'is_solved','days',  'created_at']
    list_display_links = ('id', 'name', 'subject')

    def days(self, obj):
        days_diff = (datetime.now() - obj.created_at).days
        if days_diff > 3:
            color = "red"
        else:
            color = "blue"
        if obj.is_solved :
            color = "green"

        return format_html("<div style='color:{}'>{}</div>",color , days_diff)

@admin.register(Information)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'phone', 'created_at']
    list_display_links = ('id' , 'phone' , 'address')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','is_public', 'created_at']
    list_display_links = ('id', 'user')

