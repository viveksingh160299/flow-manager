from tasks.fetch_data_task import fetchDataTask
from tasks.process_data_task import processDataTask
from tasks.store_data_task import storeDataTask

pre_defined_task_list = [{
                    'name': "task1",
                    'classname': fetchDataTask
                },
                {
                    'name': "task2",
                    'classname': processDataTask
                },
                {
                    'name': "task3",
                    'classname': storeDataTask
                }]