from django.db import models
from django.contrib.auth.models import AbstractUser


class Organisation(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Organisation"
        verbose_name_plural = "Organisations"

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    class Roles(models.TextChoices):
        ORG_OWNER = "owner", "Organisation Owner"
        ORG_ADMIN = "admin", "Organisation Admin"
        ORG_USER = "user", "Standard User"

    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        related_name="users",
        null=True,
        blank=True,
    )
    role = models.CharField(
        max_length=16,
        choices=Roles.choices,
        default=Roles.ORG_USER,
    )


    def __str__(self) -> str:
        if self.organisation:
            return f"{self.username} ({self.organisation.name})"
        return self.username
