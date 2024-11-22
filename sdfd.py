L = [1,7,2,8,0,3,6,7]
L_iter = iter(L)
for i in L_iter:
    print(i)
    if i==7:
        next(L_iter,None)
