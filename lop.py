name = input('привет, как вас зовут? ')
import sys
print ('ясно ' + name)
print ('очень приятно')
вуфлч = input('как дела? ' + name )
n = 'ясно' if  name != ("отлично") else 'ооо у меня тоже!'
print (n)
import time
time.sleep(3)
print ('хы')
import time
time.sleep(2)
print ('нууууууууу')
print("(1)Общение")
print("(2)Выход")
 
print("Введите цифры(1,2,):")
 
p = str(input());
 
if p == "1" :
    print("Окей, начали:")
    
elif p == "2" :
    input("Нажмите Enter")
 
else:
    print ("Выход...")

print("Выбирайте ответы так либо 1 либо 2")
import time
time.sleep(3)
print("а что бы ты сьел?")
print (' 5-спагетти, 7-роллы, 6-бургер ')
g = str(input());
if g == "5" :
    print("oooo я бы тоже хотел о мне пора")
    sys.exit
elif g == '2' :
    print ('ok')
elif g == '1' :
    print ('ok')
elif g == "7" :
    input("мммммммммммм ага ага но мне пора")
    sys.exit
elif g == '6' :
    input('мне пора')
    sys.exit
else:
    print ('такого нету в списке мне пора')
    sys.exit
import time
time.sleep(2)
print (' ты можешь рассказать мне какую-нибудь историю?')
import time
time.sleep(2)
print ('желательно смешную.....')
story = input('рассказывай: ')
a = len(story)
print(a)
import time
time.sleep(3)
print ('ты мне столько бесполезных букв написал(а)')
import time
time.sleep(2)
print ('мдааа ужж')
print ('11010000 10111110 11010001 10000010 11010000 10110010 11010000 10110101 11010001 10000010 111010 1000111 1000111 110101')
print ('пора завязывать с этим пока ' +name)
l = str(input());
if l == "GGG5" :
    print ('хм')
else:
    sys.exit
print ('ладно не пора')
import time
time.sleep(1)
print ('сыграем?')
print ('правила простые отгадай число')
import random
num = random.randint(1,10)
guess = int(input('Вводи от 1 до 10 '))
if guess == num :
    print ('ладно повезло')
    print ('тебе повезло......')

elif guess > 10:
    print('мне пора')
    sys.exit
elif guess < 1:
    print('мне пора')
    sys.exit
else:
    print('не правильно мне пора было загадано ', num)
