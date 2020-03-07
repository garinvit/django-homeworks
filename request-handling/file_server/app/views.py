import datetime
import os
from django.shortcuts import render


def file_list(request, date=None):
    print(date)
    template_name = 'index.html'
    files_list = os.listdir('files')
    files = []
    if date:
        date = date.date()
    for file in files_list:
        file_dict = {}
        file_dict['name'] = file
        file_dict['ctime'] = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join('files', file)))
        file_dict['mtime'] = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join('files', file)))
        if not date:
            files.append(file_dict)
        elif date:
            if date == file_dict['ctime'].date():
                files.append(file_dict)
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': files,
        'date': date  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    try:
        with open(os.path.join('files', name)) as file:
            content = file.read()
    except Exception:
        content = 'Файл не найден!!!'

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

