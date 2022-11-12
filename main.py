from transformers import pipeline
translator = pipeline("translation_ru_to_en", model="Helsinki-NLP/opus-mt-ru-en")
results = translator("Это проект по программной инженерии студентов УрФУ Шухардина Александра и Эмиля Афлатунова")
results
