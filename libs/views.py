from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Library, Book, BookTags
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LibraryForm, BookForm, TagForm, SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

#@login_required(login_url='/accounts/login/')
def index(request):
    libraries = Library.objects.order_by('-timestamp')#[:5]
    context = {"last_5_libraries": libraries}
    return render(request, 'libs/index.html', context)

def signUpView(request):
    form = SignUpForm(request.POST or None)
    context = {"form":form}
    if form.is_valid():
        # print form.cleaned_data.get("name")
        form.save()
        return HttpResponseRedirect(reverse('libs:index'))
    return render(request, 'libs/signup2.html', context)
    #return render(request, 'libs/signup.html')

def loginView(request):
    form = LoginForm(request.POST or None)
    context = {"form":form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('libs:index'))
        else:
            return render(request, 'libs/signup2.html', {
            'error_message': "The user is not active",
            })
    return render(request, 'libs/login.html', context)

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('libs:loginView'))

def addLibView(request):
    form = LibraryForm(request.POST or None)
    context = {"form":form}
    if form.is_valid():
        # print form.cleaned_data.get("name")
        form.save()
        return HttpResponseRedirect(reverse('libs:index'))
    return render(request, 'libs/add_lib.html', context)

def addBookView(request, lib_id):
    rlib = get_object_or_404(Library, pk=lib_id)
    form = BookForm(request.POST or None)
    context = {
        "form":form,
        "lib_id": lib_id,
    }
    # have to create an instance
    if form.is_valid() and rlib:
        instance = form.save(commit=False)
        instance.library = rlib
        instance.save()
        return HttpResponseRedirect(reverse('libs:booksInLibrary', args=(rlib.id,)))
    return render(request, 'libs/add_book.html', context)

def addTagView(request, book_id):
    rbook = get_object_or_404(Book, pk=book_id)
    form = TagForm(request.POST or None)

    context = {
        "form": form,
        "book_id": book_id,
    }

    if form.is_valid() and rbook:
        instance = form.save(commit=False)
        instance.tag = rbook
        instance.save()
        return HttpResponseRedirect(reverse('libs:booksInLibrary', args=(rbook.library.id,)))
    return render(request, 'libs/add_tag.html', context)

def booksInLibrary(request, lib_id):
    rlib = get_object_or_404(Library, pk=lib_id)
    context = {
        "library":rlib
    }
    return render(request, 'libs/books_in_lib.html', context)

def searchTag(request):
    searchThisTag = str(request.POST['searchThisTag'])
    rTags = get_list_or_404(BookTags, tagname__contains=searchThisTag)
    # for eachTag in rTags:
    #     print eachTag.tag.title
    context = {
        "tagName":searchThisTag,
        "allTheTags":rTags,
    }
    return render(request, 'libs/search_tag.html', context)

"""
Another maybe less safer way of doing it with raw forms
AKA no validation... and no crispy forms

def signUp(request):
    try:
        signUpUsername = str(request.POST['signUpUsername'])
        signUpEmail = str(request.POST['signUpEmail'])
        signUpPassword = str(request.POST['signUpPassword'])

        user = User.objects.create_user(signUpUsername, signUpEmail, signUpPassword)
        user.save()
    except (KeyError):
        return render(request, 'libs/signup.html', {
            'error_message': "Cannot leave either box empty",
        })

    return render(request, 'libs/index.html')

def addLibrary(request):
    # creating a new library
    l = Library(name=str(request.POST['lib_name']))
    l.save()
    # return HttpResponseRedirect(reverse('libs:index', args=(p.id,)))
    return HttpResponseRedirect(reverse('libs:index'))

def addBook(request, lib_id):
    # get the library obj
    rlib = get_object_or_404(Library, pk=lib_id)
    book = Book(title=str(request.POST['book_title']))
    # book = Book(title="Some title")
    book.library = rlib
    book.author = str(request.POST['author_name'])
    # book.author = "raza314159"
    book.save()
    # output = "This is addBook" + str(rlib.name) + " " + str(book.title)
    return HttpResponseRedirect(reverse('libs:booksInLibrary', args=(rlib.id,)))
    # return HttpResponse(output)
"""

