# OPERATOR PRECEDENCE
# exponeent (**) goes first, followed by multiplication and division, before addition and subtraction
# if you want an operation to take precedence, use parenthesis

x = 10 + 2 * 5 ** 2
# In the above, 5**2 will be evaluated first, then it's result multiplied by 2, and then added to 10.

print(x) #60

# change precedence to make addition happen first. It becomes 10+2, 5 ** 2, then multiply both operations
y = (10 + 2) * 5 ** 2
print(y)