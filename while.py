# -------------[While]----------------
# With the while loop we can execute a set of statements as long as a condition is true.

num = 1

while num <= 14:
    print(num)
    num += 1

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1