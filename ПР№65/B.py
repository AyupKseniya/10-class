def TumWor(A,w,L):
    if len(w)==L: 
        if w.count("ЫЫ")==1 or w.count("ОО")==1 or w.count("ШШ")==1 or w.count("ЧЧ")==1: 
            print(w) 
        return 
    for c in A:
        TumWor(A,w +c,L)

k=int(input()) 
TumWor("ЫШЧО", "",k)
