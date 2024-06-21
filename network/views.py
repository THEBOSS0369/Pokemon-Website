from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django import forms
from django.urls import reverse
import requests
from bs4 import BeautifulSoup

from .models import User,  Listing, Category, Comment, Bid, Post


# Pokemon website

class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=50)
    creator = forms.CharField(max_length=50)

# Pokemon Forums
def forum(request):
    posts = Post.objects.all()
    return render(request, 'network/forum.html', {
        'posts': posts
    })

#creating post

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Extract form data
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            creator = form.cleaned_data['creator']
            # Create a new Post object and save it to the database
            post = Post.objects.create(title=title, content=content, creator=creator)
            return redirect('forum')  # Redirect to the forum page after creating the post
    else:
        form = PostForm()
    return render(request, 'network/forum.html', {'form': form})

# pokemon story
def story(request):
    return render(request, 'network/story.html')

# animation
def animation(request):
    return render(request, 'network/animation.html')

# main index
def index(request):
    activelisting = Listing.objects.filter(isActive=True)
    paginator = Paginator(activelisting, 10)  # Show 10 listings per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    allCategories = Category.objects.all()
    return render(request, "network/index.html", {
        "listings": activelisting,
        "categories": allCategories
    })

# pokemons
def listing(request, id):
    listingData = Listing.objects.get(pk=id)
    listinginwatchlist = request.user in listingData.watchlist.all()
    allcomments = Comment.objects.filter(listing=listingData)
    owner = request.user.username == listingData.owner.username
    return render(request, "network/listing.html", {
        "listing": listingData,
        "listinginwatchlist": listinginwatchlist,
        "allcomments": allcomments,
        "owner": owner,
        "update": True,
        "message": "Congrats!! You won the Bid"
    })



# Pokemart
def closeauction(request, id):
    listingData = Listing.objects.get(pk=id)
    listingData.isActive = False
    listingData.save()
    owner = request.user.username == listingData.owner.username
    listinginwatchlist = request.user in listingData.watchlist.all()
    allcomments = Comment.objects.filter(listing=listingData)
    return render(request, "network/listing.html", {
        "listing": listingData,
        "listinginwatchlist": listinginwatchlist,
        "allcomments": allcomments,
    })

# Pokemon 
def watchlist(request):
    currentUser = request.user
    listings = currentUser.watchlist.all()
    return render(request, "network/watchlist.html", {
        "listings": listings
    })

# Pokemart
def addBid(request, id):
    newBid = request.POST['newBid']
    listingData = Listing.objects.get(pk=id)
    owner = request.user.username == listingData.owner.username
    if int(newBid) > listingData.price.bid:
        updateBid = Bid(user=request.user, bid=int(newBid))
        updateBid.save()
        listingData.price = updateBid
        listingData.save()
        return render(request, "network/listing.html", {
            "listing": listingData,
            "update": True,
            "owner": owner
        })
    else:
        return render(request, "network/listing.html", {
            "listing": listingData,
            "message": "Bid was Not Successful",
            "update": False,
            "owner": owner
        })

# commment section
def addcomment(request, id):
    user = request.user
    listingData = Listing.objects.get(pk=id)
    message = request.POST['newComment']

    newComment = Comment(
        author=user,
        listing=listingData,
        message=message
    )

    newComment.save()

    return HttpResponseRedirect(reverse("listing",  args=(id, )))

# add pokemon
def addlist(request, id):
    listingData = Listing.objects.get(pk=id)
    user = request.user
    listingData.watchlist.remove(user)
    return HttpResponseRedirect(reverse("listing",  args=(id, )))

# remove pokemon
def removelist(request, id):
    listingData = Listing.objects.get(pk=id)
    user = request.user
    listingData.watchlist.add(user)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

# create/ add
def create(request):
    if request.method == "GET":
        allCategories = Category.objects.all()
        return render(request, "network/create.html", {
            "categories": allCategories
        })
    else:
        #Get the data from form
        title = request.POST["title"]
        description = request.POST["description"]
        url = request.POST["url"]
        category = request.POST["category"]
        price = request.POST["price"]

        #Get the data of User
        presentUser = request.user

        #Get all content
        categoryData = Category.objects.get(categoryN=category)

        #bidding
        bid = Bid(bid=float(price), user=presentUser)
        bid.save()

        #create a new listing
        newlist = Listing(
            title=title,
            description=description,
            url=url,
            category=categoryData,
            price=bid,
            owner=presentUser
        )
        
        #save the data
        newlist.save()

        #redirect to index page
        return HttpResponseRedirect(reverse(index))
    

# show the data
def display(request):
    if request.method == "POST":
        categoryForm = request.POST['category']
        category = Category.objects.get(categoryN=categoryForm)
        activelisting = Listing.objects.filter(isActive=True, category=category)
        allCategories = Category.objects.all()
        return render(request, "network/index.html", {
            "listings": activelisting,
            "categories": allCategories
        })


# login section
def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


# logout section
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# register section
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


