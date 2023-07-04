from flask import Flask,request,jsonify
import joblib,os

app = Flask(__name__)

phish_model = open('phishing.pkl','rb')
phish_model_ls = joblib.load(phish_model)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post('/predict')
def predict():	
    data = request.get_json()
    X_predict = [data["url"]]
    # print(X_predict)
    # feature=X_predict.get('feature')
    # print(feature)
	
    y_Predict = phish_model_ls.predict(X_predict)
    print(y_Predict)
    if y_Predict == 'bad':
     result = "This is a Phishing Site"
    else:
      result = "This is not a Phishing Site"

    return (result)
   
    # return jsonify{
	# 	"y_Predict"= result}
    return "hey"

if __name__=='__main__':
    app.run(debug=True)


