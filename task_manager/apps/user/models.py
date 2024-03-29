from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator
from django.db import models


# TODO: add fields 'first_name' and 'last_name' as required for registration [??]

class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    email_validator = EmailValidator()
    username = models.CharField(verbose_name='username',
                                max_length=150,
                                unique=True,
                                help_text='Your username must be unique',
                                validators=[
                                    username_validator,
                                ],
                                error_messages={
                                    'unique': 'A user with that username already exists.',
                                })
    email = models.CharField(verbose_name='email',
                             max_length=150,
                             unique=True,
                             help_text='Your email must exists and be unique.',
                             validators=[
                                 email_validator,
                             ],
                             error_messages={
                                 'unique': 'A user with that email already exists.',
                             })
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.get_full_name() or f'@{self.username}'

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
