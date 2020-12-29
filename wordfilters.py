from basefilter import WordFilter

''' WORD SPECIFIC FILTERS '''
    # analysis of words usually appearing in spams 
    # list of some of the words we used is from: 
    # https://www.inc.com/geoffrey-james/how-to-avoid-a-spam-filter-5-rules.html
    # we addes pre-calculated bayes in case train() wasn't called
    
class CostFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cost')
        self.bayes_val = 0.80
        
class AdditionalIncomeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'additional income')
        self.bayes_val = 1.0
        
class ClickFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'click')   
        self.bayes_val = 0.80
          
class SelectedFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'selected')
        self.bayes_val = 0.77
        
class NowFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'now')
        self.bayes_val = 0.75
        
class BeYourOwnBossFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'be your own boss')
        self.bayes_val = 1.0
        
class NigerianPrinceFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'nigerian prince')
        self.bayes_val = 1.0

class PercentFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, '%')
        self.bayes_val = 0.9
        
class BuyFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'buy')
        self.bayes_val = 0.79
                
class CostFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cost')
        self.bayes_val = 0.8
        
class PokerFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'poker')
        self.bayes_val = 1.0
        
class GambleFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'gamble')
        self.bayes_val = 1.0
        
class GamblingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'gambling')
        self.bayes_val = 0.88
        
class SignUpFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'sign up')
        self.bayes_val = 0.75
        
class CustomerServiceFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'customer service')
        self.bayes_val = 0.88
        
class GameFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'game') 
        self.bayes_val = 0.55      
        
class InsuranceFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'insurance')
        self.bayes_val = 0.98
        
class PlayFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'play')
        self.bayes_val = 0.56
                
class CassinoFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cassino')
        self.bayes_val = 0.8
        
class BankAccountFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'bank account')
        self.bayes_val = 0.83

class PayFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'pay')
        self.bayes_val = 0.83
        
class Password(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'password')
        self.bayes_val = 0.37

class InheritFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'inherit')
        self.bayes_val = 0.5

class HeritageFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'heritage')
        self.bayes_val = 0.3
        
class SaleFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'sale')
        self.bayes_val = 0.86

class SubscriberFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'subscriber')
        self.bayes_val = 0.9

class SmokingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'smoking')
        self.bayes_val = 0.8

class TobaccoFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'tobacco')
        self.bayes_val = 1.0

class OrderFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'order')
        self.bayes_val = 0.9

class OrderNowFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'order now')
        self.bayes_val = 1.0

class AdvertisementFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'advertisement')
        self.bayes_val = 0.83
        
class BusinessFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'business')
        self.bayes_val = 0.96
        
class CashFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cash')
        self.bayes_val = 0.93
        
class CheapFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cheap')
        self.bayes_val = 0.58
        
class CommodityFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'commodity')
        self.bayes_val = -1
        
class CongratulationsFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'congratulations')
        self.bayes_val = -1
        
class CreditFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'credit')
        self.bayes_val = 0.87
        
class DealFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'deal')  
        self.bayes_val = 0.78
                
class DebtFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'debt')
        self.bayes_val = 0.84
         
class DegreeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'degree')
        self.bayes_val = 0.5
        
class DisclaimerFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'disclaimer')
        self.bayes_val = 0.5
         
class DiscountFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'discount')
        self.bayes_val = 0.5
         
class FreeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'free')
        self.bayes_val = 0.735
         
class GimmickFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'gimmick')
        self.bayes_val = -1
         
class GuaranteeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'guarantee')
        self.bayes_val = 0.97
    
class IncomeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'income')
        self.bayes_val = 0.97
         
class InkFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'ink')
        self.bayes_val = 0.75
         
class InvestmentFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'investment')
        self.bayes_val = 0.875
         
class JokeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'joke')
        self.bayes_val = 0.5
         
class LoadFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'load')
        self.bayes_val = 0.6
         
class MarketingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'marketing')
        self.bayes_val = 0.97
         
class MerchantFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'merchant')
        self.bayes_val = 0.91
 
class ObligationFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'obligation')
        self.bayes_val = 0.96
  
class OfferFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'offer')
        self.bayes_val = 0.92
  
class OptFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'opt')
        self.bayes_val = 0.86
  
class OpportunityFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'opportunity')
        self.bayes_val = 0.94
  
class OutstandingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'outstanding')
        self.bayes_val = 1.0
  
class PayoffFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'payoff')
        self.bayes_val = -1
  
class PriceFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'price')
        self.bayes_val =  0.88
  
class ProfitFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'profit')
        self.bayes_val = 0.8
  
class PromoFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'promo')
        self.bayes_val = 0.8
  
class PromotionFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'promotion')
        self.bayes_val = 0.88
  
class RateFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'rate')
        self.bayes_val =  0.78
  
class RefundFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'refund')
        self.bayes_val = 1.0
  
class RichFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'rich')
        self.bayes_val =  0.71
  
class SalesFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'sales')
        self.bayes_val = 0.88
  
class SaveFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'save')
        self.bayes_val = 0.9
  
class ShopFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'shop')
        self.bayes_val = 0.77
  
class SpamFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'spam')
        self.bayes_val =  0.7
  
class SpreeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'spree')
        self.bayes_val = 1.0
  
class StockFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'stock')
        self.bayes_val = 0.72
  
class SubscribeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'subscribe')
        self.bayes_val = 0.57
  
class TradingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'trading')
        self.bayes_val = 1.0
  
class WealthFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'wealth')
        self.bayes_val = 0.88
  
class WinFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'win')
        self.bayes_val = 0.82
  
class WinnerFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'winner')
        self.bayes_val = 0.6
  
class WinningFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'winning')
        self.bayes_val = 0.5
  
class WonFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'won')
        self.bayes_val = 0.77

    