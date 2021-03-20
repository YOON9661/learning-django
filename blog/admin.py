from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
from .models import Post, Category, Tag, Comment

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin):
    # 네임 필드를 이용해 슬러그를 자동으로 저장해주는 코드
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Tag, TagAdmin)