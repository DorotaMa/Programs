def ciag_iter(n):
    if n > 1:
        lst = [2]
        for i in range (2,n+1):
            if i % 2 == 0:
                a = lst[-1] + 2
                lst.append(a)
                # print([lst[-1]], i)
            if i % 2 != 0:
                a = lst[-1] * 2
                lst.append(a)
                # print([lst[-1]], i)
    else:
        lst = [2]
    return lst

def ciag_rek(n):
    if n == 1:
        return 2
    if n % 2 != 0:
        return ciag_rek(n-1) * 2
    else:
        return ciag_rek(n-1) + 2

print(ciag_iter(6))
print([ciag_rek(x) for x in range(1, 7)])