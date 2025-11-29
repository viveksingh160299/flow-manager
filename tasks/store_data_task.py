from db.db_queries import salary_data_service
from datetime import datetime

class storeDataTask:

    def execute(self, input_data, user_id):
        # Timestamp
        timestamp = datetime.now()
        timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        # Update the new salary
        salary_data_service.salaryDataService().updateSalary(input_data, timestamp, user_id)

        return "Updated!"