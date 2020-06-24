
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

#RawString = """ 於本實施例中，自動清潔機200更包含一幫浦模組330、一控制模組340及一電源模組390。電源模組390用以提供一電源給幫浦模組330及控制模組340。幫浦模組330驅動真空吸塵裝置（未圖示）進行真空吸塵，從吸塵口331吸入灰塵後將灰塵收集在集塵帶（未圖示）中。距離感測器210電連接於控制模組340，用以傳送一距離資料給控制模組340。控制模組340包含一編碼器341、一馬達模組342、一陀螺儀343、一處理器（CPU）344及存儲器345。馬達模組342驅動行走裝置223，使自動清潔機200前後移動或左右轉動。更具體而言，馬達模組342連接該些輪子231，並驅動該些輪子23旋轉進而帶動皮帶232轉動。馬達模組342電連接有一個編碼器341（Encoder），編碼器341依據馬達模組342的一操作信號，以求得行走距離或轉彎角度。由編碼器341的讀值可計算出自動清潔機200行走的距離或轉彎的角度。控制模組340的陀螺儀343用以量測的自動清潔機200的角速度(ω)，然後對角速度(ω)的積分而得到機器的積分角度(iA)，如下公式eq1。編碼器341依據行走距離、轉彎的角度及積分角度(iA)至少其中之一作出慣性導航（inertial navigation），並且進行“弓字型”來回清掃。"""
#string = RawString

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


