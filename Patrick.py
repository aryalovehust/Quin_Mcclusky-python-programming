class Patrick():
    
    def __init__(self,lst):
        self.lst = lst    
        
    #### CHOOSE NON ESSENTIAL
    def choose(self):
        s = 0
        c = len(self.lst)
        lst1 = list()
        for i in range(0,c):
            lst1.append(len(self.lst[i]))
        s = min(lst1)
        last = list()
        last = [i for i in self.lst if len(i) == s]
        return last
    