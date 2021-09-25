from neo4j import GraphDatabase

class pyghack:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def add_event(self, name, start_time, end_time, type):
        with self.driver.session() as session:
            session.run("CREATE (a:Event {name: $name, start_time: $start_time, end_time: $end_time, type: $type})", name=name, start_time=start_time, end_time=end_time, type=type)
    
    def add_student(self, name, interest):
        with self.driver.session() as session:
            session.run("CREATE (a:Student {name: $name, interest: $interest})", name=name, interest=interest)
    
    def delete_event(self, name, start_time, end_time, type):
        with self.driver.session() as session:
            session.run("MATCH (a:Event {name: $name, start_time: $start_time, end_time: $end_time, type: $type}) DETACH DELETE a", name=name, start_time=start_time, end_time=end_time, type=type)

    def delete_student(self, name, interest):
        with self.driver.session() as session:
            session.run("MATCH (a:Student {name: $name, interest: $interest}) DETACH DELETE a", name=name, interest=interest)
    
    def create_relationship(self, student_name, event_name):
        with self.driver.session() as session:
            session.run("MATCH (a:Student), (b:Event) WHERE a.name = $student_name AND b.name = $event_name"
                        " CREATE (a)-[r:Attending]->(b)"
                        " CREATE (b)-[s:Attendee]->(a) RETURN *"
                        , student_name=student_name, event_name=event_name)
    
    def fetch_students(self):
        with self.driver.session() as session:
            result = session.run("MATCH (a:Student) RETURN a.name AS name")
            names = [record["name"] for record in result]
            return names


if __name__ == "__main__":
    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    # database.delete_event("Study group", "5:30", "10:30", "study")
    # database.delete_student("Chris", "sports")
    # database.create_relationship("Chris", "1", "Study group")
    # database.fetch_students()

    database.close()