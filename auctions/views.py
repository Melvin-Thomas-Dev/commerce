from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Item
from .forms import BidForm



def index(request):
    context = {}
    items = Item.objects.all()
    context['items'] = items
    return render(request, "auctions/index.html", context)

def detail_view(request, pk):
    context = {}
    try:
        item = Item.objects.get(pk=pk)
        context['item'] = item
    except Item.DoesNotExist:
        context['error'] = "The listing does not exist"
        return render(request, "auctions/error.html", context)


    return render(request, "auctions/detail.html", context)
    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def bid_view(request, pk):
    context = {}
    user = request.user
    try:
        item = Item.objects.get(pk=pk)
        context['item'] = item
    except Item.DoesNotExist:
        # item = None
        context['error'] = "The listing does not exist"
        return detail_view(request, pk)
    if request.POST:
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.clean_amount()
            context['message'] = f"succesfully placed a bid. The bid amount is {bid}"
            return render(request, "auctions/bid.html")
        else:
            context['form'] = form
    else:
        form = BidForm()
        context['form'] = form

    return render(request, "auctions/detail.html", context)



    # if request.POST:
    #     try:
    #         item = Item.objects.get(pk=pk)
    #         context['item'] = item
    #     except Item.DoesNotExist:
    #         item = None
    #         context['error'] = "The listing does not exist"
    #         return detail_view(request, pk)
        
    #     highest_bid = item.bid.get(pk=pk).amount
    #     bid = int(request.POST['bid'])
    #     # highest_bid = item.highest_bid
    #     if not bid>highest_bid:
    #         context['message'] = f"The existing highest bid for this item is {item.bid.amount}"
    #         return render(request, "auctions/bid.html", context)
    #     if bid > highest_bid:
    #         item.bid.get(pk=pk).amount = bid
    #         context['message'] = f"You have successfully placed a Bid. The bid amount is: {bid}"
    #         return render(request, "auctions/bid.html", context)
    # else:
    #     return render(request, "auctions/detail.html", context)

            
            
        


