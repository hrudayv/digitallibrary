from django.contrib import admin
from books.models import book
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
#admin.site.register(book)

class BookResource(resources.ModelResource):

    class Meta:
        model = book

class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

admin.site.register(book, BookAdmin)
