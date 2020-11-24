import matplotlib.pyplot as plt

picture = plt.figure(figsize=(9.6, 5.4))

with open('DS4.txt', 'r') as f:
    lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
plt.scatter(y, x)
plt.show()
picture.savefig('res.png')
