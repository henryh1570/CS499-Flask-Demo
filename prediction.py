from sklearn import linear_model
reg = linear_model.LinearRegression()

def train(trainingInput, trainingOutput) :
    reg.fit(trainingInput, trainingOutput)

def predict(input) :
    return reg.predict(input)