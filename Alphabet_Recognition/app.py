from crypt import methods
from operator import methodcaller
from flask import Flask,request,jsonify
from classifier import alphabet_recognition

app=Flask(__name__)

@app.route('/pred_alphabet',methods=['POST'])
def pred_alphabet():
    image_name=request.json['iname']
    prediction=alphabet_recognition(image_name)
    return jsonify({"prediction":prediction})

if __name__ == "__main__":
    app.run(debug=True)