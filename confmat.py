pos_tag = 'SPAM'
neg_tag = 'OK'

class BinaryConfusionMatrix:
    
    def __init__(self, pos_tag, neg_tag):
        self.pos_tag = pos_tag
        self.neg_tag = neg_tag
        self.tp = 0
        self.tn = 0
        self.fp = 0
        self.fn = 0
        
    def check_value_of(self, value):
        if value not in (self.pos_tag, self.neg_tag):
            raise ValueError('The "truth" atribute can be either %s or %s' \
            % (self.pos_tag, self.neg_tag))        
        
    def update(self, reality, predict): 
        self.check_value_of(reality)
        self.check_value_of(predict) 
        if reality == predict:
            if reality == self.pos_tag:
                self.tp += 1
            else:
                self.tn += 1           
        else:
            if reality == self.neg_tag:
                self.fp += 1
            else:
                self.fn += 1
                
    def as_dict(self):
        return {"tp" : self.tp, "tn" : self.tn, "fp" : self.fp, "fn" : self.fn}   
        
    def compute_from_dicts(self, truth_dict, pred_dict):
        for email in truth_dict.keys():
            self.update(truth_dict[email], pred_dict[email])  
        return self.as_dict                                                      
              