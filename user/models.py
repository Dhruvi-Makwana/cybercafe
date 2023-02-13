from django.db import models
from django.contrib.auth.models import AbstractUser
from user.choice import SYSTEM_AVAILABILITY_CHOICES, RAM_UNITS


class User(AbstractUser):

    mobile_number = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)


class ConfigureSystems(models.Model):
    """
    Store the basic details about particular PC and Laptops.
    """
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    purchase_date = models.DateField(auto_now_add=True)
    ram = models.IntegerField()
    unit = models.CharField(choices=RAM_UNITS, max_length=20)

    class Meta:
        verbose_name = "ConfigureSystem"

    def __str__(self):
        return f'{self.name}'


class System(models.Model):
    """
    Store systems with AVAILABILITY data.
    """
    name = models.ForeignKey(ConfigureSystems, on_delete=models.CASCADE,
                             related_name="systems")
    status = models.CharField(choices=SYSTEM_AVAILABILITY_CHOICES, max_length=100)

    class Meta:
        verbose_name = "System"

    def __str__(self):
        return f' {self.name}'


class System_User_Histories(models.Model):
    """
    Store every user with his using system details.
    """
    system_user = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name="System_User_Histories")
    system = models.ForeignKey(System,
                               on_delete=models.CASCADE,
                               related_name="System_Histories")
    assign_time = models.DateTimeField(max_length=20)
    finish_time = models.DateTimeField(max_length=20)

    class Meta:
        verbose_name = "System_User_Historie"