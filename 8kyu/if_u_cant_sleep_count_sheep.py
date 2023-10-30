def count_sheep(n):
    murmur = ''
    i = 0
    while i != n:
        i+=1
        murmur = murmur + str(i) + " sheep..."
    return murmur
