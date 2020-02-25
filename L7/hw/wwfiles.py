import datetime

from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

# 1) Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).

with open ('data.txt') as f:
    content = f.read()
    print(content)

print('------------------------------------------------------------')
# 2) Создать doc шаблон, где будут использованы данные параметры.

# 3) Автоматически сгенерировать отчет о машине в формате doc (как в видео 7.2)

from time import time
tic = time()


def get_context(brand, price, year):
    return {
        'brand': brand,
        'price': price,
        'year': year,
    }
def from_template(brand, price, year, template, signature):
    template = DocxTemplate(template)
    context = get_context(brand, price, year)

    img_size = Cm(8)
    acc = InlineImage(template, signature, img_size)
    context['acc'] = acc

    template.render(context)
    template.save(brand + "_" + str(datetime.datetime.now()) + '_report.docx')


def generate_report(brand, price, year):
    template = "doc_template.docx"
    signature = 'acc.png'
    document = from_template(brand, price, year, template, signature)

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


generate_report('Honda', '1,28', '2014')
print('-------сгенерирован отчет о машине-----------------------------------------')

toc = time()
execution_time = toc - tic
print("Program Executed in " + str(execution_time))



# 4) Создать csv файл с данными о машине.


from time import time
tic = time()


a =  list(map(str, content.split('\n')))
# print(a)

import csv

with open('example.csv', 'w') as f:
    writer = csv.writer(f, delimiter = '\n')
    writer.writerow(a)


print('-----файл example.csv создан-------------------------------------------------------')

toc = time()
execution_time = toc - tic
print("Program Executed in " + str(execution_time))

# 5) Создать json файл с данными о машине.
from time import time
tic = time()

import json
with open('a_to_json.txt', 'w') as f:
    json.dump(a, f)

print('-----файл a_to_json.txt создан-------------------------------------------------------')

toc = time()
execution_time = toc - tic
print("Program Executed in " + str(execution_time))