##### CHUYỂN 1 SỐ THẬP PHÂN SANG 1 SỐ NHỊ PHÂN N BITS
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

#### KIỂM TRA XEM CÁC MINTERMS TRONG DANH SÁCH S CÓ MẶT ÍT NHẤT 1 LẦN TRONG DANH SÁCH CÁC TỔ HỢP TP
def sastify(tp, s):
    for i in range(0,len(s)):
        c = 0
        for k in range(0,len(tp)): 
            if s[i] in tp[k]:
                c = c + 1
        if c == 0:
            return False
    return True

##### ĐẾM SỐ SỐ 1 TRONG SỐ NHỊ PHÂN N
def count1s(n):
    return n.count("1")

##### CHUYỂN 1 SỐ NHỊ PHÂN SANG DẠNG KÝ TỰ ABC
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
    