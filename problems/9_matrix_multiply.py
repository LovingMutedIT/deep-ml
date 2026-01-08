def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:


    a_cols = len(a[0])
    b_rows = len(b)
    if(a_cols != b_rows):
        return -1

    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(a[0])):
                sum += a[i][k] * b[k][j]
            c[i].append(sum)
            
    return c


