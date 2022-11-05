class Archer:
    def __init__(self,bowtype,gender,age_cat):
        self.bowtype = bowtype.lower()
        self.gender = gender.lower()
        self.age_cat = age_cat
        
    def get_bowtype(self):
        return self.bowtype
    def get_gender(self):
        return self.gender
    def get_age_cat(self):
        return self.age_cat
    
    def __repr__(self):
        return f"Bowtype: {self.bowtype}, Gender: {self.gender}, Age: {self.age_cat}."
        


