from django.db import models
from django.conf import settings
from accounts.models import Organisation


class Learner(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        TERMINATED = "TERMINATED", "Terminated"
        ON_LEAVE = "ON_LEAVE", "On leave"

    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        related_name="learners",
    )

    external_id = models.CharField(
        max_length=128,
        blank=True,
        help_text="Optional ID from HRIS/Payroll/Source system used for mapping.",
    )

    email = models.EmailField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)

    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    start_date = models.DateField(null=True, blank=True)
    job_title = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ("organisation", "email"),
        )
        verbose_name = "Learner"
        verbose_name_plural = "Learners"

    def __str__(self) -> str:
        return f"{self.email} ({self.organisation.name})"
