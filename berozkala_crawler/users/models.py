from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, phone_number, password, **kwargs):

        if not phone_number:
            raise ValueError('The given phone number must be set')
        user = self.model(phone_number=phone_number, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **kwargs):
        kwargs.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **kwargs)

    def create_superuser(self, phone_number, password, **kwargs):
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, password, **kwargs)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None

    phone_number_validator = RegexValidator(r'^(\+98|0)?9\d{9}$', message=_('Invalid phone number'))

    phone_number = models.PositiveBigIntegerField(_('phone number'), unique=True, validators=[phone_number_validator])
    first_name = models.CharField(_('first name'), max_length=100, blank=True, null=False)
    last_name = models.CharField(_('last name'), max_length=100, blank=True, null=False)

    USERNAME_FIELD = 'phone_number'

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f'phone number: {self.phone_number} - first name: {self.first_name} - last name: {self.last_name}'
