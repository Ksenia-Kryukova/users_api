from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(min_value=16, max_value=99)
    job = serializers.CharField(required=False, default="Безработный(ая)")

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'age', 'job']

    def validate(self, data):
        if data['age'] < 16 or data['age'] > 99:
            raise ValidationError("Возраст должен быть между 16 и 99.")
        return data

    def create(self, validated_data):
        if 'job' not in validated_data or not validated_data['job'].strip():
            validated_data['job'] = "Безработный(ая)"
        return super().create(validated_data)
