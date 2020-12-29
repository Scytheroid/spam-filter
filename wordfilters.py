from basefilter import WordFilter

''' WORD SPECIFIC FILTERS '''
    # analysis of words usually appearing in spams 
    # list of words we used is from: 
    # https://www.inc.com/geoffrey-james/how-to-avoid-a-spam-filter-5-rules.html
class PercentFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, '%')
        
class BuyFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'buy')
                
class Game(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'game')
        
class Play(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'play')
                
class CassinoFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cassino')
        
class BankAccountFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'bank account')
        
class OccasionFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'occasion')
        
class PayFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'pay')
        
class Password(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'password')

class InheritFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'inherit')

class HeritageFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'heritage')
        
class SaleFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'sale')

class SubscriberFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'subscriber')

class SmokingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'smoking')

class TobaccoFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'tobacco')

class OrderFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'order')

class OrderNowFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'order now')

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
        
class CongratulationsFilter(WordFilter):
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
         
class LoadFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'load')
         
class MarketingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'marketing')
         
class MerchantFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'merchant')
 
class ObligationFilter(WordFilter):
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
  
class OutstandingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'outstanding')
  
class PayoffFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'payoff')
  
class PriceFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'price')
  
class ProfitFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'profit')
  
class PromoFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'promo')
  
class PromotionFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'promotion')
  
class RateFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'rate')
  
class RefundFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'refund')
  
class RichFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'rich')
  
class SalesFilter(WordFilter):
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
  
class SubscribeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'subscribe')
  
class TradingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'trading')
  
class WealthFilter(WordFilter):
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