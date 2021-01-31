

u_users = ['alice', 'brian', 'candice']
c_users = []

while u_users:
    current_users = u_users.pop()

    print("Verifying user: " + current_users.title())
    c_users.append(c_users)
print("\nTHe following users have been confirmed:")
for c in c_users:
    print(c.title())
