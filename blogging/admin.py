from django.contrib import admin
from blogging.models import Post, Category


# and a new admin registration


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('Posts',)


class CategoryInLine(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInLine,
    ]


# class PostInline(admin.TabularInline):
#     model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
