import random
import numpy
print("Здраствуйте, вас приветствует программа 'Продолжитель предложений'!")
method = input('''Какой метод вы хотите использовать?
1: Импортировать модель(Требуется файл с моделью) 2: Обучить модель
Ваш выбор: ''')
if method == '1':
    t = input('''Перенесите ранее созданый файл модели в папку к файлу программы
Нажмите Enter чтобы продолжить. ''')
    with open('model.txt','r+') as file:
        text = file.read()
        exec(f'slovar = {text}')
        file.close()
    print("Успешно!")
else:
    t = input('''Создайте файл input.txt рядом с файлом программы и введите текст для обучения туда.
Нажмите Enter чтобы продолжить. ''')
    print("Обучение...")
    with open('input.txt','r+',encoding='utf-8') as file:
        text = file.read()
        file.close()
    new_text = ''
    slovar = {}
    for i in text:
        if i.isalpha() or i==' ':
            new_text+=i.lower()
        else:
            new_text+=' '
            
    for i in range(len(new_text.split())-1):
        word = new_text.split()[i]
        next_word = new_text.split()[i+1]
        slovar[word] = slovar.get(word,set())
        slovar[word].add(next_word)

    with open('model.txt','w') as slovar_file:
        slovar_file.write(str(slovar))
        print()
        slovar_file.close()
    print("Успешно! Файл модели создан! Переходим к продолжению текста")

times = input('На сколько слов увеличить текст: ')
t=input("Введите слово с которого будет начинатся текст: ").lower()
gen_text = t
perv = t
sucsess = True
for i in range(100):
    try:
        perv = str(random.choice(list(slovar[perv])))
        gen_text +=f" {perv}"
    except:
        sucsess = False
        print("Ошибка: модель не может продолжить текст из-за неизвестного слова")
        break
if sucsess:
    print('Успешно')
    with open('output.txt','w') as output:
        output.write(gen_text)
        print("Сгенерированый текст успешно записан в файл output.txt")
        output.close()
