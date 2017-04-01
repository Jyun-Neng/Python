import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.title("Sine wave chart")
plt.show()

R = np.random.random(100000)
plt.hist(R, bins = 100)
plt.show()