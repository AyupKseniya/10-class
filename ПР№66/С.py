words = []
print("Введите ФИО:\n")
while True:
    s = input()
    if s != "":
        words.append(s)
    else:
        break
words.sort()
print("список в алфавитном порядке")
for i in words:
    print(i)
