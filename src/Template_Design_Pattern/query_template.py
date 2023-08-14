import datetime
import sqlite3


# Base class which server as the template
class QueryTemplate:
    def connect(self):
        self.conn = sqlite3.connect(database="test.db")

    def construct_query(self):
        raise NotImplementedError()

    def execute_query(self):  # This is template method
        results = self.conn.execute(self.query)
        self.result = results.fetchall()

    def format_query(self):
        pass
        # put formatting code here

    def output_result(self):
        raise NotImplementedError()


# Child class written to fit given purpose
class NewVehicleQuery(QueryTemplate):
    def construct_query(self):
        self.query = """
                        select 
                            * 
                        from sales 
                        where new=true
                    """

    def output_result(self):
        for result in self.results:
            print(result)


# Child class written to fit given purpose
class UserGrossQuery(QueryTemplate):
    def construct_query(self):
        self.query = """
                        select 
                            sales_person, sum(sales_ammount) 
                        from sales 
                        group by sales_person
                    """

    def output_result(self):
        file_name = f'gross_sales_{datetime.date.today().strftime("%Y%m%d")}'
        with open(file_name, "w") as out_file:
            out_file.write(self.result)
