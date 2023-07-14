from flask import Flask,render_template,request,send_file,jsonify
import keras
import tensorflow as tf
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods = ['POST'])  
def diff():  
    if request.method == 'POST':  
        data = request.files
        print(data)

        #call the model predict function here

        result={'a':1}
        return render_template('result.html',data=result)
    
if __name__ ==  "__main__":
    app.run()

def model_call(frames_folder):
    #load the model
    model = tf.keras.models.load_model("model\model2.h5")
    #predict
    predictedoutput= model.predict(frames_folder)
    return predictedoutput
    #return results
