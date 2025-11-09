from datetime import datetime
from abc import abstractmethod
class DigitalAssent:
    def __init__(self,name,registration_date,cost):
        self.__name = name
        self.__registration_date = registration_date
        self.__cost = cost

    @property
    def get_name(self):
        return self.__name

    @property
    def get_registration_date(self):
        return self.__registration_date

    @property
    def get_cost(self):
        return self.__cost

    def set_name(self,name):
        self.__name = name

    def set_registration_date(self):
        self.__registration_date = datetime.now().isoformat()

    def set_cost(self,cost):
        self.__cost = cost

    @abstractmethod
    def calculate_value(self):
        pass

    @abstractmethod
    def assent_type(self):
        pass


