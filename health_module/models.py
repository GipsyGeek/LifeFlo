from django.db import models
from django.contrib.auth.models import User

class DonorProfile(models.Model):
    BLOOD_TYPES = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    last_donation_date = models.DateField(null=True, blank=True)
    is_eligible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.blood_type}"
    def check_eligibility(self):
        """
        Returns a tuple: (Boolean, String Message)
        """
        # 1. Check Weight (Standard is usually 50kg+)
        if self.weight_kg < 50:
            return False, "You must weigh at least 50kg to donate safely."

        # 2. Check Last Donation (Must wait 90 days / 3 months)
        if self.last_donation_date:
            three_months_ago = date.today() - timedelta(days=90)
            if self.last_donation_date > three_months_ago:
                days_to_wait = (self.last_donation_date + timedelta(days=90)) - date.today()
                return False, f"Please wait {days_to_wait.days} more days before your next donation."

        return True, "You are eligible to donate! Check out upcoming blood drives."

class BloodDrive(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    target_units = models.IntegerField()
    partner_hospital = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class CampFunding(models.Model):
    camp_name = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.camp_name