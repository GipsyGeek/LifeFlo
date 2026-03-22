from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import DonorProfile, BloodDrive
from .serializers import BloodDriveSerializer, DonorProfileSerializer

# 1. Standard Django View for the Eligibility Quiz
def eligibility_quiz(request):
    """
    Handles the logic for checking student donation eligibility.
    Currently accepts weight as a POST parameter.
    """
    if request.method == "POST":
        # Using .get() with a default of 0 to prevent errors if weight is missing
        try:
            weight = float(request.POST.get('weight', 0))
        except ValueError:
            return JsonResponse({"status": "error", "message": "Invalid weight value."}, status=400)

        if weight >= 50:
            return JsonResponse({
                "status": "success", 
                "message": "You are eligible! Your contribution makes a difference."
            })
        else:
            return JsonResponse({
                "status": "error", 
                "message": "Weight too low. You must be at least 50kg to donate safely."
            })
            
    return JsonResponse({"message": "Please send a POST request with 'weight' to check eligibility."})


# 2. Django REST Framework ViewSets for the API
class BloodDriveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Blood Drives to be viewed or edited.
    Sorted by date (newest first).
    """
    queryset = BloodDrive.objects.all().order_by('-date')
    serializer_class = BloodDriveSerializer


class DonorProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and managing Donor Profiles.
    """
    queryset = DonorProfile.objects.all()
    serializer_class = DonorProfileSerializer