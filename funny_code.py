import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)


plt.plot(x, y)

plt.title('Sine Wave')


plt.xlabel('x values from 0 to 2π')
plt.ylabel('sin(x)')

plt.show()


data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)

print(df)
