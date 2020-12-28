from constants import POSITIVE, NEGATIVE
from basefilter import BaseFilter, WordFilter
from collections import Counter
from corpus import Corpus
from trainingcorpus import TrainingCorpus

    # analysis of words usually appearing in spams 
    # list of words we used is from: 
    # https://www.inc.com/geoffrey-james/how-to-avoid-a-spam-filter-5-rules.html
class AdvertisementFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'advertisement')
        
class BusinessFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'business')
        
class CashFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cash')
        
class CheapFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cheap')
        
class CommodityFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'commodity')
        
class Congratulations(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'congratulations')
        
class CreditFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'credit')
        
class DealFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'deal')     
                
class DebtFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'debt')
         
class DegreeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'degree')
        
class DisclaimerFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'disclaimer')
         
class DiscountFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'discount')
         
class FreeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'free')
         
class GimmickFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'gimmick')
         
class GuaranteeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'guarantee')
    
class IncomeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'income')
         
class InkFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'ink')
         
class InvestmentFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'investment')
         
class JokeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'joke')
         
class Load(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'load')
         
class Marketing(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'marketing')
         
class MerchantFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'merchant')
 
class Obligation(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'obligation')
  
class OfferFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'offer')
  
class OptFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'opt')
  
class OpportunityFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'opportunity')
  
class Outstanding(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'outstanding')
  
class PayoffFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'payoff')
  
class Price(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'price')
  
class Profit(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'profit')
  
class Promo(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'promo')
  
class Promotion(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'promotion')
  
class RateFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'rate')
  
class RefundFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'refund')
  
class Rich(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'rich')
  
class Sales(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'sales')
  
class SaveFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'save')
  
class ShopFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'shop')
  
class SpamFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'spam')
  
class SpreeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'spree')
  
class StockFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'stock')
  
class Subscribe(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'subscribe')
  
class Trading(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'trading')
  
class Wealth(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'wealth')
  
class WinFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'win')
  
class WinnerFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'winner')
  
class WinningFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'winning')
  
class WonFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'won')

        
if __name__ == "__main__":
    
    a = WonFilter()
    c = TrainingCorpus('./1')
    a.train(c)
    print(a.word_in_hams)
    print(a.word_in_spams)
    