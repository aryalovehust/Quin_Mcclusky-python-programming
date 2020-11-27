def convert(n,n_bits):
    return '{0:04b}'.format(n)

def compare(lst1, lst2):
    a = 0
    for i in lst2:
        if i not in lst1:
            a = a + 1
    if a == 0:
        return False
    return True

def sastify(tp, s):
    for i in range(0,len(s)):
        c = 0
        for k in range(0,len(tp)): 
            if s[i] in tp[k]:
                c = c + 1
        if c == 0:
            return False
    return True

def count1s(n):
    return n.count("1")

def convertBin2Str(st):
    t = "ABCDEFGHIJKLMNOPQ"
    char = t[:len(st)]
    jet = []
    for i in range(0, len(st)):
        if st[i] == "1":
            jet.append(char[i])
        if st[i] == "0":
            jet.append(char[i] + "'")
    return "".join(jet)
    

class QM():
    
    def __init__(self, mt, dc, n_bits):
        self.n_bits = n_bits
        self.sum_min = [int(i) for i in mt.split(',')]
        if len(dc) != 0:
            self.d_c = [int(i) for i in dc.split(',')]
        else:
            self.d_c = []
        total = set(self.sum_min) | set(self.d_c)
        self.minterm = [convert(i,n_bits) for i in self.sum_min]
        self.altogether = [convert(i, n_bits) for i in total]
        self.minterm.sort(key = count1s)
        self.altogether.sort(key = count1s)
        self.irr = set()

    def simplify(self, t1, t2):
        c = 0
        ret = []
        for x,y in zip(t1,t2):
            if x != y:
                c = c + 1
                ret.append("-")
            else:
                ret.append(x)
        if c != 1:
            return None
        else:
            return "".join(ret)
        
    def useless(self, t1, t2):    
        for x,y in zip(t1, t2):
            if x != y:
                if y != "-":
                    return False
        return True
    
    def firstStep(self):
        lst = list()
        for i in range(0, len(self.altogether)):
            for k in range(i, len(self.altogether)):
                if self.simplify(self.altogether[i], self.altogether[k]) != None:
                    lst.append(self.simplify(self.altogether[i], self.altogether[k]))
        return set(lst)
    
    def moderate(self, lst1, lst2):
        for i in lst1:
            c = 0
            for k in lst2:
                if not self.useless(i, k):
                    c = c + 1
            if c == len(lst2):
                self.irr.add(i)
                
    def reduce(self, lst):
        lst1  = list()
        s = len(lst)
        c = 0
        for i in range(0, s):
            for k in range(i, s):
                if self.simplify(lst[i], lst[k]) != None:
                    lst1.append(self.simplify(lst[i], lst[k]))
                    c = c + 1
        if c == 0 :
            return lst
        self.moderate(lst,lst1)
        return set(lst1)
    
    def simplifyExpression(self):
        lst = list(self.firstStep())
        self.moderate(self.minterm, lst)
        while self.reduce(lst) != lst:
            lst = list(self.reduce(lst))
        return lst
    
    def getFinalExpression(self):
        
        ### Get expression ['10--', '1--0', '1-1-', '-100'] : LST
        lst = self.simplifyExpression()
        lst = lst + list(self.irr)
        
        #### GET COMBINATION OF EXPRESSION : LST1
        lst1 = list()
        dct = dict()
        sum_min = [int(i) for i in self.sum_min ]
        d_c = [int(i) for i in self.d_c]
        comb = list()
        comb = sum_min + d_c
        for i in lst:
            temp = list()
            for k in comb:
                if self.useless(convert(k,self.n_bits),i):
                    temp.append(k)
            lst1.append(temp)
            dct.update({i:temp})
         #### GET ESSENTIAL : ESS AND NUM
        Ess = list()
        num = list()
        for i in sum_min :
            c = 0
            temp = 0
            for k in range(0,len(lst1)):
                if i in lst1[k]:
                    c = c + 1         
                    temp = k
            if c == 1:
                Ess.append(lst[temp])
        Ess1 = set(Ess)
        Ess = list(Ess1)
        for i in Ess:
            temp = list()
            for k in comb:
                if self.useless(convert(k,self.n_bits),i):
                    temp.append(k)
            num.append(temp)        
            
        ##### GET MINTERMS WHICH WERE ALREADY OCCURRED : S
        s = set()              
        for i in num:
            s = s | set(i) 
        s = list(s) 
        
        ##### GET NONE_ESSENTIAL AND COMBINATIONS OF NONE_ESSENTIAL EXPRESSION : NONESS AND LST2
        lst2 = list()
        nonEss = [i for i in lst if i not in Ess]
        for i in nonEss:
            temp = list()
            for k in comb:
                if self.useless(convert(k, self.n_bits),i):
                    temp.append(k)
            lst2.append(temp)
            
        #### GET COMBINATION OF EXPRESSION NEED REDUCING LASTSTEP : LST3
        lst3 = list()
        for m in range(0,len(lst1)):
            if compare(s, lst1[m]):
                lst3.append(lst1[m])
                
        #### GET MINTERMS WHICH WERE NOT OCCURRED YET : S1
        s1 = set()
        for i in lst3:
            s1 = s1 | set(i)
        s1 = [i for i in s1 if i not in s and i not in d_c]
        
        #### GET FINNAL EXPRESSION
        from itertools import combinations
        combin = list()
        lst3.sort(key=len)
        for i in range(1,len(lst3) + 1):
            comb = combinations(lst3, i)
            combin = combin + list(comb)
        ineed = list()
        combin = [list(i) for i in combin]
        for i in combin:
            if sastify(i, s1):
                ineed.append(i)
        return lst, lst1, Ess,num, nonEss, lst2, lst3, s, s1, ineed, dct