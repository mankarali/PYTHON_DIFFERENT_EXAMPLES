a = list(map((lambda x : 'odd' if x % 2 != 0 else 'even'), list(range(100))))
b = list(range(100))
print(dict(zip(b,a)))