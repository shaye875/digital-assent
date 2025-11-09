from classes.assetportfolio import *
from classes.website import *
from classes.mobileapp import *
if __name__ == '__main__':
    my_protfolio = Assetportfolio()
    website = Website("shaye",2300,300,1000,1500)
    mobilayapp = MobileApp('avi',2301,350,1200,500)
    my_protfolio.add_asset(website)
    my_protfolio.add_asset(mobilayapp)
    print(my_protfolio.calculate_total_net_worth())
    my_protfolio.save_portfolio()
    my_protfolio1 = Assetportfolio()
    my_protfolio1.add_asset(website)
    my_protfolio1.add_asset(mobilayapp)
    print(my_protfolio1.calculate_total_net_worth())
