class Assetportfolio:
    def __init__(self,filename='digital_assent.csv'):
        self.__assets = []
        self.__filename = filename

    def add_asset(self,asset):
        self.__assets.append(asset)

    def calculate_total_net_worth(self):
        sum = 0
        for c in self.__assets:
            cost = c.get_cost
            calculate = c.calculate_value()
            sum+=calculate-cost
        return sum

    def save_portfolio(self):
        with open(self.__filename,'w') as f:
            for a in self.__assets:
                f.write(a.to_report_line())
                f.write('\n')

    def load_portfolio(self):
        self.__assets = []
        with open(self.__filename,'r') as f:
            try:
                read = f.read()
                print(read)
                print(',')
            except FileNotFoundError:
                print('file not faund')


