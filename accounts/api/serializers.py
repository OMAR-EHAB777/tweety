from rest_framework import serializers
from accounts.models import customuser


class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = customuser
        fields = ["username"]