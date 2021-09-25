# import main Flask class and request object
from flask import Flask, request
from main import pyghack

# create the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return '''<button> <a href="/add-student/">Add Student</a></button>'''

# allow both GET and POST requests
@app.route('/add-student/', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        name = request.form.get('name')
        interest = request.form.get('interest')
        database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
        database.add_student(name, interest)
        database.close()

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Name: <input type="text" name="name"></label></div>
               <div><label>Interest: <input type="text" name="interest"></label></div>
               <input type="submit" value="Add Student">
               <button> <a href="/">Go back</a></button>
           </form>'''

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)