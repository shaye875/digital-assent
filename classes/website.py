from classes.digitalassent import *
from classes.repotable import *
class Website(DigitalAssent,Reportable):
    def __init__(self,name,registration_date,cost,monetization_rate,monthly_traffic):
        super().__init__(name,registration_date,cost)
        self.monetization_rate = monetization_rate
        self.monthly_traffic = monthly_traffic

    def assent_type(self):
        return 'WEBSITE'

    def calculate_value(self):
        return self.monthly_traffic*self.monetization_rate*12

    def to_report_line(self):
        return f'name is {self.get_name} date is {self.get_registration_date} cost is {self.get_cost} montonly trafik is {self.monthly_traffic}  monetization_rate is {self.monetization_rate} value is {self.calculate_value()}'
