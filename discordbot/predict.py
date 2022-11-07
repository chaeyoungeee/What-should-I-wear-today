from sklearn.linear_model import LinearRegression
import numpy as np
# import matplotlib.pyplot as plt

def predict_clothes(temp):
    temperature = []
    clothes_level = []
    f = open("./discordbot/temperature_clothes_level.txt", mode='r')
    while True:
        line = f.readline()
        line = line.split()
        if not line: break
        if line[0][0] == '-': line[0] = float(line[0][1:])*(-1)
        else: line[0] = float(line[0])
        temperature.append(line[0])
        clothes_level.append(float(line[1]))
    f.close()
    temperature = np.reshape(temperature, (-1,1))
    model = LinearRegression()
    model.fit(X=temperature, y=clothes_level)
    predict_clothes_level = model.predict([[temp]])[0]
    return predict_clothes_level



'''
    plt.xlabel("temperature")
    plt.ylabel("clothes_level")
    plt.plot(temperature, clothes_level, 'k.')
    plt.axis([-20,40,0,10])
    plt.plot(temperature, model.predict(temperature), color='r')
    plt.show()
'''