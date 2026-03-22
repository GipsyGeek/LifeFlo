from rest_framework import serializers
from .models import DonorProfile, BloodDrive, CampFunding

class BloodDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodDrive
        fields = '__all__'

class DonorProfileSerializer(serializers.ModelSerializer):
    # We include the username from the User model for convenience
    username = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = DonorProfile
        fields = ['username', 'blood_type', 'weight_kg', 'last_donation_date', 'is_eligible']