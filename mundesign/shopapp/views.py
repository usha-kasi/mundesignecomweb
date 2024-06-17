from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Order, Address, PaymentDetails, Wishlist, Recommendation, OrderItem


# Create your views here.


def home(request):
    return render (request, "login.html")

def demo(request):
    return HttpResponse("Thanks for visiting")

def login_view(request):
    #if request.method == "POST":
     #   username = request.POST['username']
      #  password = request.POST['password']
       # user = authenticate(request, username=username, password=password)
       # if user is not None:
        #    login(request, user)
        #    return HttpResponseRedirect(reverse('welcome'))
       # else:
        #    return render(request, 'shopapp/login.html', {'error': 'Invalid login credentials'})
   # else:
        return render(request, 'login.html')

@login_required
def welcome(request):
    return render(request, 'welcome.html')


@login_required
def my_account(request):
    debug_info = {
        'user': request.user,
        'is_authenticated': request.user.is_authenticated,
    }
    return render(request, 'my_account.html', {'debug_info': debug_info})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html', {'orders': orders})

@login_required
def saved_addresses(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'saved_addresses.html', {'addresses': addresses})

@login_required
def saved_payment_details(request):
    payments = PaymentDetails.objects.filter(user=request.user)
    return render(request, 'saved_payment_details.html', {'payments': payments})

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def recommendations(request):
    recommendations = Recommendation.objects.filter(user=request.user)
    return render(request, 'recommendations.html', {'recommendations': recommendations})

@login_required
def individual_order(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    order_items = order.orderitem_set.all()  # Get related order items
    return render(request, 'individual_order.html', {'order': order, 'order_items': order_items})


@login_required
def return_order(request):
    return render(request, 'shopapp/return_order.html')

@login_required
def order_history(request):
    return render(request, 'index.html')



def order_history_json(request):
    orders = [
        {
            "order_id": 1,
            "order_date": "2024-06-01",
            "items_purchased": "Item A, Item B",
            "total_amount": "100",
            "order_status": "Delivered",
            "delivery_address": "123 Street, City",
            "delivery_date": "2024-06-05"
        },
        {
            "order_id": 2,
            "order_date": "2024-06-02",
            "items_purchased": "Item C, Item D",
            "total_amount": "90",
            "order_status": "in transit",
            "delivery_address": "123 Street, City",
            "delivery_date": "2024-06-10"
        },
        {
            "order_id": 3,
            "order_date": "2024-06-10",
            "items_purchased": "Item E, Item F",
            "total_amount": "150",
            "order_status": "not Delivered",
            "delivery_address": "123 Street, City",
            "delivery_date": "2024-06-15"
        },
        # Add more orders as needed
    ]
    return JsonResponse(orders, safe=False)

