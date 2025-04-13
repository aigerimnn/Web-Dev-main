from rest_framework import serializers

from .models import Company, Vacancy


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    city = serializers.CharField(max_length=255)
    address = serializers.CharField()

    def create(self, validated_data):
        instance = Company.objects.create(
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            city=validated_data.get('city'),
            address=validated_data.get('address')
        )

        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)

        instance.save()

        return instance

    def delete(self, instance):
        instance.delete()


class VacancySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    salary = serializers.FloatField(allow_null=False)
    company = CompanySerializer()

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company')
