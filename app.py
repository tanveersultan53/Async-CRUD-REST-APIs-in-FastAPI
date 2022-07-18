from flask import Flask, request,jsonify
from firebase_admin import credentials, firestore, initialize_app
from flask_cors import CORS, cross_origin
import backtrader as bt
from dateutil.parser import *
import yfinance as yf
import math



app = Flask(__name__, static_folder="../public", static_url_path="/")
app.config['CORS_HEADERS'] = 'Content-Type'



CORS(app)

# cred = credentials.Certificate("firestore_apikey.json")
# # firebase_admin.initialize_app(cred)
# default_app = initialize_app(cred, {'storageBucket': 'autostock-fef22.appspot.com'})
# db = firestore.client()
# algorithms_ref = db.collection('algorithms')
# activeCompetitions_ref = db.collection('activeCompetitions')
# staleCompetitions_ref = db.collection('staleCompetitions')
# competitions_ref = db.collection('competitions')
# competitors_ref = db.collection('competitors')
# users_ref = db.collection('users')
# bots_ref = db.collection('bots')

# discussions_ref = db.collection('discussions')
# threads_ref = db.collection('threads')
# comments_ref = db.collection('comments')








@app.route('/')
def test():
   return jsonify("Test Routes")


@cross_origin()
@app.route('/api/backtest', methods=['POST'])
def backtest():
    try:
        return backtest_driver(request.json)
    except Exception as e:
        return f"An Error Occurred: {e}"
    # return backtest_driver(request.json)


def strategyFactory(entryObj):

    class strategy(bt.Strategy):

        def log(self, txt, dt=None):
            ''' Logging function for this strategy'''
            dt = dt or self.datas[0].datetime.date(0)
           # print('%s, %s' % (dt.isoformat(), txt))

        def __init__(self):
            # Set a value inside the time series
            self.dataclose = self.datas[0].close

            self.sma = bt.indicators.SMA(self.datas[0].close)
            self.ema = bt.indicators.EMA(self.datas[0].close)
            self.accum = bt.indicators.Accum(self.datas[0].close)
            self.ama = bt.indicators.AdaptiveMovingAverage(self.datas[0].close)
            self.alln = bt.indicators.AllN(self.datas[0].close)
            self.anyn = bt.indicators.AnyN(self.datas[0].close)
            self.average = bt.indicators.Average(self.datas[0].close)
            self.bbands = bt.indicators.BollingerBands(self.datas[0].close)
            self.bbandspct = bt.indicators.BollingerBandsPct(self.datas[0].close)
            self.dpo = bt.indicators.DetrendedPriceOscillator(self.datas[0].close)
            self.dma = bt.indicators.DicksonMovingAverage(self.datas[0].close)
            self.dema = bt.indicators.DoubleExponentialMovingAverage(self.datas[0].close)
            self.downday = bt.indicators.DownDay(self.datas[0].close)
            self.downdaybool = bt.indicators.DownDayBool(self.datas[0].close)
            self.downmove = bt.indicators.DownMove(self.datas[0].close)
            self.envelope = bt.indicators.Envelope(self.datas[0].close)  
            self.expsmoothing = bt.indicators.ExponentialSmoothing(self.datas[0].close)
            self.ffih = bt.indicators.FindFirstIndexHighest(self.datas[0].close)
            self.ffil = bt.indicators.FindFirstIndexLowest(self.datas[0].close)
            self.flih = bt.indicators.FindLastIndexHighest(self.datas[0].close)
            self.flil = bt.indicators.FindLastIndexLowest(self.datas[0].close)
            self.highest = bt.indicators.Highest(self.datas[0].close)
            self.hull = bt.indicators.HullMovingAverage(self.datas[0].close)
            self.hurst = bt.indicators.HurstExponent(self.datas[0].close)
            self.kst = bt.indicators.KnowSureThing(self.datas[0].close)
            self.LAGF = bt.indicators.LaguerreFilter(self.datas[0].close)
            self.LRSI = bt.indicators.LaguerreRSI(self.datas[0].close)
            self.low = bt.indicators.Lowest(self.datas[0].close)
            self.macd = bt.indicators.MACD(self.datas[0].close)
            self.macdhisto = bt.indicators.MACDHisto(self.datas[0].close)
            self.meanDev = bt.indicators.MeanDeviation(self.datas[0].close)
            self.momentum = bt.indicators.MomentumOscillator(self.datas[0].close)
            self.pctchange= bt.indicators.PercentChange(self.datas[0].close)
            self.pctrank = bt.indicators.PercentRank(self.datas[0].close)
            self.ppo = bt.indicators.PercentagePriceOscillator(self.datas[0].close)
            self.pposhort = bt.indicators.PercentagePriceOscillatorShort(self.datas[0].close)
            self.priceosc = bt.indicators.PriceOscillator(self.datas[0].close)
            self.rsiema = bt.indicators.RSI_EMA(self.datas[0].close)
            self.rsisma = bt.indicators.RSI_SMA(self.datas[0].close)
            self.rsisafe = bt.indicators.RSI_Safe(self.datas[0].close)
            self.roc = bt.indicators.RateOfChange(self.datas[0].close)
            self.roc100 = bt.indicators.RateOfChange100(self.datas[0].close)
            self.rmi = bt.indicators.RelativeMomentumIndex(self.datas[0].close)
            self.rsi = bt.indicators.RelativeStrengthIndex(self.datas[0].close)
            self.smooth = bt.indicators.SmoothedMovingAverage(self.datas[0].close)
            self.stddev = bt.indicators.StandardDeviation(self.datas[0].close)
            self.sumn = bt.indicators.SumN(self.datas[0].close)
            self.trema = bt.indicators.TripleExponentialMovingAverage(self.datas[0].close)
            self.trix = bt.indicators.Trix(self.datas[0].close)
            self.trixsignal = bt.indicators.TrixSignal(self.datas[0].close)
            self.tsi = bt.indicators.TrueStrengthIndicator(self.datas[0].close)
            self.upday = bt.indicators.UpDay(self.datas[0].close)
            self.updaybool = bt.indicators.UpDayBool(self.datas[0].close)
            self.wa = bt.indicators.WeightedAverage(self.datas[0].close)
            self.wma = bt.indicators.WeightedMovingAverage(self.datas[0].close)
            self.zlema = bt.indicators.ZeroLagExponentialMovingAverage(self.datas[0].close)
            self.zlind = bt.indicators.ZeroLagIndicator(self.datas[0].close)

            self.buylist = []
            self.selllist = []

            if len(entryObj) > 1:
                self.chain = entryObj[1]['chain']
            else:
                self.chain = 'NONE'

            self.indicatorDict = {"NONE": None,
                                  "SMA": self.sma , "EMA": self.ema , "ACCUM": self.accum, "AMA": self.ama, "ALLN": self.alln, "ANYN": self.anyn, "AVERAGE": self.average 
                                   , "BBANDS": self.bbands,"BBANDSPCT": self.bbandspct, "DPO": self.dpo, "DMA": self.dma, "DEMA": self.dema, "DOWND": self.downday,
                                  "DOWNDB": self.downdaybool, "DOWNM": self.downmove, "EVE": self.envelope,"EXPSMOOTH": self.expsmoothing,"FFIH": self.ffih, "FFIL": self.ffil,
                                  "FLIH": self.flih, "FLIL": self.flil, "MAXN": self.highest, "HMA": self.hull, "HURST": self.hurst
                                  , "KST": self.kst, "LAGF": self.LAGF, "LRSI": self.LRSI, "MINN": self.LRSI, "MACD": self.macd, "MACDHISTO": self.macdhisto,
                                  "MEANDEV": self.meanDev, "MOMENTUMOSC": self.momentum, "PCTCHANGE": self.pctchange, "PCTRANK": self.pctrank, "PPO": self.ppo
                                  ,"PPOSHORT": self.pposhort, "PRICEOSC": self.priceosc, "RSIEMA":self.rsiema, "RSISMA":self.rsisma, "RSISAFE":self.rsisafe,
                                  "ROC":self.roc, "ROC100":self.roc100,  "RMI":self.rmi, "RSI":self.rsi, "SMMA":self.smooth, "STDDEV":self.stddev,
                                  "SUMN":self.sumn, "TEMA": self.trema, "TRIX": self.trix, "TRIXSIGNAL": self.trixsignal, "TSI": self.tsi, "UPDAY": self.upday,
                                  "UPDAYBOOL": self.updaybool, "WA": self.wa, "WMA": self.wma, "ZLEMA": self.zlema, "ZLIND": self.zlema}



        def buySell(self, action):
            if action == "buy":
                if self.chain == 'NONE':
                    self.buy()
                else:
                    self.buylist.append(1)
                    self.selllist.append(0)
            elif action == "sell":
                #self.sell()
                if self.chain == 'NONE':
                    self.sell()
                else:
                    self.selllist.append(1)
                    self.buylist.append(0)


        def next(self):
            for buyOrSell in entryObj:
                comparator = buyOrSell["comparator"]
                indicatorOne = buyOrSell["indicatorOne"]
                indicatorTwo = buyOrSell["indicatorTwo"]
                action = buyOrSell["action"]

                todayValue = self.dataclose[0] if indicatorOne == "NONE" else self.indicatorDict[indicatorOne][0]

                yesterdayValue = self.dataclose[-1] if indicatorTwo == "NONE" else self.indicatorDict[indicatorTwo][-1]

                if comparator == "above" and (todayValue > yesterdayValue):
                    self.buySell(action)

                elif comparator == "below" and (todayValue < yesterdayValue):
                    self.buySell(action)
            if(self.chain == "AND"):
                if math.prod(self.buylist) == 1:
                    self.buy()
                if math.prod(self.selllist) == 1:
                    self.sell
            elif(self.chain == "OR"):
                if sum(self.buylist) == 1:
                    self.buy()
                if sum(self.selllist) == 1:
                    self.sell()


    return strategy

#main points
def backtest_driver(req):
    dataDict = req

    #print(dataDict)
    entry = dataDict["entry"]
    if entry is None or len(entry) == 0:
        return "Entry is None", 400
    strategy = strategyFactory(entry)

    cerebro = bt.Cerebro()
    cerebro.broker.setcash(dataDict['cash'])
    cerebro.broker.setcommission(commission=0.0)
    cerebro.addstrategy(strategy)

    financeData = bt.feeds.YahooFinanceData(dataname=dataDict['ticker'], fromdate=parse(dataDict['startDate']),
                                            todate=parse(dataDict['endDate']))
    

    cerebro.adddata(financeData)

    response = {}
    response["startingValue"] = cerebro.broker.getvalue()
    cerebro.run()
    response["EndingValue"] = cerebro.broker.getvalue()
    response["PnL"] = response["EndingValue"] - response["startingValue"]
    response["PnLPercent"] = (response["PnL"] / response["startingValue"]) * 100

    # randFileName = f"{str(uuid.uuid4())[:8]}.png"

    # cerebro.plot()[0][0].savefig(randFileName)
    # url = uploadPhoto(randFileName)

    # if os.path.exists(randFileName):
    #     os.remove(randFileName)
    # else:
    #     print("The file does not exist")

    # response["url"] = "https://i.imgur.com/854jut8.jpg"

    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)