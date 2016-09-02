from django.contrib import admin

from blog.models import Chapter,Article,Commentary



class articlewhateveryouwantclassadmindisplay(admin.ModelAdmin):

    def bar(self, obj):
        return 'bar'
    list_display = ['__unicode__', 'chapter', 'foo']


class show_comment(admin.ModelAdmin):
    def bar(self, obj):
        return 'bar'
    list_display = ['comment_text', 'comment_time', 'article']


admin.site.register(Chapter)
admin.site.register(Article,articlewhateveryouwantclassadmindisplay)
admin.site.register(Commentary, show_comment)
# Register your models here.
