# Classify new trades Classify new trades based on their 
# similarity to old trades. Every trade has three features:
#  profit, risk, latency. You have a list of old trades, each 
#  has been labeled with a color. You have a list of new trades, 
#  unlabeled. Create an algorithm that uses old trades to predict 
#  labels of new trades. Input: A list of old trades. A list of labels
#   corresponding to old trades. A list of new trades. Classes may be 
#   imbalanced(eg, ‘red’ label may greatly outnumber ‘green’ label) The 
#   data set is small: Old trades less than 100, new trades less than 10.

def classify(trades,lables,new_trades):
    """
    >>> classify([[99.0,5.0,20.0],[95.0,15.0,10.0],[5.0,80.0,40.0],[3.0,92.0,20.0]],['green','green','red','red'],[[90.0,10.0,15.0],[10.0,98.0,50.0]])
    ['green', 'red']
    """
    green_number = 0
    red_number = 0
    for i in range(lables.__len__()):
        if(lables[i] == "green"):
            green_number = green_number+1
        else:
            red_number = red_number+1

    count = 0
    profit_green =0.0
    risk_green =0.0
    latency_green= 0.0
    profit_red = 0.0
    risk_red = 0.0
    latency_red= 0.0
    for j in range(trades.__len__()):
        if(count < green_number):
            count = count+1
            profit_green = profit_green+trades[j][0]
            risk_green = risk_green+trades[j][1]
            latency_green = latency_green+trades[j][2]
        else:
            profit_red =profit_red + trades[j][0]
            risk_red = risk_red+trades[j][1]
            latency_red = latency_red+trades[j][2]

    profit_green = profit_green / green_number
    risk_green = risk_green / green_number
    latency_green = latency_green/ green_number
    profit_red = profit_red/red_number
    risk_red = risk_red/red_number
    latency_red = latency_red/red_number
    result = []
    for k in range(len(new_trades)):
        if(abs(new_trades[k][0] - profit_green) <(new_trades[k][0]-profit_red)):
            result.append("green")
        elif(abs(new_trades[k][0] - profit_green) >(new_trades[k][0]-profit_red)):
            result.append("red")
        else:
            if(abs(new_trades[k][0] - risk_green) <(new_trades[k][0]-risk_red)):
                result.append("green")
            elif(abs(new_trades[k][0] - risk_green) >(new_trades[k][0]-risk_red)):
                result.append("red")
            else:
                if(abs(new_trades[k][0] - latency_green) <(new_trades[k][0]-latency_red)):
                    result.append("green")
                else:
                    result.append("red")
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()