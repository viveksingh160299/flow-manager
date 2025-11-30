from abc import ABC, abstractmethod

# 1. Define the abstract base class (interface)
class taskInterface(ABC):

    @abstractmethod
    def execute(self, input_data, user_id):
        pass