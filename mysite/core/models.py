from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, _
from django.contrib.postgres.fields import JSONField
from django.utils import timezone


class MemberManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        now = timezone.now()

        if not email:
            raise ValueError('sishti Email')
        email = self.normalize_email(email)
        member = self.model(email=email,
                            date_joined=now,
                            **extra_fields)
        member.set_password(password)
        member.save(using=self._db)
        return member

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password,
                                 **extra_fields)


class Member(AbstractBaseUser):
    username = models.CharField(_('username'), max_length=30, unique=True,
                                help_text=_('Required. 30 characters or fewer. Letters, digits and '
                                            '-/./_ only.'),
                                validators=[
                                    validators.RegexValidator(r'^[\w.-]+$',
                                                              _('Enter a valid username. '
                                                                'This value may contain only letters, numbers '
                                                                'and -/./_ characters.'), 'invalid'),
                                ],
                                error_messages={
                                    'unique': _("A user with that username already exists."),
                                })
    email = models.EmailField(_('email address'), primary_key=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    foods = JSONField(default='')
    address = models.CharField(_('address'), max_length=200)
    type_of_food = models.CharField(max_length=1, choices=(
        ('T', 'Traditional'), ('F', 'Fast Food'), ('B', 'Traditional and Fast Food')))
    phone_numbers = models.CharField(max_length=11)

    objects = MemberManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name',
                       'address', 'type_of_food',
                       'phone_numbers']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name
