# import main Flask class and request object
from flask import Flask, request
from main import pyghack

# create the Flask app
app = Flask(__name__)


@app.route('/')
def index():
    name = "TimeStamp"
    return '''
            <body style="text-align: center;background-color:powderblue;margin-top: 120px;">
            <header><h1>Welcome to %s</h1></header>
            <button style="background-color: orange; /* Green */
            border: none;
            color: white;
            padding: 15px 32px;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;"> <a href="/add-student/">Add Student</a></button>
            <button style="background-color: orange; /* Green */
            border: none;
            color: white;
            padding: 15px 32px;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;"> <a href="/add-event/">Add Event</a></button>
            <button style="background-color: orange; /* Green */
            border: none;
            color: white;
            padding: 15px 32px;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;"> <a href="/delete-student/">Remove Student</a></button>
            <button style="background-color: orange; /* Green */
            border: none;
            color: white;
            padding: 15px 32px;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;"> <a href="/delete-event/">Remove Event</a></button>
            <button style="background-color: orange; /* Green */
            border: none;
            color: white;
            padding: 15px 32px;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;"> <a href="/connect-student-event/">Add Student to an Event</a></button>
            
            <button style="background-color: orange; /* Green */
            border: none;
            color: white;
            padding: 15px 32px;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;"> <a href="/connect-student-student/">Connect Students</a></button>
            </body>
            ''' % name


# allow both GET and POST requests
@app.route('/add-student/', methods=['GET', 'POST'])
def add_student():
    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    names, interests = database.fetch_students()
    names = ', '.join(names)
    interests = ', '.join(interests)
    database.close()
    str = ""
    output = '''
           <body style="text-align: center;background-color:powderblue;margin-top: 120px;">
           <form method="POST">
               <h2>Current students: %s -
               Their interests: %s</h2>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>Name: <input type="text" name="name" style = "height: 38;"></label></div>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>Interest: <input type="text" name="interest" style = "height: 38;"></label></div>
               <br>
               <input style="background-color: orange;
                border: none;
                color: white;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;" type="submit" value="Add Student">
               <button style="background-color: orange;
                border: none;
                color: white;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;"> <a href="/">Go Back</a></button>
               <p>%s</p>
           </form>
           </body>'''
    # handle the POST request
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
    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    names, start_times, end_times, types = database.fetch_events()
    names = ', '.join(names)
    start_times = ', '.join(start_times)
    end_times = ', '.join(end_times)
    types = ', '.join(types)
    database.close()
    str = ""
    output = '''
           <body style="text-align: center;background-color:powderblue;margin-top: 120px;">
           <form method="POST">
               <h2>Current events: %s -
               Start times: %s -
               End times: %s -
               Types: %s</h2>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"> <label>Name: <input type="text" name="name" style = "height: 38;"></label></div>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>Start Time: <input type="text" name="start_time" style = "height: 38;"></label></div>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>End Time: <input type="text" name="end_time" style = "height: 38;"></label></div>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>Type: <input type="text" name="type" style = "height: 38;"></label></div>
               <br>
               <input style="background-color: orange;
                border: none;
                color: white;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;" type="submit" value="Add Event">
               <button style="background-color: orange;
                border: none;
                color: white;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;"> <a href="/">Go Back</a></button>
               <p>%s</p>
           </form>
           </body>'''
    # handle the POST request
    if request.method == 'POST':
        str = "Event successfully added!"
        name = request.form.get('name')
        if not name:
            str = "You didn't enter a name!"
            return output % (names, start_times, end_times, types, str)
        start_time = request.form.get('start_time')
        if not start_time:
            str = "You didn't enter a start time!"
            return output % (names, start_times, end_times, types, str)
        end_time = request.form.get('end_time')
        if not end_time:
            str = "You didn't enter an end time!"
            return output % (names, start_times, end_times, types, str)
        type = request.form.get('type')
        if not type:
            str = "You didn't enter a type!"
            return output % (names, start_times, end_times, types, str)
        database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
        database.add_event(name, start_time, end_time, type)
        database.close()
    # otherwise handle the GET request
    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    names, start_times, end_times, types = database.fetch_events()
    names = ', '.join(names)
    start_times = ', '.join(start_times)
    end_times = ', '.join(end_times)
    types = ', '.join(types)
    database.close()
    return output % (names, start_times, end_times, types, str)


# allow both GET and POST requests
@app.route('/delete-student/', methods=['GET', 'POST'])
def delete_student():
    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    names, interests = database.fetch_students()
    names = ', '.join(names)
    interests = ', '.join(interests)
    database.close()
    str = ""
    output = '''
           <body style="text-align: center;background-color:powderblue;margin-top: 120px;">
           <form method="POST">
               <h2>Current students: %s -
               Their interests: %s</h2>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>Name: <input type="text" name="name" style = "height: 38;"></label></div>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>Interest: <input type="text" name="interest" style = "height: 38;"></label></div>
                <br>
               <input style="background-color: orange;
                border: none;
                color: white;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;" type="submit" value="Remove Student">
               <button style="background-color: orange;
                border: none;
                color: white;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;"> <a href="/">Go Back</a></button>
               <p>%s</p>
           </form>
           </body>'''
    # handle the POST request
    if request.method == 'POST':
        str = "Student successfully removed!"
        name = request.form.get('name')
        if not name:
            str = "You didn't enter a name!"
            return output % (names, interests, str)
        interest = request.form.get('interest')
        if not interest:
            str = "You didn't enter an interest!"
            return output % (names, interests, str)
        database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
        database.delete_student(name, interest)
        database.close()

    # otherwise handle the GET request
    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    names, interests = database.fetch_students()
    names = ', '.join(names)
    interests = ', '.join(interests)
    database.close()
    return output % (names, interests, str)


@app.route('/delete-event/', methods=['GET', 'POST'])
def delete_event():
    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    names, start_times, end_times, types = database.fetch_events()
    names = ', '.join(names)
    start_times = ', '.join(start_times)
    end_times = ', '.join(end_times)
    types = ', '.join(types)
    database.close()
    str = ""
    output = '''
           <body style="text-align: center;background-color:powderblue;margin-top: 120px;">
           <form method="POST">
               <h2>Current events: %s -
               Start times: %s -
               End times: %s -
               Types: %s</h2>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>Name: <input type="text" name="name" style = "height: 38;"></label></div>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;" ><label>Start Time: <input type="text" name="start_time" style = "height: 38;"></label></div>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>End Time: <input type="text" name="end_time" style = "height: 38;"></label></div>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>Type: <input type="text" name="type" style = "height: 38;"></label></div>
                <br>
               <input style="background-color: orange;
                border: none;
                color: white;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;" type="submit" value="Remove Event">
               <button style="background-color: orange;
                border: none;
                color: white;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;"> <a href="/">Go Back</a></button>
               <p>%s</p>
           </form>
           </body>'''
    # handle the POST request
    if request.method == 'POST':
        str = "Event successfully deleted!"
        name = request.form.get('name')
        if not name:
            str = "You didn't enter a name!"
            return output % (names, start_times, end_times, types, str)
        start_time = request.form.get('start_time')
        if not start_time:
            str = "You didn't enter a start time!"
            return output % (names, start_times, end_times, types, str)
        end_time = request.form.get('end_time')
        if not end_time:
            str = "You didn't enter an end time!"
            return output % (names, start_times, end_times, types, str)
        type = request.form.get('type')
        if not type:
            str = "You didn't enter a type!"
            return output % (names, start_times, end_times, types, str)
        database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
        database.delete_event(name, start_time, end_time, type)
        database.close()
    # otherwise handle the GET request
    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    names, start_times, end_times, types = database.fetch_events()
    names = ', '.join(names)
    start_times = ', '.join(start_times)
    end_times = ', '.join(end_times)
    types = ', '.join(types)
    database.close()
    return output % (names, start_times, end_times, types, str)


@app.route('/connect-student-event/', methods=['GET', 'POST'])
def connect_student_event():
    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    names, start_times, end_times, types = database.fetch_events()
    names = ', '.join(names)
    start_times = ', '.join(start_times)
    end_times = ', '.join(end_times)
    types = ', '.join(types)
    # names_students, interests = database.fetch_students()
    # names_students = ', '.join(names_students)
    # interests = ', '.join(interests)
    database.close()
    str = ""
    output = ''' 
              <body style="text-align: center;background-color:powderblue;margin-top: 120px;">
               <form method="POST" align = "center">
               <h2>Current events: %s -
               Start times: %s -
               End times: %s - 
               Types: %s</h2>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>Event Name: <input type="text" name="event_name" style = "height: 38;"></label></div>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>Student Name: <input type="text" name="student_name" style = "height: 38;"></label></div>
               <br>
               <input style="background-color: orange;
                border: none;
                color: white;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;" type="submit" value="Add Student to an event">
               <button style="background-color: orange;
                border: none;
                color: white;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;"> <a href="/">Go Back</a></button>
               <p>%s</p>
           </form>
           </body>'''

    if request.method == 'POST':
        str = "Student Registered successfully to the Event!"
        event_name = request.form.get('event_name')
        student_name = request.form.get('student_name')
        if not event_name:
            str = "You didn't enter a name!"
            return output % (names, start_times, end_times, types, str)
        if not student_name:
            str = "You didn't enter a name!"
            return output % (names, start_times, end_times, types, str)

        database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
        database.connect_student_event(student_name, event_name)
        database.close()

    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    names, start_times, end_times, types = database.fetch_events()
    names = ', '.join(names)
    start_times = ', '.join(start_times)
    end_times = ', '.join(end_times)
    types = ', '.join(types)
    # names_students, interests = database.fetch_students()
    # names_students = ', '.join(names_students)
    # interests = ', '.join(interests)
    database.close()
    return output % (names, start_times, end_times, types, str)

@app.route('/connect-student-student/', methods=['GET', 'POST'])
def connect_student_student():
    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    # names, start_times, end_times, types = database.fetch_events()
    # names = ', '.join(names)
    # start_times = ', '.join(start_times)
    # end_times = ', '.join(end_times)
    # types = ', '.join(types)
    names_students, interests = database.fetch_students()
    names_students = ', '.join(names_students)
    interests = ', '.join(interests)
    database.close()
    str = ""
    output = ''' 
              <body style="text-align: center;background-color:powderblue;margin-top: 120px;">
               <form method="POST" align = "center">
               <h2>Current students: %s -
               Their interests: %s</h2>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>Student Name: <input type="text" name="student_name_a" style = "height: 38;"></label></div>
               <div style="border: none;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;"><label>Student Name: <input type="text" name="student_name_b" style = "height: 38;"></label></div>
               <br>
               <input style="background-color: orange;
                border: none;
                color: white;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;" type="submit" value="Connect two students">
               <button style="background-color: orange;
                border: none;
                color: white;
                padding: 15px 32px;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;"> <a href="/">Go Back</a></button>
               <p>%s</p>
           </form>
           </body>'''

    if request.method == 'POST':
        str = "Students successfully connected!"
        student_name_a = request.form.get('student_name_a')
        student_name_b = request.form.get('student_name_b')
        if not student_name_a:
            str = "You didn't enter a name!"
            return output % (names_students, interests, str)
        if not student_name_b:
            str = "You didn't enter a name!"
            return output % (names_students, interests, str)
        if student_name_a == student_name_b:
            str = "That's the same student!"
            return output % (names_students, interests, str)

        database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
        database.connect_student_student(student_name_a, student_name_b)
        database.close()

    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    # names, start_times, end_times, types = database.fetch_events()
    # names = ', '.join(names)
    # start_times = ', '.join(start_times)
    # end_times = ', '.join(end_times)
    # types = ', '.join(types)
    names_students, interests = database.fetch_students()
    names_students = ', '.join(names_students)
    interests = ', '.join(interests)
    database.close()
    return output % (names_students, interests, str)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
