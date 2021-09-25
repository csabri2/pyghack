from neo4j import GraphDatabase

class pyghack:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # def add_event(self, user, name, start_time, end_time, type):
    #     with self.driver.session() as session:
    #         session.write_transaction(self._create_and_return_event, user, name, start_time, end_time, type)

    # @staticmethod
    # def _create_and_return_event(tx, user, name, start_time, end_time, type):
    #     result = tx.run("CREATE (a:Event) "
    #                     "SET a.user = $user, "
    #                     "a.name = $name, "
    #                     "a.start_time = $start_time, "
    #                     "a.end_time = $end_time, "
    #                     "a.type = $type", user = user, name = name, start_time = start_time, end_time = end_time, type = type)
    #     return result.single()[0]

    def add_event(self, event_id, name, start_time, end_time, type):
        with self.driver.session() as session:
            session.run("CREATE (a:Event {event_id: $event_id, name: $name, start_time: $start_time, end_time: $end_time, type: $type})", event_id=event_id, name=name, start_time=start_time, end_time=end_time, type=type)
    
    def add_student(self, name, interest):
        with self.driver.session() as session:
            session.run("CREATE (a:Student {name: $name, interest: $interst})", name=name, interest=interest)
    
    def delete_event(self, event_id, name, start_time, end_time, type):
        with self.driver.session() as session:
            session.run("MATCH (a:Event {event_id: $event_id, name: $name, start_time: $start_time, end_time: $end_time, type: $type}) DELETE a", event_id=event_id, name=name, start_time=start_time, end_time=end_time, type=type)

    def delete_student(self, name, interest):
        with self.driver.session() as session:
            session.run("MATCH (a:Student {name: $name, interest: $interst}) DELETE a", name=name, interest=interest)

    # def _create_and_return_user(tx, name, )


if __name__ == "__main__":
    database = pyghack("bolt://192.168.137.2:7687/", "neo4j", "1234")
    database.add_event("Study group", "1700", "1900", "study")
    database.close()