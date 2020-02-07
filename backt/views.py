from django.http import HttpResponse
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG

class SmaCross(Strategy):
    def init(self):
        Close = self.data.Close
        self.ma1 = self.I(SMA, Close, 10)
        self.ma2 = self.I(SMA, Close, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()

# Create your views here.
def hisse(request, name):
    bt = Backtest(GOOG, SmaCross,
                  cash=10000, commission=.002)
    name=bt.run()
    html = "<html><body>It is now %s.</body></html>" % name
    return HttpResponse(html)
