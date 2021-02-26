def TumWor(A,w,L):
    if len(w)==L: 
        if w.count("Ы")==2 or w.count("О")==2 or w.count("Ш")==2 or w.count("Ч")==2: 
            print(w) 
        return 
    for c in A:
        TumWor(A,w +c,L)

k=int(input()) 
TumWor("ЫШЧО", "",k)
