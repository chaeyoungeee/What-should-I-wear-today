from sklearn.linear_model import LinearRegression
import numpy as np
import gspread
# import matplotlib.pyplot as plt

def predict_clothes(temp):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    gc = gspread.service_account(filename='./discordbot/key.json')

    ws = gc.open("temperature_clothes_level").worksheet('sheets1')
    temperature = ws.col_values(1)
    for i in range(len(temperature)):
        if temperature[i][0] == '-':
            temperature[i] = float(temperature[i][1:]) * (-1)
        else:
            temperature[i] = float(temperature[i])
    clothes_level = list(map(float, ws.col_values(2)))

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