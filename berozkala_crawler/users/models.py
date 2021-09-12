from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError(_('Users must have a phone_number'))

        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password=None):
        if not password:
            raise TypeError(_('Password must be set'))

        user = self.create_user(phone_number, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None

    phone_number_validator = RegexValidator(r'^(\+98|0)?9\d{9}$', message=_('Invalid phone number'))

    phone_number = models.PositiveBigIntegerField(_('phone number'), unique=True, validators=[phone_number_validator])
    first_name = models.CharField(_('first name'), max_length=100, blank=True, null=False)
    last_name = models.CharField(_('last name'), max_length=100, blank=True, null=False)
    is_active = models.BooleanField(_('is active'), default=True)
    is_verified = models.BooleanField(_('is verified'), default=True)
    is_staff = models.BooleanField(_('is staff'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    USERNAME_FIELD = 'phone_number'
    

    objects = UserManager()

    def __str__(self):
        return self.phone_number
        

    class Meta:
        db_table = 'user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    
