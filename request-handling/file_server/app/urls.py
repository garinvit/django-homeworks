from django.urls import path, converters, register_converter
from datetime import datetime
# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from app import views


class DataConverter:
    regex = "[0-9]{4}-[0-9]{2}-[0-9]{2}"

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value.strftime('%Y-%m-%d')


register_converter(DataConverter, 'dstr')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', views.file_list, name='file_list'),
    path('<dstr:date>/', views.file_list, name='file_list'),    # задайте необязательный параметр "date"
                                      # для детальной информации смотрите HTML-шаблоны в директории templates
    path('file/<name>', views.file_content, name='file_content'),
]
