from flask import Flask, escape, request, jsonify

id = 1001
c_id = 112200
students = {1001: 'Vatsa Patel', 1003: 'Vsrgatsa Patel',1006: 'Vasfgatsa Patel',1007: 'Vatsa Patel',}

classes = {1001: {
            'name': 'cmpe',
            'students': []
            }}

app = Flask(__name__)

@app.route('/')
def api_hello():
    if 'name' in request.args:
        return request.args['name']
    else:
        return 'API works!'

@app.route('/students', methods=['POST'])
def insert_student():
    name = request.json['name']
    global id
    id += 1
    students[id] = name
    print(students)
    return jsonify(
        id = id,
        name=name,
    ), 201

@app.route('/students/<id>', methods=['GET'])
def get_id(id):
    return jsonify(
        id = id,
        name=students.get(int(id)),
    ), 200

@app.route('/classes/<id>', methods=['GET'])
def get_class(id):
    t=classes.get(int(id))
    return jsonify(
        id = id,
        name=t['name'],
        students=t['students']
    ), 200

@app.route('/classes', methods=['POST'])
def insert_class():
    name = request.json['name']
    global c_id
    c_id += 1
    classes[c_id] = { 'name': name, 'students': [] }
    print(classes)
    return jsonify(
        id = c_id,
        name=name,
        students= '[]'
    ), 201

@app.route('/classes/<class_id>', methods=['PATCH'])
def insert_studsent(class_id):
    stu_id = request.json['student_id']
    s_name = students.get(stu_id)
    classes[int(class_id)]['students'].append( {'id' : stu_id, 'name': s_name} )
    c_metadata = classes.get(int(class_id))
    print(c_metadata)
    return jsonify(
        id = class_id,
        name= c_metadata['name'],
        students= c_metadata['students']
    ), 201
