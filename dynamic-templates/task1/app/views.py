from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    with open('inflation_russia.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')

    # чтение csv-файла и заполнение контекста
        context = {}

        return render(request, template_name, context={'inflation': reader})
