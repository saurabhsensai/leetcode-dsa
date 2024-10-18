#this first type of question for pascal triangle, we have given row and col and we have to output a element from that position from pascal triangle.


def SpecNum(n , r):
    n = n - 1 
    r = r - 1
    res = 1
    for i in range(0, r):
        res = res * (n - i)
        res = res // (i + 1)

    return res
        

# print(SpecNum(6, 2))


# second type of question wants you to print the entire row.

def PrintEntireRow(r):
    output = []
    output.append(1)
    ans = 1
    for i in range(1 , r):
        ans = ans * (r - i)
        ans = ans // i
        output.append(ans)
    
    return output

print(PrintEntireRow(6))
