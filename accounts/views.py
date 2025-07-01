from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
import random

# In-memory store for OTPs
otp_storage = {}

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # Make sure 'home' is defined in urls.py
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
    return render(request, 'accounts/register.html')

from django.core.mail import send_mail
from django.contrib import messages
import random

def forgot_password_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        print(f"Email submitted: {email}")  # debug print

        user = User.objects.filter(email=email).first()
        if user:
            otp = str(random.randint(100000, 999999))
            otp_storage[email] = otp
            print(f"Generated OTP: {otp}")  # debug print

            # Professional email content
            subject = 'CloudCopilot OTP for Password Reset'
            message = f"""
Dear {user.username},

Your One-Time Password (OTP) for resetting your CloudCopilot password is:

{otp}

Please enter this OTP on the verification page to proceed.

⚠️ This OTP is valid for 10 minutes. Do not share it with anyone.

Thank you for using CloudCopilot.
— The CloudCopilot Team
            """

            try:
                send_mail(
                    subject=subject,
                    message=message.strip(),  # Strip leading spaces from multiline string
                    from_email='CloudCopilot <saiganeshreddy0311@gmail.com>',
                    recipient_list=[email],
                    fail_silently=False,
                )
                request.session['reset_email'] = email
                messages.success(request, f"OTP sent to {email}. Please check your inbox.")
                return redirect('otp_verify')
            except Exception as e:
                print("Email send error:", e)
                messages.error(request, "Failed to send OTP. Please try again later.")
        else:
            messages.error(request, "Email not found.")
    return render(request, 'accounts/forgot_password.html')




def otp_verify_view(request):
    email = request.session.get('reset_email')
    if not email:
        return redirect('forgot_password')

    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if entered_otp == otp_storage.get(email):
            if new_password == confirm_password:
                user = User.objects.filter(email=email).first()
                user.password = make_password(new_password)
                user.save()
                otp_storage.pop(email, None)
                messages.success(request, "Password reset successful. Please log in.")
                return redirect('login')
            else:
                messages.error(request, "Passwords do not match.")
        else:
            messages.error(request, "Invalid OTP.")
    return render(request, 'accounts/otp_verify.html')
