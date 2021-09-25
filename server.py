# import main Flask class and request object
from flask import Flask, request
from main import pyghack

# create the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return '''
            <button> <a href="/add-student/">Add Student</a></button>
            <button> <a href="/add-event/">Add Event</a></button>'''

# allow both GET and POST requests
@app.route('/add-student/', methods=['GET', 'POST'])
def add_student():
    # handle the POST request
    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    names, interests = database.fetch_students()
    names = ', '.join(names)
    interests = ', '.join(interests)
    database.close()
    str = ""
    output = '''
           <form method="POST">
               <p>Current students: %s</p>
               <p>Their interests: %s</p>
               <div><label>Name: <input type="text" name="name"></label></div>
               <div><label>Interest: <input type="text" name="interest"></label></div>
               <input type="submit" value="Add Student">
               <button> <a href="/">Go back</a></button>
               <p>%s</p>
           </form>'''
    if request.method == 'POST':
        str = "Student successfully added!"
        name = request.form.get('name')
        if not name:
            str = "You didn't enter a name!"
            return output % (names, interests, str)
        interest = request.form.get('interest')
        if not interest:
            str = "You didn't enter an interest!"
            return output % (names, interests, str)
        database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
        database.add_student(name, interest)
        database.close()

    # otherwise handle the GET request
    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    names, interests = database.fetch_students()
    names = ', '.join(names)
    interests = ', '.join(interests)
    database.close()
    return output % (names, interests, str)

@app.route('/add-event/', methods=['GET', 'POST'])
def add_event():
    # handle the POST request
    str = ""
    output = '''
           <form method="POST">
               <div><label>Name: <input type="text" name="name"></label></div>
               <div><label>Start Time: <input type="text" name="start_time"></label></div>
               <div><label>End Time: <input type="text" name="end_time"></label></div>
               <div><label>Type: <input type="text" name="type"></label></div>
               <input type="submit" value="Add Event">
               <button> <a href="/">Go back</a></button>
               <p>%s</p>
           </form>'''
    if request.method == 'POST':
        str = "Event successfully added!"
        name = request.form.get('name')
        if not name:
            str = "You didn't enter a name!"
            return output % str
        start_time = request.form.get('start_time')
        if not start_time:
            str = "You didn't enter a start time!"
            return output % str
        end_time = request.form.get('end_time')
        if not end_time:
            str = "You didn't enter an end time!"
            return output % str
        type = request.form.get('type')
        if not type:
            str = "You didn't enter a type!"
            return output % str
        database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
        database.add_event(name, start_time, end_time, type)
        database.close()
    # otherwise handle the GET request
    return output % str

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)