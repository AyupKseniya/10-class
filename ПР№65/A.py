def TumWor(A,w,L):
    if len(w)==L:
        if w[1]=="Ы":
            print(w)
        return
    for c in A:
        TumWor(A,w +c,L)
k=int(input())
TumWor("ЫШЧО", "",k)   
