from db.db_queries import salary_data_service

class fetchDataTask:

    def execute(self, input_data, user_id):
        user_salary = salary_data_service.salaryDataService().getSalary(user_id)

        return user_salary