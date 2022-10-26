# ввод данных
print ("Введите фамилию, имя, отчество, год рождения")
def isint(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
while True:
    try:
        file = open('FIO.txt', 'a', encoding='utf8') 
        try:
            ln, fn, p, y = map(str, input().split())
            if ln == '-' and fn == '-' and p == '-' and y == '-':
                break
            elif isint(y) and len(y) == 4:
                file.write(str(ln) + ' ' + str(fn) + ' ' + str(p) + ' ' + str(y) + ' ' + '\n') 
            else:
                print('Неправильно введен год рождения')
        except ValueError:
            print('Неправильный ввод данных')
        finally:
            file.close()
    except:
        print('Ошибка при открытие файла')

        # чтения файла
print('Фамилия Имя Отчество Год рождения')
try:
    file = open('FIO.txt', 'r', encoding='utf8')
    while True:
        list = file.readline()
        if not list:
            break
        print('фамилия ' + ' имя ' + ' отчество ' + ' год рождения ' + '\n')
        print(str(list))
except:
    print('Ошибка при открытие файла')
finally:
    file.close()