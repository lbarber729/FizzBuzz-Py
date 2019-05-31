def  Fizzbuzz(n):
    line = ''
    if n % 3 == 0:
        line += "Fizz"
    if n % 5 == 0:
        line += "Buzz"
    if not line:
        line += str(n)
    return line
