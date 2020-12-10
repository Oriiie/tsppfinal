from django.contrib import admin
from django import forms
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInLine(admin.TabularInline):
    readonly_fields = ("name", "email")
    model = Reviews
    extra = 0


class MovieShotsInLine(admin.StackedInline):
    model = MovieShots
    extra = 0


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [ReviewInLine, MovieShotsInLine]
    form = MovieAdminForm
    save_on_top = True
    save_as = True
    list_editable = ("draft", )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "movie", "ip")


admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(RatingStar)

admin.site.site_title = "Что посмотреть?"
admin.site.site_header = "Что посмотреть?"
