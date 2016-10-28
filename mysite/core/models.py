from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, _, PermissionsMixin
from django.db.models import ForeignKey

from .ModelHelper import MemberProfile, FoodHelper


class MemberManager(UserManager):
    pass


class Member(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'),
                              unique=True,
                              error_messages={
                                  'unique': _("A user with that email already exists."),
                              })

    name = models.CharField(_('name'), max_length=30)

    address = models.CharField(_('address'), max_length=200)
    type_of_food = models.CharField(max_length=1, choices=(
        ('T', 'Traditional'), ('F', 'Fast Food'), ('B', 'Traditional and Fast Food')))
    phone_numbers = models.CharField(max_length=11)
    brand_photo = models.ImageField(upload_to='images/')

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))

    objects = MemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',
                       'address', 'type_of_food',
                       'phone_numbers']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def get_profile(self):
        return MemberProfile(str(self.name), str(self.address), str(self.phone_numbers),
                             str(self.brand_photo), self.pk)

    def __str__(self):
        return self.name


class Food(models.Model):
    restaurant = ForeignKey(Member)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    food_photo = models.ImageField(upload_to='images/')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'title' in kwargs:
            self.title = kwargs['title']
            self.price = kwargs['price']
            self.description = kwargs['description']
            self.food_photo = kwargs['food_photo']

    def get_food(self):
        return FoodHelper(str(self.title), str(self.price),
                          str(self.description), str(self.food_photo))

    def __str__(self):
        return self.title


class OnlineOrder(models.Model):
    restaurant = ForeignKey(Member)
    foods = JSONField('')
    total_price = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(auto_now_add=True)
    estimated_time = models.IntegerField(blank=True)
    customer = models.CharField(max_length=50)  # we just maintain an username
    handled = models.BooleanField(default=False)  # default = false && just for double check

    def __str__(self):
        return self.customer


class OfflineOrder(models.Model):
    restaurant = ForeignKey(Member)
    foods = JSONField('')
    order_date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(auto_now_add=True)
    estimated_time = models.IntegerField()
    pending_time = models.IntegerField(blank=True)
    customer = models.CharField(max_length=50)
    rating = models.FloatField(null=True)

    def __str__(self):
        return self.order_date
