
    ######################           MAIN             ###################
from Quin_Mcclusky import QM
from Patrick import Patrick
from Extension_Functions import convertBin2Str
def Main():
    n_bits = int(input("Nhap vao so bit: "))
    minterm = str(input("Nhap vao cac minterms cach nhau boi dau phay: "))
    if len(minterm) == 0:
        print("Nothing.")
        return
    dontcares = str(input("Nhap vao cac dontcares: "))
    q = QM(minterm, dontcares, n_bits)
    lst, lst1, Ess, num, nonEss, lst2, lst3, s, s1, ineed, dct = q.getFinalExpression()
    print("\nExpression: ",lst)
    print("Combinations in expression: ",lst1)
    print("\nEssential: ",Ess)
    print("Combinations of Essentials: ",num)
    print("\nNon Essential: ",nonEss)
    print("Combinations of Non Essential: ",lst2)
    print("\nMinterms and dontCares were already occurred: ", s)
    print("Minterms were not occurred yet: ", s1)
    print("\nExpression need reducing laststep: ",lst3)
    print("Combinations Inneed: ", ineed)
    charEss = [convertBin2Str(i) for i in Ess]
    chs = list()
    NE = list()
    if len(ineed) == 0:
        return charEss, NE,chs
    p = Patrick(ineed)    
    NE = p.choose()
    charNonEss = list()
    for i in NE:
        temp = list()
        for k in i:
            for x,y in dct.items():
                if k == y:
                    temp.append(x)
        chs.append(temp)
    for i in chs:
        temp = list()
        for k in i:
            temp.append(convertBin2Str(k))
        charNonEss.append(temp)
    print("\nEssential implicants: ")
    for i in charEss:
        print(i)
    print("NonEssential implicants are involved in expression: ")
    print("Choose one of list below: ")
    for i in charNonEss:
        print(i)
Main()