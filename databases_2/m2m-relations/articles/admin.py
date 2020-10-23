from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Relationship, Tags


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # print(form.cleaned_data)

            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            #raise ValidationError('Тут всегда ошибка')
            if form.cleaned_data.get('main'):
                counter += 1
        if not counter:
            raise ValidationError('Выберите основной раздел!')
        elif counter > 1:
            raise ValidationError('Основной раздел должен быть один!')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass