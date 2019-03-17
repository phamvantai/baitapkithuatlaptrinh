i=1;
while i<100:
    nt=1;
    for j in range(2, i - 1):
        if i%j == 0:
            nt= 0;
    if nt==1:
        print(i)
    i=i+1