from django.contrib import admin
from polls.models import Answer, Poll, Questions


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    ordering = ('questions_text',)
    list_display = ('id', 'questions_text', 'pub_year', 'poll')
    list_display_links = ('id', 'questions_text',)
    list_per_page = 20
    list_filter = ('pub_date',)
    search_fields = ('questions_text',)
    actions = ('cleanup_text',)

    fieldsets = [
        ("General", {
            "fields": ["questions_text", "pub_date", ]
        }),
        ("External Information", {
            "fields": ["poll", ],
            "description": "Information about related Poll"
        })
    ]

    readonly_fields = ["pub_date"]

    @staticmethod
    def pub_year(obj):
        return obj.pub_date.year

    @staticmethod
    def cleanup_text(modeladmin, request, queryset):
        queryset.update(questions_text="")


admin.site.register(Answer)
admin.site.register(Poll)
admin.site.register(Questions, QuestionAdmin)
