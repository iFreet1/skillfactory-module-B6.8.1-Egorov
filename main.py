from cat import Cat

cats = [Cat('Барон', 'Мальчик', 2), Cat('Сэм', 'Мальчик', 2)]

for cat in cats:
    print(*cat.get_information(), sep='')
