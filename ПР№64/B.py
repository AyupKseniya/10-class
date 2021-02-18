file=input("Введите имя файла")
rush=input("введите новое расширение")
n="."
k=file.count(".")
if n not in file:
        print(file+n+rush)
elif k>1:
        file=file.split(".")
        print(file[0]+n+file[1]+n+rush)
else:
        file=file.split(".")
        print(file[0]+n+rush)
