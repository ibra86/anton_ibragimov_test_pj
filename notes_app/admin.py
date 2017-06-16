from django.contrib import admin

# Register your models here.
from .models import Note, Book, BookContent
from .forms import NoteForm


class NoteAdmin(admin.ModelAdmin):
    form = NoteForm
    actions = ['bulk_admin_deletion']

    def get_actions(self, request):
        actions = super(NoteAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def bulk_admin_deletion(self, request, queryset):
        for obj in queryset:
            obj.delete()
        if queryset.count() == 1:
            msg = "1 note entry was"
        else:
            msg = "%s notes entries were" % queryset.count()
        self.message_user(request, "%s successfully deleted." % msg)
    bulk_admin_deletion.short_description = "Delete selected notes"


class BookNoteInline(admin.TabularInline):
    model = BookContent
    extra = 1


class BookAdmin(admin.ModelAdmin):
    inlines = (BookNoteInline,)


admin.site.register(Note, NoteAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContent)
