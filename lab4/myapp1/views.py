
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (requset):
  return render(requset,"myapp1/index.html")
tax_rate=0.15
def calculate_total_price(request, number):
    try:
        price = (number)
        tax_amount = price * tax_rate
        total_price = price + tax_amount
        return HttpResponse(f"Total Price after 15% Tax: ${total_price}")
    except ValueError:
        return HttpResponse("Please enter a valid number.")
def tax_rate_view(request):
    return render(request, 'tax_calculator/tax_rate.html', {'tax_rate': tax_rate})