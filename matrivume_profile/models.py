from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver

User = get_user_model()

# Create your models here.
# Todo: To add ancestry app we will add (Father, Mother, GrandFather, ProGrandFather)
# Todo: To add an app for our team information
# Todo: To add app for Blogging
# Todo: To add app for Social Networking
# Todo: Instead of asking directly we will make feature like imei.info


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Identity(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name="identity_user")
    birth_date = models.DateField(null=True, blank=True)
    '''
    weight = models.PositiveSmallIntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    '''

    '''
    trade_license_number = models.CharField(max_length=255, null=True, blank=True)
    tax_identification_number = models.CharField(max_length=255, null=True, blank=True)
    student_id = models.CharField(max_length=255, null=True, blank=True)
    '''

    '''
    passport_number = models.CharField(max_length=255, null=True, blank=True)
    national_identity = models.CharField(max_length=255, null=True, blank=True)
    birth_certificate = models.CharField(max_length=255, null=True, blank=True)
    cell_phone_number = models.CharField(max_length=50, null=True, blank=True)
    '''

    github_profile_link = models.URLField(null=True, blank=True)
    bio = models.TextField(default="No bio")
    # profile_picture = models.ImageField(upload_to='') when we make login system we will make it

    # cell_phone_imei_code = models.CharField(max_length=50, null=True, blank=True)

    # education_profile = we will add educational profile :)
    # address = we are going use the google's maps API :)

    def __str__(self):
        return self.user_profile.username
