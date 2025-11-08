import secrets
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core import signing
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Service, ServiceBooking
from .models import Order
import requests
from django.core.mail import send_mail
from django.conf import settings

# --------------------------------------
# TOKEN HANDLER
# --------------------------------------
def get_or_create_token(request, section_name):
    """Generate or retrieve a short, session-tied token."""
    if not request.session.session_key:
        request.session.create()

    if 'short_token' not in request.session:
        short_token = secrets.token_urlsafe(12)
        request.session['short_token'] = short_token

    token = request.session['short_token']

    payload = {
        'session_key': request.session.session_key,
        'section': section_name,
        'user_type': 'guest',
    }
    signed = signing.dumps(payload)
    request.session[f'token_data_{token}'] = signed
    return token


def verify_token(request, token):
    """Check token validity."""
    signed = request.session.get(f'token_data_{token}')
    if not signed:
        return None

    try:
        decoded = signing.loads(signed, max_age=3600)
    except (signing.BadSignature, signing.SignatureExpired):
        return None

    if decoded.get('session_key') != request.session.session_key:
        return None
    return decoded


# --------------------------------------
# STATIC PAGES
# --------------------------------------
def homepage(request):
    return render(request, 'homepage/home.html')


def about_entry(request):
    token = get_or_create_token(request, 'about-section')
    return redirect('about_detail', token=token)


def about_detail(request, token):
    if not verify_token(request, token):
        return render(request, '404.html', {'error': 'Invalid token'}, status=404)
    return render(request, 'homepage/about.html')


def reviews_entry(request):
    token = get_or_create_token(request, 'review-section')
    return redirect('reviews_detail', token=token)


def reviews_detail(request, token):
    if not verify_token(request, token):
        return render(request, '404.html', {'error': 'Invalid token'}, status=404)
    return render(request, 'homepage/reviews.html')


def careers_entry(request):
    token = get_or_create_token(request, 'careers-section')
    return redirect('careers_detail', token=token)


def careers_detail(request, token):
    if not verify_token(request, token):
        return render(request, '404.html', {'error': 'Invalid token'}, status=404)
    return render(request, 'homepage/careers.html')


def know_more_entry(request):
    token = get_or_create_token(request, 'know_more-section')
    return redirect('know_more_detail', token=token)


def know_more_detail(request, token):
    if not verify_token(request, token):
        return render(request, '404.html', {'error': 'Invalid token'}, status=404)
    return render(request, 'homepage/know_more.html')


# --------------------------------------
# SERVICES SECTION
# --------------------------------------
def services_entry(request):
    token = get_or_create_token(request, 'services-section')
    return redirect('services_detail', token=token)


def services_detail(request, token):
    if not verify_token(request, token):
        return render(request, '404.html', {'error': 'Invalid token'}, status=404)
    services = Service.objects.all() #fetches all services from the database
    return render(request, 'homepage/services.html', {'services': services})


# --------------------------------------
# ECITIZEN SERVICES (FULL 18 ITEMS)
# --------------------------------------
def ecitizen_entry(request):
    token = get_or_create_token(request, 'ecitizen-section')
    return redirect('ecitizen_detail', token=token)


def ecitizen_detail(request, token):
    if not verify_token(request, token):
        return render(request, '404.html', {'error': 'Invalid token'}, status=404)

    # Use the global ECITIZEN_SERVICES
    return render(request, "homepage/ecitizen_detail.html", {"services": ECITIZEN_SERVICES, "token": token})

ECITIZEN_SERVICES = [
    {"id": 1, "name": "eCitizen Account Sign-Up", "description": "Assistance with new eCitizen account registration and login issues.", "image": "ecitizen.png", "slug": "ecitizen_account", "price": 100},
    {"id": 2, "name": "Change Phone Number", "description": "Change your lost eCitizen account phone number easily with us.", "image": "change_phoneno.png", "slug": "change_phoneno","price": 300,},
    {"id": 3, "name": "Good Conduct Certificate", "description": "Get assistance with a Good Conduct Certificate application and renewals.", "image": "goodconductcert.png", "slug": "good_conduct_certificate", "price": 200,},
    {"id": 4, "name": "Migration Application", "description": "Get assistance with Passport & Visa Applications.", "image": "migration.png", "slug": "migration", "price": 500,},
    {"id": 5, "name": "Temporary Passport Application", "description": "Visit EAC with your temporary passport permit.", "image": "temporary_passport.png", "slug": "temporary_pass", "price": 300,},
    {"id": 6, "name": "ID Application", "description": "Replace your lost National ID card free with our assistance.", "image": "id_application.png", "slug": "id_application", "price": 250,},
    {"id": 7, "name": "Birth Certificate Application", "description": "Get assistance with all related Civil registration Services.", "image": "birtcert.png", "slug": "birth_certificate", "price": 150,},
    {"id": 8, "name": "Death Certificate Application", "description": "Also apply for new/replacement Death certificate online.", "image": "deatcert.png", "slug": "death_certificate", "price": 150,},
    {"id": 9, "name": "Marriage Registration", "description": "We assist you with Civil marriage Registration.", "image": "marriage_certi.png", "slug": "marriage_registration", "price": 200,},
    {"id": 10, "name": "Business Name Registration", "description": "Register your Business/Company Name with our online platform.", "image": "Business_Reg.png", "slug": "business_registration", "price": 300,},
    {"id": 11, "name": "Certificate of Incorporation", "description": "Get assistance with obtaining a Certificate of Incorporation.", "image": "cert_incoporation.png", "slug": "certificate_of_incorporation", "price": 300,},
    {"id": 12, "name": "Partnership Business Registration", "description": "Register your Partnership Business with our online assistance.", "image": "business_registration.png", "slug": "partnership_business_registration", "price": 350,},
    {"id": 13, "name": "Private Company Registration", "description": "Register your Private Company (Cr12, Cr13) from our eCitizen dashboard.", "image": "private_company.png", "slug": "private_company_registration", "price": 450,},
    {"id": 14, "name": "Company Name Search", "description": "Search for your desired business name availability with us.", "image": "name_search.png", "slug": "name_search", "price": 150,},
    {"id": 15, "name": "Court E-Filing", "description": "We assist you with online Judiciary e-filing services including case tracking & court fee payments.", "image": "e-filling.png", "slug": "court_e_filling", "price": 200,},
    {"id": 16, "name": "Affordable Housing Application", "description": "We assist you in making booking application for the affordable housing program through our platform.", "image": "affordable_housing.png", "slug": "affordable_housing_1450", "price": 300,},
    {"id": 17, "name": "Diaspora Affairs (Authentication Certificate)", "description": "Get assistance with Diaspora Affairs Authentication Certificate application for legal document approvals with us.", "image": "diaspora_affairs.png", "slug": "diaspora_affairs", "price": 200,},
    {"id": 18, "name": "Business Permit Application", "description": "At CyberConnect we help you apply for your business license instantly.", "image": "business_perm.png", "slug": "business_permit", "price": 500,},
 ]

    


# --------------------------------------
# SERVICE DETAIL / ADD TO CART
# It finds the selected service (from either your database or your ECITIZEN_SERVICES list), then adds it to the cart stored in the user’s session.
# Its core function that handles all services requested iby user, be it in KRA , ecitizen or other dashboard.
# --------------------------------------
def service_detail(request, service_id):
    access = request.GET.get("access")

    if access:
        service_data = next((s for s in ECITIZEN_SERVICES if str(s["id"]) == str(service_id)), None)
        if not service_data:
            raise Http404("Service not found")
    else:
        service = get_object_or_404(Service, id=service_id)
        service_data = {
            "id": service.id,
            "name": service.name,
            "description": service.description,
            "price": service.price,
            "image": service.image.url if service.image else 'static/default.png'
        }

    # ✅ Add to the using the same session-based cart structure
    cart = request.session.get('cart', {})

    if str(service_data['id']) not in cart:
        cart[str(service_data['id'])] = {
            'name': service_data['name'],
            'price': float(service_data.get('price', 0)),
            'quantity': 1,
            'image': service_data['image'],
            'description': service_data['description']
        }
    request.session['cart'] = cart
    request.session.modified = True

    messages.success(request, f"{service_data['name']} added to cart!")
    
    # Redirect to booking page first instead of cart
    return render(request, 'homepage/book_service.html', {'service': service_data, 'cart_items': cart})

# --------------------------------------
# CART VIEWS
# --------------------------------------
def view_cart(request):
    cart = request.session.get("cart", {})

    subtotal = sum(float(item["price"]) * int(item["quantity"]) for item in cart.values())
    total = subtotal

    return render(request, "homepage/view_cart.html", {
        "cart": cart,   # ✅ matches your template’s `{% for key, item in cart.items %}`
        "subtotal": round(subtotal, 2),
        "total": round(total, 2),
    })


@csrf_exempt
def update_cart(request, service_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        cart = request.session.get("cart", {})
        if str(service_id) in cart:
            cart[str(service_id)]["quantity"] = quantity
            request.session["cart"] = cart
            request.session.modified = True

            subtotal = sum(float(i["price"]) * int(i["quantity"]) for i in cart.values())
            item_total = float(cart[str(service_id)]["price"]) * quantity
            return JsonResponse({
                "success": True,
                "item_total": f"{item_total:.2f}",
                "cart_total": f"{subtotal:.2f}",
            })
    return JsonResponse({"success": False})


@csrf_exempt
def remove_from_cart(request, service_id):
    if request.method == "POST":
        cart = request.session.get("cart", {})
        if str(service_id) in cart:
            del cart[str(service_id)]
            request.session["cart"] = cart
            request.session.modified = True

            subtotal = sum(float(i["price"]) * int(i["quantity"]) for i in cart.values())
            return JsonResponse({
                "success": True,
                "cart_total": f"{subtotal:.2f}",
            })
    return JsonResponse({"success": False})




# --------------------------------------
# CHECKOUT
# --------------------------------------
def checkout_view(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect("view_cart")

    subtotal = sum(float(item["price"]) * int(item["quantity"]) for item in cart.values())
    total = subtotal  # Add shipping later if needed

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        city = request.POST.get("city")
        country = request.POST.get("country")
        notes = request.POST.get("notes")

        # Save order
        order = Order.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            city=city,
            country=country,
            notes=notes,
            subtotal=subtotal,
            total=total,
        )

        # Email alert
        send_mail(
            subject=f"🛍️ New Order from {first_name} {last_name}",
            message=f"New order placed.\nName: {first_name} {last_name}\nPhone: {phone}\nTotal: KSh {total}\nNotes: {notes}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
        )

        # WhatsApp alert (via CallMeBot or Twilio)
        try:
            requests.get(
                f"https://api.callmebot.com/whatsapp.php?phone=+254YOURNUMBER&text=New+Order:+{first_name}+{last_name}+Total+KSh+{total}&apikey=YOUR_API_KEY"
            )
        except:
            pass

        messages.success(request, "Your order has been placed successfully!")
        request.session["cart"] = {}  # Clear cart
        return redirect("order_success")

    return render(request, "homepage/checkout.html", {
        "cart": cart,
        "subtotal": subtotal,
        "total": total,
    })


# --------------------------------------
# BOOK SERVICE
# --------------------------------------
def book_service(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
        service_name = service.name
    except Service.DoesNotExist:
        service_name = request.GET.get("access", "Unknown Service").replace("_", " ").title()
        booking = ServiceBooking.objects.create(
            service_name=service_name,
            full_name="Guest User",
            phone_number="Not Provided",
            transaction_code="Pending",
        )
    else:
        booking = ServiceBooking.objects.create(
            service=service,
            full_name="Guest User",
            phone_number="Not Provided",
            transaction_code="Pending",
        )

    return redirect("https://forms.gle/your_google_form_id_here")
