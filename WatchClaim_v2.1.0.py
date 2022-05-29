# -*- coding: utf-8 -*-
"""
Created on Sat May 28 17:27:00 2022

@author: ides1

以「一種」及「如請求項」，作為計算請求項編號的算法。
"""

s = '''

001:自動清潔設備；003:柔性牽引機構；004:柔性牽引機構；005:柔性牽引機構；006:懸掛機構；007:懸掛機構；008:升降機構；010:驅動結構；011:驅動結構；012:驅動結構；100:移動平臺；101:底面；120:控制模組；130:傳感器模組；132:鐳射雷達；134:傳感器；136:攝影機；138:電容觸頭；139:機械觸頭；140:驅動模組；142:輪子；144:轉向機構；146:動力系統；200:升降臺；201:底面；202:升降機構；207:升降臺基座；208:連接杆；210:懸掛機構；220:第一線纜；221:第一端；222:第二端；230:線纜導軌；231:第一導向槽拐角；232:第二導向槽拐角；233:定滑輪；235:第一導向凸起；236:第二導向凸起；240:驅動機構；242:動力裝置；244:驅動輪；244b:捲筒；244c:捲筒；245:樞軸；246:驅動耦合器；247:齒條；247a:滑動端；247b:連接端；249:線纜；251:第二線纜；271:第一連接端；272:第二連接端；274:下表面；275:第一側；276:第二側；277:滑槽；278:輔助輪；281:第一鉸接端；283:第二鉸接端；291:直線驅動機構；300:清潔模組；320:清潔頭；322:清潔頭基板；324:作業頭；325:滑塊；326:滑動端；327:回轉端；328:彈性支撑結構；329:樞軸；330:驅動單元；332:引擎；334:驅動輪；336:齒輪機構；344:滑槽；362:清潔頭基板；364:滑槽；365:滑塊；366:滑動端；367:回轉端；369:樞軸；371:樞軸；372:清潔頭基板；373:連杆；374:回轉端；375:滑動端；376:滑塊；377:滑塊；378:滑槽；379:滑槽；380:樞軸；381:樞軸；382:清潔頭基板；383:樞軸；384:驅動輪；400:給水模組；410:儲存裝置；420:分配器；421:分配口；440:給水驅動裝置；500:回收模組；510:輥子；511:彈性吸水材料；520:輥子驅動裝置；540:回收組件；541:刮板；543:回收槽；544:回收口；545:回收倉；546:葉片；547:回收驅動裝置；548:葉片驅動裝置；549:濾網；700:吸塵模組；A:樞轉中心；A’:樞轉中心；O:回轉中心；O’:回轉中心；S600:方法；S610:步驟；S620:步驟；S630:步驟；S640:步驟；S650:步驟；S660:步驟；S680:步驟；V:線速度；V0:移動速度
549:回收葉片
 


'''

claims = '''

1.一種自動清潔設備，包括： 移動平臺，被配置爲在操作面上自動沿著目標方向移動； 清潔模組，安裝在該移動平臺上，包括： 乾式清潔模組，同該移動平臺連接，被配置爲採用乾式清潔方式清潔該操作面； 濕式清潔模組，同該移動平臺連接，被配置爲配合清潔液採用濕式清潔方式清潔該操作面；以及 回收模組，同該移動平臺連接，並被配置爲回收該清潔液。

2.如請求項1的自動清潔設備，其中該濕式清潔模組，安裝在該移動平臺上，包括： 清潔頭，被配置爲清潔該操作面； 驅動單元，同該清潔頭連接，驅動該清潔頭沿著目標面做往復運動。

3.如請求項1的自動清潔設備，其中該清潔頭爲板狀結構，包括作業頭，該作業頭爲刷子、抹布、海綿中的任何一種或多種。

4.如請求項1的自動清潔設備，其中該移動平臺包括升降臺，該升降臺同該移動平臺連接，被配置爲相對於移動平臺上下移動； 該濕式清潔模組和該回收模組，安裝在該升降臺上

5.如請求項1的自動清潔設備，其中該升降臺包括： 升降機構，同該移動平臺連接，被配置爲驅動該升降臺相對於該移動平臺上下移動； 升降臺基座，同該升降機構連接，被配置爲在升降機構的作用下相對於該移動平臺上下移動，該升降臺基座包括： 第一連接端，靠近該移動平臺的前方；和 第二連接端，靠近該移動平臺的後方。

6.如請求項5的自動清潔設備，其中該升降臺基座還包括輔助輪，其中，當該升降臺基座相對於該移動平臺向下移動時，該輔助輪首先接觸到該操作面。

7.如請求項6的自動清潔設備，其中該升降機構爲柔性牽引機構，通過第一線纜將該升降臺基座懸掛在該移動平臺上，並配置爲牽動該升降臺基座相對於該移動平臺上下移動。

8.如請求項7的自動清潔設備，其中該升降臺還包括連接杆，該連接杆包括： 第一鉸接端，同該升降臺基座的該第一連接端鉸接；和 第二鉸接端，同該移動平臺鉸接。

9.如請求項8的自動清潔設備，其中該柔性牽引機構包括： 懸掛機構，包括該第一線纜，將該升降臺基座懸掛在該移動平臺上，和 驅動機構，驅動該升降臺基座相對於該移動平臺做上下移動。

10.如請求項9的自動清潔設備，其中該懸掛機構包括： 至少一個線纜導軌，安裝在該升降臺基座上，以便該第一線纜通過，其中，該第一線纜穿過該至少一個線纜導軌時延伸方向發生轉折。

11.如請求項9的自動清潔設備，其中該移動平臺包括： 給水模組，被配置爲向該操作面提供清潔液，該給水模組位於該濕式清潔模組之前，以使該濕式清潔模組使用該清潔液清潔該操作面。

12.如請求項11的自動清潔設備，其中該回收模組在該給水模組的後方。

13.如請求項11的自動清潔設備，其中該給水模組包括儲存裝置，安裝在該移動平臺上來儲存該清潔液，該儲存裝置設有開口，該清潔液經該開口至該操作面。

14.如請求項13的自動清潔設備，其中該給水模組還包括分配器，同該儲存裝置的該開口連接，其中，該清潔液經該儲存裝置的該開口流向該分配器，並通過該分配器均勻地塗在該操作面上。

15.如請求項14的自動清潔設備，其中該給水模組還包括給水驅動裝置，安裝在該儲存裝置的該開口處，同該分配器連接，被配置爲從該儲存裝置中抽取該清潔液至該分配器。

16.如請求項1的自動清潔設備，其中該回收模組包括輥子，同該移動平臺樞軸連接，相對於該移動平臺做旋轉運動，當該回收模組工作時，該輥子貼在該操作面上， 其中，該輥子包括彈性吸水材料來吸收該操作面上的該清潔液。

17.如請求項16的自動清潔設備，該回收模組還包括輥子驅動裝置，同該輥子連接，驅動該輥子做旋轉運動。

18.如請求項17的自動清潔設備，其中該回收模組還包括回收組件，同該移動平臺連接，被配置爲回收該輥子吸收的該清潔液，該回收組件包括： 刮板，該刮板壓緊該輥子，將該輥子吸收的該清潔液擠壓出來， 其中，當該輥子旋轉時，該輥子經過該刮板的方向爲從上向下經過。

19.如請求項18的自動清潔設備，其中該輥子驅動裝置驅動該輥子逆著該目標方向移動，使得該輥子同該操作面接觸部分的線速度指向該移動平臺的前方， 其中，該刮板位於該輥子的後方。

20.如請求項18的自動清潔設備，其中該回收組件還包括： 回收槽，同該刮板連接，並被配置爲回收該刮板從該輥子上擠壓出的該清潔液。

21.如請求項20的自動清潔設備，其中該回收組件還包括回收倉， 其中，該回收槽包括回收口，該回收倉通過該回收口同該回收槽連接。

22.如請求項21的自動清潔設備，其中該回收組件還包括回收葉片，在該回收槽裏並同該移動平臺樞軸連接，該回收葉片通過旋轉運動將該回收槽中的該清潔液運送至該回收口。

23.如請求項22的自動清潔設備，其中該回收組件還包括回收驅動裝置，被配置爲抽取該回收口處的該清潔液至該回收倉。

24.如請求項22的自動清潔設備，其中該回收組件還包括葉片驅動裝置，同該回收葉片連接，被配置爲驅動該回收葉片旋轉。

25.如請求項22的自動清潔設備，其中該回收葉片包括蝸杆葉片刷。

26.如請求項22的自動清潔設備，其中該回收組件還包括濾網，位於該回收口，被配置爲過濾該清潔液中的雜質。


'''


from collections import defaultdict
from typing import NamedTuple
import re
import copy

# ============= 處理元件 ==================================================

copiedclaims = copy.copy(claims)

def elemtokener(s):
  edic = defaultdict(str)  
  rdic = defaultdict(str)
  idxnum = defaultdict(str)
  idxelem = defaultdict(str)
  # numelem = defaultdict(str)

  class Token(NamedTuple):
      numb: str
      spacerMid: str
      elem: str
      spacerEnd: str

  token_specification = [
      ('numb',     r'[a-zA-Z_0-9]+'),    # Integer or decimal number
      ('spacerMid',  r'[- —、，:：]*'),     # 元件與符號的間隔記號
      ('elem',     r'.*?'),         # 元件
      ('spacerEnd',  r'[、；，。\n]'),     # 每一對元件與符號配對之間的間隔記號
  ]
  tok_regex = ''.join('(?P<%s>%s)' % pair for pair in token_specification)
  #print(tok_regex)

  idx = 0
  idxmin = 5000
  alist_token = []
  for mo in re.finditer(tok_regex, s):
    atok = Token(mo.group('numb').strip(),
                 mo.group('spacerMid').strip(),
                 mo.group('elem').strip(),
                 mo.group('spacerEnd').strip())
    num = atok.numb
    name = atok.elem
    elem = name
    rdic[elem] = num
    edic[num] = elem
    alist_token.append(atok)
    #a_groupdict = mo.groupdict()
    #print(atok, value)
    idx_str = '【%s】' % str(idx+idxmin)
    idxnum[idx_str] = num
    idxnum[num] = idx_str
    idxelem [idx_str] = elem
    idxelem [elem] = idx_str
    # numelem [num] = name
    # numelem [name] = num
    
    idx += 1
  return alist_token, edic, rdic, idxnum, idxelem #, numelem



# ============= 處理請求項 ==================================================
alsit_token, edict, rdictc, idxnum, idxelem = elemtokener(s)
# print(alsit_token, "\n", edict, "\n", rdictc, "\n",
#                         idxnum, "\n",idxelem, "\n", numelem)

alist_token = edict.values()

sdorded_token = ( tok for tok in 
                   sorted(alist_token, key=lambda tok: len(tok), reverse=True))
# print(alist_token)
#將元件名稱，更換成idx

for elem in sdorded_token:
  copiedclaims = copiedclaims.replace(elem, idxelem [elem])
# print("============ 初始替換 ============", )
# print(copiedclaims)

# ============= 處理請求項 ==================================================


def claimtokener_idx(elem, claims):
  class Token(NamedTuple):
      pos: int
      pream: str
      pream1st: str
      elem: str
      clmtyp: str
      clmnum: int
  #元件符號的 regex
  temp_token_spec = [
      ('pream',  r'.{,4}'),     # 保留，以後用來處理「閘極電極部」和「電極部」所出現的錯誤。
      ('elem',  elem),         # 元件
  ]
  temp_tok_regex = ''.join('(?P<%s>%s)' % pair for pair in temp_token_spec)
  #print(tok_regex)
  
  # Token 的 regex
  token_specification = [
      ('clmflag',   r'【請求項\d+】'),     # 請求項的編號
      ('indpen',  r'一種'),                #獨立項   r'\d+.{,3}一種'
      ('depen',   r'如請求項\d'),        # 附屬項
      ('element',  temp_tok_regex),         # 元件
  ]
  tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
  #print(tok_regex)


  alist_token = []
  clmtyp = 'indpen'
  clmnum = 0
  pos = 0
  for mo in re.finditer(tok_regex, claims):
    kind = mo.lastgroup
    #value = mo.group()
    #print(kind, value)
    match kind:
        case 'clmflag':        #找出請求項的編號
            pass #clmnum += 1  
        case 'indpen':
            clmtyp = '獨立項'  #找出「一種」，判斷為獨立項
            pos = 0            #獨立項時，先讓位置設為0，重新計數。
            clmnum += 1 
        case 'depen':
            clmtyp = '附屬項'   #找出「根據請求項」，判斷為附屬項
            clmnum += 1 
        case 'element':
            try:
                preamble =  mo.group('pream')
                preamble_1st = preamble[-1]
            except:
                preamble_1st = "  "
                
            atok = Token(pos, 
                         mo.group('pream'), 
                         preamble_1st, 
                         mo.group('elem'),
                         clmtyp,
                         clmnum)
            pos += 1
            alist_token.append(atok)
            #print(atok)
            #print(atok.pream1st+atok.elem, atok.pos, atok.clmtyp, atok.clmnum)
            if atok.pos != 0 and atok.pream1st not in "該的些述":
                print(atok.pream1st+idxelem[atok.elem], 
                      "位置="+str(atok.pos), 
                      atok.clmtyp, 
                      "【請求項"+str(atok.clmnum)+"】")
            if atok.pos == 0 and atok.pream1st in "該些述":
                print(atok.pream1st+idxelem[atok.elem], 
                      "位置="+str(atok.pos), 
                      atok.clmtyp, 
                      "【請求項"+str(atok.clmnum)+"】")            
  #print(alist_token)
  return

def claimtokener(elem, claims):
  class Token(NamedTuple):
      pos: int
      pream: str
      pream1st: str
      elem: str
      clmtyp: str
      clmnum: int
  #元件符號的 regex
  temp_token_spec = [
      ('pream',  r'.{,4}'),     # 保留，以後用來處理「閘極電極部」和「電極部」所出現的錯誤。
      ('elem',  elem),         # 元件
  ]
  temp_tok_regex = ''.join('(?P<%s>%s)' % pair for pair in temp_token_spec)
  #print(tok_regex)
  
  # Token 的 regex
  token_specification = [
      ('clmflag',   r'【請求項\d+】'),     # 請求項的編號
      ('indpen',  r'一種'),                #獨立項   r'\d+.{,3}一種'
      ('depen',   r'如請求項\d'),        # 附屬項
      ('element',  temp_tok_regex),         # 元件
  ]
  tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
  #print(tok_regex)


  alist_token = []
  clmtyp = 'indpen'
  clmnum = 0
  pos = 0
  for mo in re.finditer(tok_regex, claims):
    kind = mo.lastgroup
    #value = mo.group()
    #print(kind, value)
    match kind:
        case 'clmflag':        #找出請求項的編號
            pass #clmnum += 1  
        case 'indpen':
            clmtyp = '獨立項'  #找出「一種」，判斷為獨立項
            pos = 0            #獨立項時，先讓位置設為0，重新計數。
            clmnum += 1 
        case 'depen':
            clmtyp = '附屬項'   #找出「根據請求項」，判斷為附屬項
            clmnum += 1 
        case 'element':
            try:
                preamble_1st =  mo.group('pream')[-1]
            except:
                preamble_1st = "  "
                
            atok = Token(pos, 
                         mo.group('pream'), 
                         preamble_1st, 
                         mo.group('elem'),
                         clmtyp,
                         clmnum)
            pos += 1
            alist_token.append(atok)
            #print(atok)
            #print(atok.pream1st+atok.elem, atok.pos, atok.clmtyp, atok.clmnum)
            if atok.pos != 0 and atok.pream1st not in "該的些述":
                print(atok.pream1st+atok.elem, atok.pos, atok.clmtyp, atok.clmnum)
  #print(alist_token)
  return



# elem = '電化學測試片'
# claimtokener(elem, claims)

# 方法一
# for k, v in edict.items():
#     claimtokener(v, claims)
  
# 方法二
for k, v in edict.items():    
    elem = v
    claimtokener_idx(idxelem [elem], copiedclaims)
    
  
   
  