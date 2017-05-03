# HeatIndexCalculator.py
# Your job is to write a function in HeatIndexCalculator.py (call
# it **calculateHeatIndex()** that calculates the heat index
# factor based on the Heat Index Calculator from
# Calculator.net (http://www.calculator.net/heat-index-calculator.html)

# Define Function below
# be sure to return an integer
def calculateHeatIndex(RH, T):
    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = -.22475541
    e = -6.83783*(10**-3)
    f = -5.481717*(10**-2)
    g = 1.22874*(10**-3)
    h = 8.5282*(10**-4)
    i = -1.99*(10**-6)
    heatindex = a + b*T + c*RH + d*T*RH + e*T**2 + f*RH**2 + g*RH*T**2 + h*T*RH**2 + i*T**2*RH**2
    heatindex = int(heatindex)
    return heatindex

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    print('(45, 108) = ' + str(calculateHeatIndex(45, 108)))
    print('(65, 80) = ' + str(calculateHeatIndex(65, 80)))
    print('(65, 90) = ' + str(calculateHeatIndex(65, 90)))
    print('(60, 100) = ' + str(calculateHeatIndex(60, 100)))
    print('(95, 80) = ' + str(calculateHeatIndex(95, 80)))
    print('(100, 90) = ' + str(calculateHeatIndex(100, 90)))
    print('(80, 94) = ' + str(calculateHeatIndex(80, 94)))
    print('(70, 98) = ' + str(calculateHeatIndex(70, 98)))
