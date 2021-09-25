from neo4j import GraphDatabase

class pyghack:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def add_event(self, name, start_time, end_time, type):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_event, name, start_time, end_time, type)

    @staticmethod
    def _create_and_return_event(tx, name, start_time, end_time, type):
        result = tx.run("CREATE (a:Event) "
                        "SET a.name = $name, "
                        "a.start_time = $start_time, "
                        "a.end_time = $end_time, "
                        "a.type = $type", name = name, start_time = start_time, end_time = end_time, type = type)
        return result.single()[0]


if __name__ == "__main__":
    database = pyghack("bolt://192.168.137.2:7687/", "neo4j", "1234")
    database.add_event("Study group", "1700", "1900", "study")
    database.close()