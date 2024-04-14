# 1) как можно сделать проверку существует ли файл?

import os.path
os.path.isfile("имя_файла.расширение")

### или так:
os.path.exists('my_file')

### Функция os.getcwd возвращает текущий каталог:
import os
cwd = os.getcwd()
print(cwd)

### пример рекурсивно выводит список всех файлов и подкаталогов для данного каталога:
import os
def walk(dir):
  for name in os.listdir(dir):
    path = os.path.join(dir, name)
    if os.path.isfile(path):
        print(path)
    else:
        walk(path)
walk(path)

### интерпретация системной утилиты grep. 
### В текущем каталоге будут найдены файлы с питоновским расширением, в которых будет найдена поисковая строка 'import os':

import os, sys, fnmatch
 
mask = '*.py'
pattern = 'import os'
 
def walk(arg,dir,files):
   for file in files:
     if fnmatch.fnmatch(file,mask):
        name = os.path.join(dir,file)
        try:
          data = open(name,'rb').read()
          if data.find(pattern) != -1:
            print(path)
        except:
            pass    
os.path.walk('.',walk,[])

# 2) как открыть файлы из списка?

import os
# Каталог из которого будем брать файлы
directory = 'F:\\python\\test'
# Получаем список файлов из каталога directory в переменную files
files = os.listdir(directory)
# Фильтруем список по расширению
images = filter(lambda x: x.endswith('.jpg'), files)
php = filter(lambda x: x.endswith('.php'), files)
pdf = filter(lambda x: x.endswith('.pdf'), files)
html = filter(lambda x: x.endswith('.html'), (files))
txt = filter(lambda x: x.endswith('.txt'), (files)) 
# Выводим список на экран нужный файл print(list(txt))
S = (list(txt))
# открыть файл
for x in S: open('F:\\python\\new\\{}'.format(x),'w')


# 3) Прочитать файл и записать его содержимое в другой файл:

f = open(r'my_file')
lines = f.readlines()
f.close()
lines[0] = "This is a my_file2 \n" # изменяем 1-ю строку
f = open(r'my_file2','w')
f.writelines(lines)
f.close()

# 4) Для полной уверенности в закрытии файла можно использовать блок try/finally:

try:
   # Тут идет запись в файл
finally:
	file.close()

# Можно также использовать менеджер контекста, который в любом случае закроет файл:

with open("my_file") as somefile:
	do_something(somefile)

# 5) Построчное чтение текстовых файлов и функция readline():
f = open(filename)
while True:
  line = f.readline()
  if not line: break
  process(line)
f.close()

# Файл сам может выступать в роли итератора:
for line in open(filename):
  process(line)

# 6) Pickling
# Практически любой тип объекта может быть сохранен на диске в любой момент его жизни, а позже прочитан с диска. Для этого есть модуль pickle:
import pickle
t1 = [1, 2, 3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print t2
[1, 2, 3]


import os
# объединяет рабочий каталог с путём который дал ты "database/raw/train.csv" ра. кат. D:\main\note
file_path = os.path.abspath("database/raw/train.csv")
# аналог
print(os.getcwd()) 
# D:\main\note
print(os.path.join(os.getcwd(), "database/raw/train.csv")) 
# D:\main\note\database/raw/train.csv
print(os.path.normpath(os.path.join(os.getcwd(), "database/raw/train.csv")))
# D:\main\note\database\raw\train.csv