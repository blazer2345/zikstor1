from django.shortcuts import render

# Create your views here.

def productsPage(request):
  return render(request, 'productpage.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductUploadForm

def product_page(request):
    products = Product.objects.filter(status='approved')

    return render(request, 'home.html', {
        'products': products
    })

def get_cart_count(request):
    cart = request.session.get('cart', {})
    return sum(cart.values())


# MAIN PRODUCT PAGE
def home(request):

    search = request.GET.get('q', '')

    products = Product.objects.filter(
        status='approved'
    )

    if search:
        products = products.filter(
            product_name__icontains=search
        )

    context = {
        'products': products,
        'search': search,
        'cart_count': get_cart_count(request),
    }

    return render(
        request,
        'home.html',
        context
    )


# UPLOAD PRODUCT PAGE
def upload_product(request):

    if request.method == 'POST':

        form = ProductUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            product = form.save(commit=False)

            product.status = 'pending'

            product.save()

            messages.success(
                request,
                'Product uploaded successfully! '
                'It will appear after admin approval.'
            )

            return redirect('upload_product')

    else:
        form = ProductUploadForm()

    context = {
        'form': form,
        'cart_count': get_cart_count(request),
    }

    return render(
        request,
        'upload.html',
        context
    )


# ADD PRODUCT TO CART
def add_to_cart(request, product_id):

    if request.method != 'POST':
        return redirect('home')

    product = get_object_or_404(
        Product,
        id=product_id,
        status='approved'
    )

    cart = request.session.get('cart', {})

    product_id = str(product.id)

    cart[product_id] = cart.get(product_id, 0) + 1

    request.session['cart'] = cart

    messages.success(
        request,
        'Product added to your cart.'
    )

    return redirect('home')


# CART PAGE
def cart_view(request):

    cart = request.session.get('cart', {})

    cart_items = []

    total = 0

    for product_id, quantity in cart.items():

        try:
            product = Product.objects.get(
                id=int(product_id),
                status='approved'
            )

            subtotal = product.price * quantity

            total += subtotal

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })

        except Product.DoesNotExist:
            continue

    context = {
        'cart_items': cart_items,
        'total': total,
        'cart_count': get_cart_count(request),
    }

    return render(
        request,
        'cart.html',
        context
    )


# REMOVE PRODUCT FROM CART
def remove_from_cart(request, product_id):

    if request.method == 'POST':

        cart = request.session.get('cart', {})

        product_id = str(product_id)

        if product_id in cart:
            del cart[product_id]

        request.session['cart'] = cart

    return redirect('cart')