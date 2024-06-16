# conditional statement.
def sami(name):
    print(f"Hello everyone those are present here.{name}")
sami("ali")
# recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

