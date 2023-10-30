def make_negative( number ):
    return [number,-number][number >=0]


print(make_negative(5))

print(make_negative(-2))

