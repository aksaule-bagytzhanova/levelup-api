class ChatGPTRequestTemplate:
    @staticmethod
    def generate_request(profile, suggestion_type):
        if suggestion_type == 'nutritionist':
            prompt = f"Сгенерируй рацион питания для сброса веса используя мои данные:\n" \
                    f"Пол: {profile.get_gender_display()}\n" \
                    f"Возраст: {profile.get_age()}\n" \
                    f"Вес: {profile.weight} кг\n" \
                    f"Рост: {profile.height} см\n" \
                    f"Идеальный вес: {profile.ideal_weight} кг\n" \
                    f"Цель: {profile.get_target_display()}\n" \
                    f"Аллергии: {profile.allergy if profile.allergy else 'Нет'}\n"
        elif suggestion_type == 'dietitian':
            prompt = f"Создай детальный план питания для достижения моего идеального веса. Вот мои данные:\n" \
                    f"Пол: {profile.get_gender_display()}\n" \
                    f"Возраст: {profile.get_age()}\n" \
                    f"Вес: {profile.weight} кг\n" \
                    f"Рост: {profile.height} см\n" \
                    f"Идеальный вес: {profile.ideal_weight} кг\n" \
                    f"Цель: {profile.get_target_display()}\n" \
                    f"Аллергии: {profile.allergy if profile.allergy else 'Нет'}\n"
        elif suggestion_type == 'fitness':
            prompt = f"Предложи план фитнес тренировок для достижения моих целей. Вот мои данные:\n" \
                    f"Пол: {profile.get_gender_display()}\n" \
                    f"Возраст: {profile.get_age()}\n" \
                    f"Вес: {profile.weight} кг\n" \
                    f"Рост: {profile.height} см\n" \
                    f"Идеальный вес: {profile.ideal_weight} кг\n" \
                    f"Цель: {profile.get_target_display()}\n" \
                    f"Аллергии: {profile.allergy if profile.allergy else 'Нет'}\n"
        else:
            prompt = "Нет доступных предложений для выбранного типа."
        
        return prompt