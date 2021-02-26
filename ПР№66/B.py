words=[]
print("введите слова:\n")
while True:
    s = input()
    if s != "":
        chislo,sl=s.split()
        words.append(sl)
    else:
        break
words.sort()
print("список слов в алфавитном порядке:")
print(",".join(words))
