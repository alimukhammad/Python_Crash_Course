

players = ['charly', 'marta', 'michael', 'florence', 'eli']
print("1 :", players[0:3])
print("2 :", players[1:4])
print("3 :", players[:4])
print("4 :", players[2:])
print("5 :", players[-3:], "\n")

print("Here are the first three players on my team:")
for p in players[:3]:
    print(p.title())

