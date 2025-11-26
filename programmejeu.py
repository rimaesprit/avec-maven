# Simple algorithmic fish drawing in ASCII

width = 20  # width of the fish body
height = 7  # height of the fish body

# Draw top fin
for i in range(height//2):
    spaces = ' ' * (height//2 - i)
    stars = '*' * (2*i + 1)
    print(spaces + stars + spaces)

# Draw fish body
for i in range(height):
    print('*' + ' ' * width + '*')

# Draw tail
for i in range(height//2, 0, -1):
    spaces = ' ' * (height//2 - i)
    stars = '*' * (2*i + 1)
    print(spaces + stars + spaces)
