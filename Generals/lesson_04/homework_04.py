from os.path import split
from turtledemo.penrose import start

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
print("***")
print("task_01")
print("***")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

# task 02 ==
print("***")
print("task_02")
print("***")

""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
print("***")
print("task_03")
print("***")
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer)

# task 04
print("***")
print("task_04")
print("***")
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_count = adwentures_of_tom_sawer.lower().count("h")
print(f"Літера 'h' зустрічається {h_count} разів у тексті")

# task 05
print("***")
print("task_05")
print("***")
"""Виведіть, скільки слів у тексті починається з Великої літери?
"""
check_issup = adwentures_of_tom_sawer.split()
count = 0
for word in check_issup:
    if word[0].isupper():
        count += 1
print(f"Слів які починаються з великої літери: {count} ")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("***")
print("task_06")
print("***")
first_position = adwentures_of_tom_sawer.find("Tom")
second_position = adwentures_of_tom_sawer.find(
    "Tom",
    first_position + 1
)
print(second_position)

# task 07
print("***")
print("task_07")
print("***")
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print(adwentures_of_tom_sawer_sentences)
# task 08
print("***")
print("task_08")
print("***")
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
sentence_4 = adwentures_of_tom_sawer_sentences[3]
print(sentence_4.lower())
# task 09
print("***")
print("task_09")
print("***")
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith('By the time'):
        print(sentence)

# task 10
print("***")
print("task_10")
print("***")
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
count_words = adwentures_of_tom_sawer_sentences[-1].strip()
if count_words == "":
    count_words = adwentures_of_tom_sawer_sentences[-2].strip()

count_words = count_words.split()
print("Кількість слів в останньому реченні:", len(count_words))