from django.contrib import admin
from .models import DonorProfile, BloodDrive, CampFunding

@admin.register(BloodDrive)
class BloodDriveAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date', 'target_units')
    list_filter = ('date', 'partner_hospital')
    search_fields = ('title', 'location')

@admin.register(DonorProfile)
class DonorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_type', 'is_eligible', 'last_donation_date')
    list_editable = ('is_eligible',) # Allows you to toggle eligibility from the list!