from rest_framework import serializers

from apps.profiles.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

class ProfileUpdateSerializer(serializers.ModelSerializer):
    blood_test_photo = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'gender', 'weight', 'height', 'allergy', 'blood_test_photo']

    def validate(self, data):
        request = self.context.get('request')
        if request and request.method == 'PUT':
            required_fields = ['date_of_birth', 'gender', 'weight', 'height', 'allergy']
            for field in required_fields:
                if field not in data:
                    raise serializers.ValidationError({field: "This field is required."})
        return data

    def update(self, instance, validated_data):
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.height = validated_data.get('height', instance.height)
        instance.allergy = validated_data.get('allergy', instance.allergy)

        blood_test_photo = validated_data.get('blood_test_photo')
        if blood_test_photo:
            instance.blood_test_info = self.process_blood_test_photo(blood_test_photo)

        instance.ideal_weight = self.calculate_ideal_weight(instance.height, instance.gender)
        instance.is_filled = True
        instance.save()
        return instance

    def process_blood_test_photo(self, photo):
        # Обработка фото и возврат результата в виде текста
        # Здесь нужно добавить вашу логику обработки фото
        return "Processed blood test info"

    def calculate_ideal_weight(self, height, gender):
        # Логика для расчета идеального веса
        if gender == Profile.GenderChoices.MALE:
            return height - 100
        else:
            return height - 110
