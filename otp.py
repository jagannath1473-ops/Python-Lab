n = int(input(&quot;Enter number of terms: &quot;))

a = 0
b = 1

print(a, end=&quot; &quot;)
print(b, end=&quot; &quot;)

for i in range(3, n + 1):

c = a + b

print(c, end=&quot; &quot;)

a = b
b = c
