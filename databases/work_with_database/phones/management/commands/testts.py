import csv
from django.utils.text import slugify
with open('../../../phones.csv', 'r') as csvfile:
    phone_reader = csv.reader(csvfile, delimiter=';')
    # пропускаем заголовок
    next(phone_reader)

    for line in phone_reader:
        # TODO: Добавьте сохранение модели
        print(line)
        print(slugify(line[1]))