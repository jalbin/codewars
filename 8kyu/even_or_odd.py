def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# An obscur but elegant alternative solution is

#   return ["Even","Odd"][number % 2]

# Indeed, depending on wheter number % 2 is 0 or 1, it will index the list ["Even","Odd"] and return its corresponding element  accordingly.
