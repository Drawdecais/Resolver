from itertools import combinations, permutations, product
combin = [i for i in combinations(list(range(1,10)),4) if sum(i)==22]
print(list([16-(l[0]+m[0]),l[2:],m,l[:2],13-(l[1]+m[1])]
        for (j, l1), (k, l2) in product(enumerate(combin), repeat=2)
        if j>k and len(set(l1)&set(l2)) == 2
        for l in permutations(tuple(set(l1)^set(l2)))
        for m in permutations(tuple(set(l1)&set(l2)))
        if 0<16-(l[0]+m[0])==14-(l[2]+m[0]) not in (l+m) and
           0<13-(l[1]+m[1])==15-(l[3]+m[1]) not in (l+m)))