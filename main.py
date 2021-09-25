from neo4j import GraphDatabase

class pyghack:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def add_event(self, event_id, name, start_time, end_time, type):
        with self.driver.session() as session:
            session.run("CREATE (a:Event {event_id: $event_id, name: $name, start_time: $start_time, end_time: $end_time, type: $type})", event_id=event_id, name=name, start_time=start_time, end_time=end_time, type=type)
    
    def add_student(self, name, interest):
        with self.driver.session() as session:
            session.run("CREATE (a:Student {name: $name, interest: $interest})", name=name, interest=interest)
    
    def delete_event(self, event_id, name, start_time, end_time, type):
        with self.driver.session() as session:
            session.run("MATCH (a:Event {event_id: $event_id, name: $name, start_time: $start_time, end_time: $end_time, type: $type}) DETACH DELETE a", event_id=event_id, name=name, start_time=start_time, end_time=end_time, type=type)

    def delete_student(self, name, interest):
        with self.driver.session() as session:
            session.run("MATCH (a:Student {name: $name, interest: $interest}) DETACH DELETE a", name=name, interest=interest)
    
    def create_relationship(self, student_name, event_id, event_name):
        with self.driver.session() as session:
            session.run("MATCH (a:Student), (b:Event) WHERE a.name = $student_name AND b.event_id = $event_id AND b.name = $event_name"
                        " CREATE (a)-[r:Attending]->(b)"
                        " CREATE (b)-[s:Attendee]->(a) RETURN *"
                        , student_name=student_name, event_id = event_id, event_name=event_name)


if __name__ == "__main__":
    database = pyghack("bolt://localhost:7687/", "neo4j", "1234")
    # database.delete_event("1", "Study group", "1700", "1900", "study")
    # database.delete_student("Chris", "sports")
    # database.create_relationship("Chris", "1", "Study group")
    database.close()