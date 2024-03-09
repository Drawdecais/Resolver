from itertools import combinations
global n;n = 1
numeros = list(range(1, 10))
combinaciones = [combinacion for combinacion in combinations(numeros, 4) if sum(combinacion) == 22]
for ls1 in combinaciones:
    for ls2 in combinaciones:
        if ls1 != ls2 and len(set(ls1) & set(ls2)) == 2:
            i1,i2 = set(ls1) & set(ls2)
            l1,l2 = ([x for x in ls if x not in (i1, i2)] for ls in (ls1, ls2))
            l1[1:1], l2[1:1] = (i2, i1), (i2, i1)

            def comp(f1,f2):
                global n
                dif16 = 16-(f1[0] + f1[1])
                dif14 = 14-(f1[1] + f1[2])
                dif13 = 13-(f2[0] + f2[1])
                dif15 = 15-(f2[1] + f2[2])

                if dif16 == dif14 and dif13 == dif15 and len(set((*f1,*f2,dif16,dif13))) > 7:
                    print(f1,f2,dif16,dif13,"n:",n);n+=1


            f1 = [l1[0],i1,l2[0]]
            f2 = [l1[-1],i2,l2[-1]]
            comp(f1,f2)
            f1 = [l1[0],i2,l2[0]]
            f2 = [l1[-1],i1,l2[-1]]
            comp(f1,f2)
            f1 = [l2[0],i2,l1[0]]
            f2 = [l1[-1],i1,l2[-1]]
            comp(f1,f2)
            f1 = [l2[0],i1,l1[0]]
            f2 = [l2[-1],i2,l1[-1]]
            comp(f1,f2)