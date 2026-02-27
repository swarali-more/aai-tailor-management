from django.shortcuts import render, redirect
from .models import Customer

def home(request):
    return render(request, 'home.html')


def add_customer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        Customer.objects.create(
            name=name,
            phone=phone
        )

        return redirect('old_customers')

    return render(request, 'add_customer.html')


def old_customers(request):
    search_query = request.GET.get('search')

    if search_query:
        customers = Customer.objects.filter(name__icontains=search_query)
    else:
        customers = Customer.objects.all()

    return render(request, 'old_customers.html', {
        'customers': customers,
        'search_query': search_query
    })

def customer_detail(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'customer_detail.html', {'customer': customer})

def delete_customer(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('old_customers')