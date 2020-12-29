from basefilter import WordFilter

''' WORD SPECIFIC FILTERS '''
    # analysis of words usually appearing in spams

    # some of the words we used are from: 
    # https://www.inc.com/geoffrey-james/how-to-avoid-a-spam-filter-5-rules.html
    
    # we use pre-calculated bayes in case train() wasn't called


class AdditionalIncomeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'additional income')
        self.bayes_val = 1.0

class BeYourOwnBossFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'be your own boss')
        self.bayes_val = 1.0

class BestPriceFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'best price')
        self.bayes_val = 1.0

class BigBucksFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'big bucks')
        self.bayes_val = -1

class BillionFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'billion')
        self.bayes_val = 0.6153846153846154

class CashBonusFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cash bonus')
        self.bayes_val = 1.0

class CentsOnTheDollarFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cents on the dollar')
        self.bayes_val = -1

class ConsolidateDebtFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'consolidate debt')
        self.bayes_val = -1

class DoubleYourCashFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'double your cash')
        self.bayes_val = -1

class DoubleYourIncomeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'double your income')
        self.bayes_val = -1

class EarnExtraCashFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'earn extra cash')
        self.bayes_val = -1

class EarnMoneyFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'earn money')
        self.bayes_val = -1

class EliminateBadCreditFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'eliminate bad credit')
        self.bayes_val = -1

class ExtraCashFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'extra cash')
        self.bayes_val = -1

class ExtraIncomeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'extra income')
        self.bayes_val = 1.0

class ExpectToEarnFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'expect to earn')
        self.bayes_val = 1.0

class FastCashFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'fast cash')
        self.bayes_val = -1

class FinancialFreedomFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'financial freedom')
        self.bayes_val = 1.0

class FreeAccessFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'free access')
        self.bayes_val = 1.0

class FreeConsultationFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'free consultation')
        self.bayes_val = -1

class FreeGiftFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'free gift')
        self.bayes_val = -1

class FreeHostingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'free hosting')
        self.bayes_val = -1

class FreeInfoFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'free info')
        self.bayes_val = 1.0

class FreeInvestmentFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'free investment')
        self.bayes_val = -1

class FreeMembershipFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'free membership')
        self.bayes_val = 1.0

class FreeMoneyFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'free money')
        self.bayes_val = 1.0

class FreePreviewFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'free preview')
        self.bayes_val = -1

class FreeQuoteFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'free quote')
        self.bayes_val = -1

class FreeTrialFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'free trial')
        self.bayes_val = 0.0

class FullRefundFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'full refund')
        self.bayes_val = 1.0

class GetOutOfDebtFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'get out of debt')
        self.bayes_val = 0.0

class GetPaidFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'get paid')
        self.bayes_val = 1.0

class GiveawayFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'giveaway')
        self.bayes_val = 0.0

class GuaranteedFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'guaranteed')
        self.bayes_val = 1.0

class IncreaseSalesFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'increase sales')
        self.bayes_val = 1.0

class IncreaseTrafficFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'increase traffic')
        self.bayes_val = 1.0

class IncredibleDealFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'incredible deal')
        self.bayes_val = -1

class LowerRatesFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'lower rates')
        self.bayes_val = -1

class LowestPriceFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'lowest price')
        self.bayes_val = 1.0

class MakeMoneyFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'make money')
        self.bayes_val = 1.0

class MillionDollarsFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'million dollars')
        self.bayes_val = 1.0

class MiracleFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'miracle')
        self.bayes_val = 1.0

class MoneyBackFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'money back')
        self.bayes_val = 1.0

class OnceInALifetimeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'once in a lifetime')
        self.bayes_val = -1

class OneTimeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'one time')
        self.bayes_val = 1.0

class PenniesADayFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'pennies a day')
        self.bayes_val = -1

class PotentialEarningsFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'potential earnings')
        self.bayes_val = -1

class PrizeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'prize')
        self.bayes_val = 0.6

class PromiseFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'promise')
        self.bayes_val = 0.7619047619047619

class PureProfitFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'pure profit')
        self.bayes_val = -1

class RiskfreeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'risk-free')
        self.bayes_val = 0.875

class SatisfactionGuaranteedFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'satisfaction guaranteed')
        self.bayes_val = 1.0

class SaveBigMoneyFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'save big money')
        self.bayes_val = -1

class SaveUpToFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'save up to')
        self.bayes_val = 1.0

class SpecialPromotionFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'special promotion')
        self.bayes_val = 1.0

class ActNowFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'act now')
        self.bayes_val = 1.0

class ApplyNowFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'apply now')
        self.bayes_val = -1

class BecomeAMemberFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'become a member')
        self.bayes_val = 1.0

class CallNowFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'call now')
        self.bayes_val = -1

class ClickBelowFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'click below')
        self.bayes_val = 1.0

class ClickHereFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'click here')
        self.bayes_val = 0.9545454545454546

class GetItNowFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'get it now')
        self.bayes_val = -1

class DoItTodayFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'do it today')
        self.bayes_val = -1

class DontDeleteFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'don’t delete')
        self.bayes_val = -1

class ExclusiveDealFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'exclusive deal')
        self.bayes_val = -1

class GetStartedNowFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'get started now')
        self.bayes_val = -1

class ImportantInformationRegardingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'important information regarding')
        self.bayes_val = -1

class InformationYouRequestedFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'information you requested')
        self.bayes_val = -1

class InstantFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'instant')
        self.bayes_val = 0.9090909090909091

class LimitedTimeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'limited time')
        self.bayes_val = 1.0

class NewCustomersOnlyFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'new customers only')
        self.bayes_val = -1

class OrderNowFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'order now')
        self.bayes_val = 1.0

class PleaseReadFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'please read')
        self.bayes_val = 1.0

class SeeForYourselfFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'see for yourself')
        self.bayes_val = 1.0

class SignUpFreeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'sign up free')
        self.bayes_val = -1

class TakeActionFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'take action')
        self.bayes_val = 1.0

class ThisWontLastFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'this won’t last')
        self.bayes_val = -1

class UrgentFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'urgent')
        self.bayes_val = 1.0

class WhatAreYouWaitingForFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'what are you waiting for?')
        self.bayes_val = 1.0

class WhileSuppliesLastFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'while supplies last')
        self.bayes_val = -1

class WillNotBelieveYourEyesFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'will not believe your eyes')
        self.bayes_val = -1

class WinnerFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'winner')
        self.bayes_val = 0.6

class WinningFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'winning')
        self.bayes_val = 0.5

class YouAreAWinnerFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'you are a winner')
        self.bayes_val = -1

class YouHaveBeenSelectedFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'you have been selected')
        self.bayes_val = -1

class BulkEmailFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'bulk email')
        self.bayes_val = 1.0

class BuyDirectFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'buy direct')
        self.bayes_val = -1

class CancelAtAnyTimeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cancel at any time')
        self.bayes_val = -1

class CheckOrMoneyOrderFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'check or money order')
        self.bayes_val = -1

class CongratulationsFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'congratulations')
        self.bayes_val = 1.0

class ConfidentialityFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'confidentiality')
        self.bayes_val = -1

class CuresFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cures')
        self.bayes_val = 0.5

class DearFriendFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'dear friend')
        self.bayes_val = -1

class DirectEmailFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'direct email')
        self.bayes_val = 1.0

class DirectMarketingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'direct marketing')
        self.bayes_val = 1.0

class HiddenChargesFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'hidden charges')
        self.bayes_val = -1

class HumanGrowthHormoneFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'human growth hormone')
        self.bayes_val = -1

class InternetMarketingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'internet marketing')
        self.bayes_val = 1.0

class LoseWeightFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'lose weight')
        self.bayes_val = 1.0

class MassEmailFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'mass email')
        self.bayes_val = -1

class MeetSinglesFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'meet singles')
        self.bayes_val = -1

class MultilevelMarketingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'multi-level marketing')
        self.bayes_val = 1.0

class NoCatchFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'no catch')
        self.bayes_val = 1.0

class NoCostFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'no cost')
        self.bayes_val = 0.9285714285714286

class NoCreditCheckFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'no credit check')
        self.bayes_val = -1

class NoFeesFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'no fees')
        self.bayes_val = -1

class NoGimmickFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'no gimmick')
        self.bayes_val = -1

class NoHiddenCostsFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'no hidden costs')
        self.bayes_val = -1

class NoHiddenFeesFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'no hidden fees')
        self.bayes_val = -1

class NoInterestFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'no interest')
        self.bayes_val = 1.0

class NoInvestmentFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'no investment')
        self.bayes_val = -1

class NoObligationFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'no obligation')
        self.bayes_val = 1.0

class NoPurchaseNecessaryFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'no purchase necessary')
        self.bayes_val = -1

class NoQuestionsAskedFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'no questions asked')
        self.bayes_val = 1.0

class NoStringsAttachedFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'no strings attached')
        self.bayes_val = -1

class NotJunkFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'not junk')
        self.bayes_val = -1

class NotspamFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'notspam')
        self.bayes_val = -1

class ObligationFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'obligation')
        self.bayes_val = 0.9666666666666667

class PasswordsFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'passwords')
        self.bayes_val = 0.0

class RequiresInitialInvestmentFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'requires initial investment')
        self.bayes_val = -1

class SocialSecurityNumberFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'social security number')
        self.bayes_val = -1

class ThisIsntAScamFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'this isn’t a scam')
        self.bayes_val = -1

class ThisIsntJunkFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'this isn’t junk')
        self.bayes_val = -1

class ThisIsntSpamFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'this isn’t spam')
        self.bayes_val = -1

class UndisclosedFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'undisclosed')
        self.bayes_val = 0.8

class UnsecuredCreditFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'unsecured credit')
        self.bayes_val = -1

class UnsecuredDebtFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'unsecured debt')
        self.bayes_val = -1

class UnsolicitedFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'unsolicited')
        self.bayes_val = 0.7272727272727273

class ValiumFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'valium')
        self.bayes_val = -1

class ViagraFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'viagra')
        self.bayes_val = 1.0

class VicodinFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'vicodin')
        self.bayes_val = -1

class WeHateSpamFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'we hate spam')
        self.bayes_val = -1

class WeightLossFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'weight loss')
        self.bayes_val = 1.0

class XanaxFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'xanax')
        self.bayes_val = -1

class AcceptCreditCardsFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'accept credit cards')
        self.bayes_val = 1.0

class AdFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'ad')
        self.bayes_val = 0.7490494296577946

class AllNewFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'all new')
        self.bayes_val = 1.0

class AsSeenOnFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'as seen on')
        self.bayes_val = -1

class BargainFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'bargain')
        self.bayes_val = 1.0

class BeneficiaryFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'beneficiary')
        self.bayes_val = 1.0

class BillingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'billing')
        self.bayes_val = 0.8

class BonusFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'bonus')
        self.bayes_val = 0.9285714285714286

class CardsAcceptedFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cards accepted')
        self.bayes_val = -1

class CashFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cash')
        self.bayes_val = 0.926829268292683

class CertifiedFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'certified')
        self.bayes_val = 1.0

class CheapFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'cheap')
        self.bayes_val = 0.5833333333333334

class ClaimsFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'claims')
        self.bayes_val = 0.8461538461538461

class ClearanceFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'clearance')
        self.bayes_val = 1.0

class CompareRatesFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'compare rates')
        self.bayes_val = 1.0

class CreditCardOffersFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'credit card offers')
        self.bayes_val = -1

class DealFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'deal')
        self.bayes_val = 0.7857142857142857

class DebtFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'debt')
        self.bayes_val = 0.8461538461538461

class DiscountFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'discount')
        self.bayes_val = 0.782608695652174

class FantasticFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'fantastic')
        self.bayes_val = 0.25

class InAccordanceWithLawsFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'in accordance with laws')
        self.bayes_val = -1

class IncomeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'income')
        self.bayes_val = 0.975609756097561

class InvestmentFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'investment')
        self.bayes_val = 0.875

class JoinMillionsFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'join millions')
        self.bayes_val = -1

class LifetimeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'lifetime')
        self.bayes_val = 1.0

class LoansFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'loans')
        self.bayes_val = 1.0

class LuxuryFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'luxury')
        self.bayes_val = 1.0

class MarketingSolutionFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'marketing solution')
        self.bayes_val = -1

class MessageContainsFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'message contains')
        self.bayes_val = -1

class MortgageRatesFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'mortgage rates')
        self.bayes_val = 1.0

class NameBrandFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'name brand')
        self.bayes_val = -1

class OfferFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'offer')
        self.bayes_val = 0.9202898550724637

class OnlineMarketingFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'online marketing')
        self.bayes_val = -1

class OptInFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'opt in')
        self.bayes_val = 1.0

class PreapprovedFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'pre-approved')
        self.bayes_val = -1

class QuoteFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'quote')
        self.bayes_val = 0.9202127659574468

class RatesFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'rates')
        self.bayes_val = 0.8444444444444444

class RefinanceFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'refinance')
        self.bayes_val = 1.0

class RemovalFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'removal')
        self.bayes_val = 0.9777777777777777

class ReservesTheRightFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'reserves the right')
        self.bayes_val = 1.0

class ScoreFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'score')
        self.bayes_val = 0.0

class SearchEngineFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'search engine')
        self.bayes_val = 0.8461538461538461

class SentInComplianceFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'sent in compliance')
        self.bayes_val = 1.0

class SubjectToFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'subject to')
        self.bayes_val = 0.7692307692307693

class TermsAndConditionsFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'terms and conditions')
        self.bayes_val = 1.0

class TrialFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'trial')
        self.bayes_val = 0.5714285714285714

class UnlimitedFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'unlimited')
        self.bayes_val = 0.9285714285714286

class WarrantyFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'warranty')
        self.bayes_val = 0.8571428571428571

class WebTrafficFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'web traffic')
        self.bayes_val = -1

class WorkFromHomeFilter(WordFilter):
    def __init__(self):
        WordFilter.__init__(self, 'work from home')
        self.bayes_val = 1.0

# class CostFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'cost')
#         self.bayes_val = 0.80
        
# class AdditionalIncomeFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'additional income')
#         self.bayes_val = 1.0
        
# class ClickFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'click')   
#         self.bayes_val = 0.80
          
# class SelectedFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'selected')
#         self.bayes_val = 0.77
        
# class NowFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'now')
#         self.bayes_val = 0.75
        
# class BeYourOwnBossFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'be your own boss')
#         self.bayes_val = 1.0
        
# class NigerianPrinceFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'nigerian prince')
#         self.bayes_val = 1.0

# class PercentFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, '%')
#         self.bayes_val = 0.9
        
# class BuyFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'buy')
#         self.bayes_val = 0.79
        
# class PokerFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'poker')
#         self.bayes_val = 1.0
        
# class GambleFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'gamble')
#         self.bayes_val = 1.0
        
# class GamblingFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'gambling')
#         self.bayes_val = 0.88
        
# class SignUpFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'sign up')
#         self.bayes_val = 0.75
        
# class CustomerServiceFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'customer service')
#         self.bayes_val = 0.88
        
# class GameFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'game') 
#         self.bayes_val = 0.55      
        
# class InsuranceFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'insurance')
#         self.bayes_val = 0.98
        
# class PlayFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'play')
#         self.bayes_val = 0.56
                
# class CassinoFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'cassino')
#         self.bayes_val = 0.8
        
# class BankAccountFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'bank account')
#         self.bayes_val = 0.83

# class PayFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'pay')
#         self.bayes_val = 0.83
        
# class Password(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'password')
#         self.bayes_val = 0.37

# class InheritFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'inherit')
#         self.bayes_val = 0.5

# class HeritageFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'heritage')
#         self.bayes_val = 0.3
        
# class SaleFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'sale')
#         self.bayes_val = 0.86

# class SubscriberFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'subscriber')
#         self.bayes_val = 0.9

# class SmokingFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'smoking')
#         self.bayes_val = 0.8

# class TobaccoFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'tobacco')
#         self.bayes_val = 1.0

# class OrderFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'order')
#         self.bayes_val = 0.9

# class OrderNowFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'order now')
#         self.bayes_val = 1.0

# class AdvertisementFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'advertisement')
#         self.bayes_val = 0.83
        
# class BusinessFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'business')
#         self.bayes_val = 0.96
        
# class CashFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'cash')
#         self.bayes_val = 0.93
        
# class CheapFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'cheap')
#         self.bayes_val = 0.58
        
# class CommodityFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'commodity')
#         self.bayes_val = -1
        
# class CongratulationsFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'congratulations')
#         self.bayes_val = 0.8
        
# class CreditFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'credit')
#         self.bayes_val = 0.87
        
# class DealFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'deal')  
#         self.bayes_val = 0.78
                
# class DebtFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'debt')
#         self.bayes_val = 0.84
         
# class DegreeFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'degree')
#         self.bayes_val = 0.5
        
# class DisclaimerFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'disclaimer')
#         self.bayes_val = 0.5
         
# class DiscountFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'discount')
#         self.bayes_val = 0.5
         
# class FreeFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'free')
#         self.bayes_val = 0.735
         
# class GimmickFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'gimmick')
#         self.bayes_val = -1
         
# class GuaranteeFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'guarantee')
#         self.bayes_val = 0.97
    
# class IncomeFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'income')
#         self.bayes_val = 0.97
         
# class InkFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'ink')
#         self.bayes_val = 0.75
         
# class InvestmentFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'investment')
#         self.bayes_val = 0.875
         
# class JokeFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'joke')
#         self.bayes_val = 0.5
         
# class LoadFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'load')
#         self.bayes_val = 0.6
         
# class MarketingFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'marketing')
#         self.bayes_val = 0.97
         
# class MerchantFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'merchant')
#         self.bayes_val = 0.91
 
# class ObligationFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'obligation')
#         self.bayes_val = 0.96
  
# class OfferFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'offer')
#         self.bayes_val = 0.92
  
# class OptFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'opt')
#         self.bayes_val = 0.86
  
# class OpportunityFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'opportunity')
#         self.bayes_val = 0.94
  
# class OutstandingFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'outstanding')
#         self.bayes_val = 1.0
  
# class PayoffFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'payoff')
#         self.bayes_val = -1
  
# class PriceFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'price')
#         self.bayes_val =  0.88
  
# class ProfitFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'profit')
#         self.bayes_val = 0.8
  
# class PromoFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'promo')
#         self.bayes_val = 0.8
  
# class PromotionFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'promotion')
#         self.bayes_val = 0.88
  
# class RateFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'rate')
#         self.bayes_val =  0.78
  
# class RefundFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'refund')
#         self.bayes_val = 1.0
  
# class RichFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'rich')
#         self.bayes_val =  0.71
  
# class SalesFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'sales')
#         self.bayes_val = 0.88
  
# class SaveFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'save')
#         self.bayes_val = 0.9
  
# class ShopFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'shop')
#         self.bayes_val = 0.77
  
# class SpamFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'spam')
#         self.bayes_val =  0.7
  
# class SpreeFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'spree')
#         self.bayes_val = 1.0
  
# class StockFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'stock')
#         self.bayes_val = 0.72
  
# class SubscribeFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'subscribe')
#         self.bayes_val = 0.57
  
# class TradingFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'trading')
#         self.bayes_val = 1.0
  
# class WealthFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'wealth')
#         self.bayes_val = 0.88
  
# class WinFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'win')
#         self.bayes_val = 0.82
  
# class WinnerFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'winner')
#         self.bayes_val = 0.6
  
# class WinningFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'winning')
#         self.bayes_val = 0.5
  
# class WonFilter(WordFilter):
#     def __init__(self):
#         WordFilter.__init__(self, 'won')
#         self.bayes_val = 0.77
