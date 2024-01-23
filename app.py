from flask import Flask , request , jsonify

app = Flask(__name__)

data = [
    {'id':0,'name': "mash", 'age': 25},
    {'id':1,'name': "mashi", 'age': 22},
]

@app.route('/')
def home():
    return "hello gp"

@app.route('/get_user/<name>')
def get_user(name):
    return 'hi ' + name

@app.route('/get_name')
def get_name():
    return request.args.get('name')

@app.route('/all_data')
def all_data():
    return jsonify(data)

@app.route('/create_user', methods=['POST'])
def create_user():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        new_data  = {'id':len(data)+1, 'name':name,'age':age}
        data.append(new_data)

        return jsonify(data)


@app.route('/get_one/<id>')
def get_one(id):
    for item in data:
        if str(item['id']) == id:
            return jsonify(item)

    return 'User not found'

@app.route('/update_user/<id>', methods = ['PUT', 'DELETE'])
def update_user(id):
    if request.method == "PUT":
        for i in range(len(data)):
            if(str(data[i]['id']) == id):
                name = request.form.get('name')
                age = request.form.get('age')
                if name:
                    data[i]['name'] = name
                if age:
                    data[i]['age'] = age
                return jsonify(data[i])
        else: 
            return "user not found"
    elif request.method == "DELETE":
         for i in range(len(data)):
            if(str(data[i]['id']) == id):
                data.pop(i)

                return f'user {id} deleted'
            
         return "user not found"


if __name__ == '__main__':
    app.run(debug=True)
    # for item in data:
    #     print(item['id'])