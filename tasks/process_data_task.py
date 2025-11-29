from tasks.task_interface import taskInterface

class processDataTask(taskInterface):

    def execute(self, input_data, user_id):
        # Process the data
        incremented_user_salary = 1.2*input_data

        return incremented_user_salary