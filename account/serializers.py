from rest_framework import serializers
from .models import UserAccount


class UserRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'
        # extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = UserAccount.objects.create_user(**validated_data)
        return user