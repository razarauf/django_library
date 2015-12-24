from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^addLibrary/$', views.addLibView, name="addLibraryView"),
    url(r'^addBook/(?P<lib_id>[0-9]+)/$', views.addBookView, name="addBookView"),
    url(r'^addTag/(?P<book_id>[0-9]+)/$', views.addTagView, name="addTagView"),
    url(r'^searchTag/$', views.searchTag, name="searchTag"),

    url(r'^booksInLibrary/(?P<lib_id>[0-9]+)/$', views.booksInLibrary, name="booksInLibrary"),
]