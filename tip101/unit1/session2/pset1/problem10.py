def fizzbuzz(n):
    i = 1
    for x in range(n):
        if ((i % 3) and (i % 5)) != 0:
            print(i)
            i = i + 1
        elif (i % 5) == 0:
            print("Buzz")
            i = i + 1
        elif (i % 3) == 0:
            print("Fizz")
            i = i + 1
fizzbuzz(13)