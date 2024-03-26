import matplotlib.pyplot as plt

fig, ax = plt.subplots()


center = (0, 0)


radius = 1


circle1 = plt.Circle(xy=center, radius=radius, color='blue')


circle2 = plt.Circle(xy=center, radius=radius / 2, color='gray')


ax.add_patch(circle1)
ax.add_patch(circle2)


ax.set_aspect("equal")


plt.xlim([-radius - radius / 5 + center[0], radius + radius / 5 + center[0]])
plt.ylim([-radius - radius / 5 + center[1], radius + radius / 5 + center[1]])


plt.xlabel("X")
plt.ylabel("Y")


plt.title('Blue and gray circles')

plt.show()
