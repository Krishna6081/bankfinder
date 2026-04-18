from django.core.validators import RegexValidator
from django.db import models


class Branch(models.Model):
    branch_name = models.CharField(max_length=255)
    contact_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\d{10}$",
                message="Enter a 10-digit phone number using digits only.",
            )
        ],
    )
    address = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["branch_name"]
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.branch_name
