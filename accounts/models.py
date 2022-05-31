from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, name=None, full_name=None,
                    is_active=True, is_staff=None, is_admin=None):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("Пользователь должен иметь адрес электронной почты")
        elif not password:
            raise ValueError("Пользователь должен ввести пароль")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, full_name=full_name)

        user.password = make_password(password)
        user.is_active = is_active
        user.admin = is_admin
        user.staff = is_staff
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, name=None):
        user = self.create_user(email, password, name, is_staff=True, is_admin=True)
        return user

    def create_staffuser(self, email, password=None, name=None):
        user = self.create_user(email, password, name, is_staff=True)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        if self.name:
            return self.name
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.is_admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    def save(self, *args, **kwargs):
        if not self.id and not self.is_admin and not self.is_staff:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
