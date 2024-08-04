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
    


class ChatGPTRecommendationRequestTemplate:
    @staticmethod
    def generate_request(profile):
        prompt = f"Сделай мне план питания от нутрициолога:" \
                f"Вот мои данные:" \
                f"дата рождения: {profile.date_of_birth}," \
                f"рост: {profile.height}," \
                f"вес: {profile.weight}," \
                f"цель веса: {profile.ideal_weight}," \
                f"цель: {profile.get_target_display()}," \
                f"аллергии: {profile.allergy if profile.allergy else 'Нет'}," \
                f"все должно быть на казахском языке кроме ключевых слов json." \
                f"Ответь строго в таком формате без других слов:" \
                "{'breakfast': {'title': 'тут название','description': 'тут инфо про калории\n жиры\n белок\n углеводы','recipe': 'тут инфо про состав с заголовками и рецепт учитывай количество и пиши на разные линии'},'lunch': {'title': 'тут название','description': 'тут инфо про калории\n жиры\n белок\n углеводы','recipe': 'тут инфо про состав с заголовками и рецепт учитывай количество и пиши на разные линии'},'dinner': {'title': 'тут название','description': 'тут инфо про калории\n жиры\n белок\n углеводы','recipe': 'тут инфо про состав с заголовками и рецепт учитывай количество и пиши на разные линии'}}"

        return prompt


class ChatGPTProfileSportRequestTemplate:
    @staticmethod
    def generate_request(profile):
        prompt = f"Сделай мне список тренировок от фитнес инструктора:" \
                f"Вот мои данные:" \
                f"дата рождения: {profile.date_of_birth}" \
                f"рост: {profile.height}" \
                f"вес: {profile.weight}" \
                f"цель веса: {profile.ideal_weight}" \
                f"цель: {profile.get_target_display()}" \
                f"аллергии: {profile.allergy if profile.allergy else 'Нет'}" \
                f"мои травмы: {profile.injuries if profile.injuries else 'Нет'}" \
                f"хочу добиться за срок: {profile.get_time_limit_display}." \
                f"по каждому типу нужно 3 упражений." \
                f"title и description должны быть на русском языке." \
                f"ответь строго в таком формате без других слов:" \
                "{'back': [{'title': 'тут название', 'description': 'тут детальное описание'}],'hand': [{'title': 'тут название', 'description': 'тут детальное описание'}], 'leg': [{'title': 'тут название', 'description': 'тут детальное описание'}], 'chest': [{'title': 'тут название', 'description': 'тут детальное описание'}], 'press': [{'title': 'тут название', 'description': 'тут детальное описание'}]}"

        return prompt
