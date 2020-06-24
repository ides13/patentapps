
# coding: utf-8

###############

def FindSame(string_a, string_b):
    import difflib
    matcher = difflib.SequenceMatcher(a=string_a, b=string_b)
    match = matcher.find_longest_match(0, len(matcher.a), 0, len(matcher.b))
    same = matcher.a[match.a:match.a+match.size]
    return same
###############


def printdict(dict):
    for key in sorted(dict):
        print(key, '-->', dict[key])              
###############


def MergeDict(dic1, dic2):
    dic={}
    for key in dic1:
        if dic2[key] is not None:
            dic[key]=dic1[key]+dic2[key]
        else:
            dic[key]=dic1[key]
          
    for key in dic2:
        if dic[key] is None:
            dic[key]=dic2[key]
    return dic
###############

file = open('datafile.txt', 'r', encoding = 'utf-8-sig')
string = file.read()

###############
import re
pattern = '[0-9a-zA-Z]+'
Index= '元件符號'
Word_dict = {}
Word_2_dict = {}
Word = '【【】】'
#string = re.sub('\n+', '', string)
string = re.sub('【[0-9]+】', '', string)
string = re.sub('[圖图][0-9a-zA-Z]+', '', string)
string = re.sub('[第][0-9a-zA-Z]+[圖图]', '', string)

while True:
    m = re.search(pattern, string)
    if m is None:  # 在這邊卡很久，找不到時，不能夠用「m.group函數」
        break
    else:
        Index = m.group()  # Index = string[m.start():m.end()]

    #處理元件符號及對應用語
    if m.start() > 9:                                                 # Str前面的字元小於10時會沒有字串, 0>1。
        Word = string[m.start()-10:m.start()]
    elif m.start() > 1:
        Word = string[:m.start()]
    else:
        Tempstring = Word+m.group()+string[m.end():]
        #Tempstring = Word+string[m.end():]
        Word = Tempstring[:10]

    string = string[m.end():]
    
    #加入字典
    if Index in Word_dict:
        WordSame = FindSame(Word_dict[Index], Word)
        if WordSame is not '':Word_dict.update({Index:WordSame})        #當兩字串沒有相同字元時，會出現“空的值”
        if WordSame is not '':Word_2_dict[Index].append(Word) 
    else:
        Word_dict[Index] = Word
        Word_2_dict[Index] = [Word]       
############____End_While____

####################################
#Temp_Dict為具有相同用語之list的字典。
#ddd為合併的字典。
####################################

Temp_list=[]
Temp_Dict={}

for Index in Word_2_dict:
    for i in range(0,len(Word_2_dict[Index])-1):
        Temp_list.append(FindSame(Word_2_dict[Index][i], Word_2_dict[Index][i+1]))
    Temp_Dict[Index]=Temp_list
    Temp_list=[]
    
ddd = MergeDict(Temp_Dict, Word_2_dict)
      
file.close()

from collections import Counter
F = open('workfile.txt','w', encoding = 'utf-8-sig')

for Index in sorted(ddd):
    words=ddd[Index]
    most_common_words= [word for word, word_count in Counter(words).most_common(1)]
    #print(Index, '：', str(most_common_words)[2:-2])
    
    F.write(Index)
    F.write("""：""")
    F.write(str(most_common_words)[2:-2])
    F.write("\n")
F.close()

####################################
#第一版本。
#可以檢索「Word_dict」。
####################################
F = open('workfile_v1.txt','w', encoding = 'utf-8-sig')

for Index in sorted(Word_dict):
    #print (Index, Word_dict[Index])
    F.write(Index)
    F.write("""：""")
    F.write(Word_dict[Index])
    F.write("\n")
F.close()


