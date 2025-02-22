from django.core.validators import RegexValidator, validate_ipv4_address
from django.core.exceptions import ValidationError
from django.db import models


class React(models.Model):
    DOMAIN_REGEX = r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'

    DomainName = models.CharField(
        max_length=35,
        default='google.com',
        validators=[
            RegexValidator(
                DOMAIN_REGEX,
                "Enter a valid domain name (e.g., example.com)."
            )
        ]
    )
    IPAddress = models.GenericIPAddressField(
        protocol='IPv4',
        default='192.168.1.2',
        validators=[validate_ipv4_address]
    )
    Class = models.CharField(
        max_length=1,
        default='A',
        choices=[
            ('A', 'Class A'),
            ('B', 'Class B'),
            ('C', 'Class C')
        ]
    )

    def clean(self):
        super().clean()

        try:
            ip_first_octet = int(self.IPAddress.split('.')[0])
        except (ValueError, AttributeError):
            raise ValidationError("Enter a valid IPv4 address.")

        if 1 <= ip_first_octet <= 126 and self.Class != 'A':
            raise ValidationError("IP address suggests Class A, but selected class is not A.")
        elif 128 <= ip_first_octet <= 191 and self.Class != 'B':
            raise ValidationError("IP address suggests Class B, but selected class is not B.")
        elif 192 <= ip_first_octet <= 223 and self.Class != 'C':
            raise ValidationError("IP address suggests Class C, but selected class is not C.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.DomainName} ({self.IPAddress}, {self.Class})"

