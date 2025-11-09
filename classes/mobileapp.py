from classes.digitalassent import *
from classes.repotable import *
class MobileApp(DigitalAssent,Reportable):
    def __init__(self,name,registration_date,cost,avg_rating ,downloads):
        super().__init__(name,registration_date,cost)
        self.__avg_rating = avg_rating
        self.__downloads = downloads

    def assent_type(self):
        return 'MOBILEAPP'

    def calculate_value(self):
        return self.__downloads*0.5+self.__avg_rating*1000

    def to_report_line(self):
        return f'the type is {self.assent_type()} the name is {self.get_name} the date is {self.get_registration_date} the cost is {self.get_cost} the dowtlas is {self.__downloads} the avg is {self.__avg_rating} nuo is {self.calculate_value()}'