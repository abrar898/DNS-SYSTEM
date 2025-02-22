from rest_framework import serializers
from .models import React
import re


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['DomainName', 'IPAddress', 'Class']

    def validate_DomainName(self, value):
        """Validate domain name format."""
        domain_regex = r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
        if not re.match(domain_regex, value):
            raise serializers.ValidationError("Enter a valid domain name (e.g., example.com).")
        return value

    def validate_IPAddress(self, value):
        """Validate IPv4 address."""
        try:
            octets = value.split('.')
            if len(octets) != 4 or not all(0 <= int(octet) <= 255 for octet in octets):
                raise ValueError
        except (ValueError, AttributeError):
            raise serializers.ValidationError("Enter a valid IPv4 address.")
        return value

    def validate(self, data):
        """Validate the relationship between IP address and Class."""
        ip_first_octet = int(data['IPAddress'].split('.')[0])
        ip_class = data['Class']

        if 1 <= ip_first_octet <= 126 and ip_class != 'A':
            raise serializers.ValidationError("IP address suggests Class A, but selected class is not A.")
        elif 128 <= ip_first_octet <= 191 and ip_class != 'B':
            raise serializers.ValidationError("IP address suggests Class B, but selected class is not B.")
        elif 192 <= ip_first_octet <= 223 and ip_class != 'C':
            raise serializers.ValidationError("IP address suggests Class C, but selected class is not C.")

        return data
