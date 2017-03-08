import prediction as machine
import fileops as fops
import math
from flask import Flask, request, send_from_directory, redirect
app = Flask(__name__, static_url_path='')

# Take in user 2D array input
def getPrediction(user_input) :
    values = fops.fileToArr('dataset.txt')
    input = fops.dataToInputArr(values)
    output = fops.dataToOutputArr(values)
    machine.train(input, output)
    return machine.predict(user_input)

# Save 2D input and integer output
def saveData(input, output) :
    value = str(input[0]) + ':' + str(int(math.ceil(output)))
    value = value.replace("[", "")
    value = value.replace("]", "")
    value = value.replace(" ", "")
    fops.fileAppend('dataset.txt', value)

@app.route("/")
def root():
    return app.send_static_file('home.html')

@app.route("/reset")
def res():
    fops.fileReset('dataset.txt')
    return 'Training Data has been reset'


#"/predicting?id=<int:rid>&&direction=<int:direction>&&day=<int:day>&&hour=<int:hour>"
@app.route("/predict", methods = ['POST'])
def predicting():
    road_id = request.form['rid']
    road_direction = request.form['direction']
    road_day = request.form['day']
    road_hour = request.form['hour']
    input = [[int(road_id), int(road_direction), int(road_day), int(road_hour)]]
    output = getPrediction(input)
    saveData(input, output)
    return 'Road id = ' + road_id + " Road Direction = " + road_direction + " Day = " \
           + road_day + " Road Hour = " + road_hour + ' Magic Machine says traffic score is ' + str(output)

@app.route("/test")
def test():
    return app.send_static_file('predict.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')