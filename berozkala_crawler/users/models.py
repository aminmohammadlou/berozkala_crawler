from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(_('age'))

    phone_number_validator = RegexValidator(r'^(\+98|0)?9\d{9}$', message=_('Invalid phone number'))

    phone_number = models.PositiveBigIntegerField(_('phone number'), unique=True, validators=[phone_number_validator])
    email = models.EmailField(_('email'), blank=True, unique=True)
    bio = models.TextField(_('bio'), blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='avatars', blank=True, null=True)

    class Meta:
        db_table = 'profile'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f'id: {self.user.id} username: {self.user.username}'