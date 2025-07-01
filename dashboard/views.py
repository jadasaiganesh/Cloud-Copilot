from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import Profile  # Make sure this is in your models.py

@login_required
def home_view(request):
    return render(request, 'dashboard/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Assumes you have a login page with name='login'

@login_required
def profile_view(request):
    user = request.user
    pwd_form = PasswordChangeForm(user)

    if request.method == 'POST':
        if 'update_email' in request.POST:
            user.email = request.POST.get('email')
            user.save()
            messages.success(request, 'Email updated successfully.')
            return redirect('profile')

        elif 'change_password' in request.POST:
            pwd_form = PasswordChangeForm(user, request.POST)
            if pwd_form.is_valid():
                pwd_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully.')
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the errors below.')

    last_login_date = user.last_login.date() if user.last_login else "N/A"

    return render(request, 'dashboard/profile.html', {
        'user': user,
        'pwd_form': pwd_form,
        'last_login_date': last_login_date,
    })

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def services_view(request):
    return render(request, 'dashboard/services.html')

from django.shortcuts import render

def about_view(request):
    return render(request, 'dashboard/about.html')
from django.shortcuts import render, get_object_or_404
from .models import Service  # We'll define this model below
from django.shortcuts import render



# dashboard/views.py

from django.shortcuts import render

def lambda_view(request):
    return render(request, 'dashboard/lambda.html')

def ec2_view(request):
    return render(request, 'dashboard/ec2.html')

def s3_view(request):
    return render(request, 'dashboard/s3.html')

def rds_view(request):
    return render(request, 'dashboard/rds.html')

def dynamodb_view(request):
    return render(request, 'dashboard/dynamodb.html')

def vpc_view(request):
    return render(request, 'dashboard/vpc.html')

def iam_view(request):
    return render(request, 'dashboard/iam.html')

def cloudtrail_view(request):
    return render(request, 'dashboard/cloudtrail.html')

def cloudfront_view(request):
    return render(request, 'dashboard/cloudfront.html')

def sqs_view(request):
    return render(request, 'dashboard/sqs.html')

def sns_view(request):
    return render(request, 'dashboard/sns.html')

def aurora_view(request):
    return render(request, 'dashboard/aurora.html')

def ebs_view(request):
    return render(request, 'dashboard/ebs.html')

def cloudwatch_view(request):
    return render(request, 'dashboard/cloudwatch.html')

def route53_view(request):
    return render(request, 'dashboard/route53.html')

def codepipeline_view(request):
    return render(request, 'dashboard/codepipeline.html')

def stepfunctions_view(request):
    return render(request, 'dashboard/stepfunctions.html')

def appsync_view(request):
    return render(request, 'dashboard/appsync.html')

def kms_view(request):
    return render(request, 'dashboard/kms.html')

def sagemaker_view(request):
    return render(request, 'dashboard/sagemaker.html')

def rekognition_view(request):
    return render(request, 'dashboard/rekognition.html')
