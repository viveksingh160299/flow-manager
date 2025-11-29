from db.crud.crud_ops import crudOps

class salaryDataService:

    def __init__(self):
        self.table_name = "salary_data"

    def getSalary(self, user_id):
        query = '''SELECT salary FROM {table} WHERE user_id=%s'''

        results  = crudOps.fetch(query, self.table_name, (user_id,))

        return results


    def updateSalary(self, salary, timestamp, user_id):
        query = '''UPDATE {table} SET salary=%s, timestamp=%s WHERE user_id=%s'''

        crudOps.update(query, self.table_name, (salary, timestamp, user_id))
