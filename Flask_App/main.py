from unicodedata import name
from flask import Flask, request, jsonify

app=Flask(__name__)
contacts=[
    {
        "Name":"Rahul sir",
        "Contact_no":"9740283273",
        "id":"1",
        "nick_name":"Maths Teacher"
    },
    {
        "Name":"Abhinav sir",
        "Contact_no":"8093709927",
        "id":"2",
        "nick_name":"Physics"
    },
]

@app.route('/')
def welcome():
    return "Hello, welcome to flask app 01729 !"

@app.route('/add_data',methods=['POST'])
def add_data():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'could not get valid json response'
        },400)
    else:
        contact={
            "Name":request.json['Name'],
            "Contact_no":request.json['c_no'],
            "id":str(int(contacts[-1]['id'])+1),
            "nick_name":request.json['n_name']
        }
        contacts.append(contact)
        return jsonify({
            'status':'success',
            'message':'Contact added successfully !'
        })

@app.route('/get_data',methods=['GET'])
def get_data():
    return jsonify({"data":contacts})

if __name__=='__main__':
    app.run()