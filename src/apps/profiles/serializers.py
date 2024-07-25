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
        fields = ['date_of_birth', 'gender', 'weight', 'height', 'ideal_weight', 'target', 'allergy', 'blood_test_photo', 'injuries', 'time_limit']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'blood_test_photo' and value:
                instance.blood_test_info = self.process_blood_test_photo(value)
            else:
                setattr(instance, attr, value)
        
        instance.save()
        return instance

    def process_blood_test_photo(self, photo):
        # Обработка фото и возврат результата в виде текста
        # Здесь нужно добавить вашу логику обработки фото
        return "Processed blood test info"
