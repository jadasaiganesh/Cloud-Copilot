from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),  # <-- Add this line
    path('services/', views.services_view, name='services'),
    path('about/', views.about_view, name='about'),    
    path('lambda/', views.lambda_view, name='lambda'),
    path('ec2/', views.ec2_view, name='ec2'),
    path('s3/', views.s3_view, name='s3'),
    path('rds/', views.rds_view, name='rds'),
    path('dynamodb/', views.dynamodb_view, name='dynamodb'),
    path('vpc/', views.vpc_view, name='vpc'),
    path('iam/', views.iam_view, name='iam'),
    path('cloudtrail/', views.cloudtrail_view, name='cloudtrail'),
    path('cloudfront/', views.cloudfront_view, name='cloudfront'),
    path('sqs/', views.sqs_view, name='sqs'),
    path('sns/', views.sns_view, name='sns'),
    path('aurora/', views.aurora_view, name='aurora'),
    path('ebs/', views.ebs_view, name='ebs'),
    path('cloudwatch/', views.cloudwatch_view, name='cloudwatch'),
    path('route53/', views.route53_view, name='route53'),
    path('codepipeline/', views.codepipeline_view, name='codepipeline'),
    path('stepfunctions/', views.stepfunctions_view, name='stepfunctions'),
    path('appsync/', views.appsync_view, name='appsync'),
    path('kms/', views.kms_view, name='kms'),
    path('sagemaker/', views.sagemaker_view, name='sagemaker'),
    path('rekognition/', views.rekognition_view, name='rekognition'),


]
