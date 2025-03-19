from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram import Bot, Dispatcher, types


from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import app.keyboards as kb

from aiogram.types import BufferedInputFile
from config import GROUP_ID,KAT2_GROUP_ID,KAT3_GROUP_ID,TOKEN
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




from datetime import datetime

import logging



from aiogram import Bot, Dispatcher, types

import config
logging.basicConfig(level=logging.INFO)



senders = {
'qstkennethadams388@gmail.com':'itpz jkrh mtwp escx',
'usppaullewis171@gmail.com':'lpiy xqwi apmc xzmv',
'ftkgeorgeanderson367@gmail.com':'okut ecjk hstl nucy',
'nieedwardbrown533@gmail.com':'wvig utku ovjk appd',
'h56400139@gmail.com':'byrl egno xguy ksvf',
'den.kotelnikov220@gmail.com':'xprw tftm lldy ranp',
'trevorzxasuniga214@gmail.com':'egnr eucw jvxg jatq',
'dellapreston50@gmail.com':'qoit huon rzsd eewo',
'neilfdhioley765@gmail.com':'rgco uwiy qrdc gvqh',
'hhzcharlesbaker201@gmail.com':'mcxq vzgm quxy smhh',
'samuelmnjassey32@gmail.com':'lgct cjiw nufr zxjg',
'allisonikse1922@gmail.com':'tozo xrzu qndn mwuq',
'corysnja1996@gmail.com':'pfjk ocbf augx cgiy',
'maddietrdk1999@gmail.com':'rhqb ssiz csar cvot',
'yaitskaya.alya@mail.ru':'CeiYHA6GNpvuCz584eCp',
'yelena.polikarpova.1987@mail.ru':'70Ktuvrs1iYbvSnbK8hG',
'yeva.zuyeva.85@mail.ru':'EBjgRqq73hue9dGhUA2R',
'zina.yagovenko.69@mail.ru':'QKBmpXnzFZVu9w4ewSrA',
'ilya.yaroslavov.72@mail.ru':'A2gNkb8n54i4T7XdPdH5',
'maryamna.moskvina.62@mail.ru':'dT7ftdX72cMsVemqRRqu',
'zina.zhvikova@mail.ru':'7CwRkjeL3a5viE9we3bt',
'boyarinova.fisa@mail.ru':'NnJfmSBzQ9Eew09xirpY',
'prokhor.sveshnikov.73@mail.ru':'Ybunrxdf95gkzm6A6ipp',
'azhikelyamov.yulian@mail.ru':'r7hanfr0tMqcBE4Edmg0',
'prokhor.siyantsev@mail.ru':'yubs6kvtfpWT4Tram26e',
'yablonev90@mail.ru':'42krThdaYbWCrCbH8UgK',
'mari.dvornikova.86@mail.ru':'qdEzYLWSTz6UEM2E4i0u',
'vika.tobolenko.96@mail.ru':'3WQ2wFTwge9m2C09QsfK',
'koporikov.yura@mail.ru':'nJtyfjqYi91j7tk0udNx',
'zina.podshivalova.92@mail.ru':'u4CL3YxVutmiuTvmTrbu',
'leha.novitskiy.71@mail.ru':'qQZd1gMqkU906Xk2hgJJ',
'rimma.aleksandrovicha.72@mail.ru':'biL4m6h0h4xQrDB3PnPp',
'polina.karaseva.1987@mail.ru':'mxZUqPPTrZHK99jUfPhB',
'prokhor.sablin.82@mail.ru':'vN7FjmmCmAD0JnQsANyc',
'kade.kostya@mail.ru':'U0hdXu7y3c1AVeT1Vpn9',
'yelizaveta.novokshonova.71@mail.ru':'aKPpgaPDuwaKbX1pbcq3',
'pozdovp@mail.ru':'EGDd20c7s82Z0s9LmrXc',
'siyasinovy@mail.ru':'z2ZdsRL04JvBYZrrjrvv',
'nina.gref.73@mail.ru':'sitw1XTxCVgji061iqj7',
'fil.golubkin.80@mail.ru':'PeaLrzjbn408DEeiqmQq',
'venedikt.babinov.71@mail.ru':'tBewA1HQm29c2Zkira96',
'den.verderevskiy.67@mail.ru':'fndp7qr67dpfXBAu0ePH',
'olga.viranovskaya.92@mail.ru':'50QSPrecgk5cMdk1YsBm',
'uyankilovich@mail.ru':'Muw9kX9vAhhKxbZXZ3sh',
'clqdxtqbfj@rambler.ru':'8278384a3L51C',
'qeuvkzwxao@rambler.ru':'72325556pMFol',
'mgiwwgbjqt@rambler.ru':'3180204jCoAdt',
'olwogjcicw@rambler.ru':'3993480P4Gyth',
'qjdmjszsnc@rambler.ru':'6545403StkbOh',
'yqoibpcoki@rambler.ru':'695328653f9Wp',
'vnlhjjkbxr@rambler.ru':'4609313egqV59',
'vpgcdkunar@rambler.ru':'9936120R4LYh3',
'agycsnogqq@rambler.ru':'0234025nWwX5j',
'ctmhzsngse@rambler.ru':'2480571s1sZvW',
'ryztzlttdn@rambler.ru':'9416368kTX5jI',
'hqxybovebw@rambler.ru':'8245145VhX704',
'rejrjswkwb@rambler.ru':'5114881xCYqsB',
'xkbecjvxnx@rambler.ru':'5670524FiFi39',
'xnlqkfvwzx@rambler.ru':'7911186rp8L9P',
'gvzzmqtuzy@rambler.ru':'5133370ZstXEx',
'eijxsbjyfy@rambler.ru':'36196124YQZeI',
'bizdlfuahq@rambler.ru':'8374903tkk2gA',
'dhehumtsef@rambler.ru':'9126453AkhK0Z',
'zsotxpaxvi@rambler.ru':'46227528QryxI',
'ktsgdygeuc@rambler.ru':'1853586bnCyzK',
'uiacgqvgpe@rambler.ru':'65280104FvoJW',
'ynazuhytyd@rambler.ru':'1038469bD3PXc',
'ewmyymarvi@rambler.ru':'5023318Bh3tBg',
'wllhpdisuj@rambler.ru':'24856958LdTsS',
'ldqicaqxqo@rambler.ru':'3878601ZNDUtq',
'qnuumqoreq@rambler.ru':'97575207Is6tx',
'hlqhvdwpvn@rambler.ru':'6886684bPjiyd',
'mjjjxiuadq@rambler.ru':'0606032V81m1F',
'qmasujqfrk@rambler.ru':'277585511anUy',
'mfemvxqdcq@rambler.ru':'8831015UwqwWD',
'jauvxszfam@rambler.ru':'0711044gqzrVR',
'lkmujuagfk@rambler.ru':'08781007DLS8k',
'kcamwmzxjo@rambler.ru':'9812873rVr1MY',
'czkklwifon@rambler.ru':'74278883h9FP8',
'tsjsbqyrfk@rambler.ru':'0150917jIseH2',
'pbetvcnhzh@rambler.ru':'9952234XaKDFu',
'bsahxcpwkw@rambler.ru':'2860163ch8Ido',
'xphyesgbtc@rambler.ru':'6594341ERehhX',
'egmpjoufeq@rambler.ru':'2613441hfDuWr',
'jyaolatwam@rambler.ru':'7668835xdjLbg',
'istooplcmf@rambler.ru':'6592403JR47Wm',
'vxesoednot@rambler.ru':'35885918QZw94',
'oywtklayaz@rambler.ru':'4434448KsCuTf',
'tazxrlpjil@rambler.ru':'8342862p9Wyst',
'aumiycpxid@rambler.ru':'4109383BuuNcN',
'lrrztbfuzy@rambler.ru':'3646406sDO8ay',
'ocggavguxr@rambler.ru':'6406050SL2mZG',
'imprdsrnmd@rambler.ru':'4869746vpxksJ',
'eidyoikavp@rambler.ru':'1243890yXPyix',
'jtbcabsapw@rambler.ru':'566339497yHv3',
'szokdvnzrw@rambler.ru':'5285567I3Bil1',
'jqflrccfjs@rambler.ru':'7239478VeLuf1',
'nhmxjawemh@rambler.ru':'22695409fkCex',
'uoolwvvwdc@rambler.ru':'1073090zX6ebM',
'bdnptczren@rambler.ru':'2684430DcPEuk',
'bfghzdkurg@rambler.ru':'3874335d5hDQy',
'ljlexsfcvo@rambler.ru':'4102671EIquGo',
'byzjhysyyg@rambler.ru':'4637736mzdEcT',
'tlrjbuzcyj@rambler.ru':'2437827AhPaGW',
'denjsbmggh@rambler.ru':'228014585ayVe',
'ekkjrcskzo@rambler.ru':'6609442MFPeDO',
'ptpjocqobw@rambler.ru':'6047270EXk7Hb',
'nekrxmcklm@rambler.ru':'3532718I3vV4C',
'ulgqeqvdqy@rambler.ru':'6764301Nx25yL',
'ezofozvhyn@rambler.ru':'43181265tC6FQ',
'hwklsnkqky@rambler.ru':'2399374mHyEUJ',
'elglaqexoj@rambler.ru':'9803014pMNF9p',
'rgmjfwhhjs@rambler.ru':'3268611cfC3aR',
'vcvwvkntgb@rambler.ru':'6536007UgTXg4',
'phkohtlitv@rambler.ru':'0238010TXt5aN',
'pqqqyejlqi@rambler.ru':'0429804UwSSi2',
'toxevermnd@rambler.ru':'1801000MqDm87',
'dicfdqgxad@rambler.ru':'2062460Tbvjlz',
'sktsnxhcxe@rambler.ru':'35185285Pon91',
'jpljjnrrla@rambler.ru':'0815671xPHjiw',
'rtqpiimiid@rambler.ru':'6534672URa1mI',
'ldygdlpizk@rambler.ru':'6686886YWhL05',
'fqxqadaxfy@rambler.ru':'3195621x5qYdU',
'chybzpsglw@rambler.ru':'8032931YTKllg',
'vkctzanare@rambler.ru':'1157997LGySqk',
'repjncygun@rambler.ru':'3300691BqYJVG',
'khrarivdow@rambler.ru':'7168350Cmqkmj',
'aqbeitoqdl@rambler.ru':'87552792499tS',
'vhauhgmbnc@rambler.ru':'9276444y9YzY1',
'cfoqabqkbi@rambler.ru':'4601718gc2Zji',
'kmqnowhvjp@rambler.ru':'6667003L1jZxc',
'djsdksvzhj@rambler.ru':'7523251yAKPjZ',
'uztbbbfqbp@rambler.ru':'8265517naN9fx',
'ljrbpfuicp@rambler.ru':'39793362TjZIk',
'jzzdyxicjo@rambler.ru':'8117494s6CZVB',
'gjnbtrflkc@rambler.ru':'8623171iqXOD9',
'jfjtwncyeb@rambler.ru':'7066987lMSG2Z',
'rfphqkyyrj@rambler.ru':'8800207M5Nj7Y',
'ilynipkqwx@rambler.ru':'83333032WQo83',
'ifzenleixs@rambler.ru':'69679436xM9U4',
'oevwtysoel@rambler.ru':'6918228UC47Zs',
'hpdkdwqvzx@rambler.ru':'0605431xMVexd',
'ekbkufxdxx@rambler.ru':'1918712uEOQ9t',
'zstxwfwiof@rambler.ru':'4043772UwRp5o',
'rjmrbybhnd@rambler.ru':'5203792lDmxvC',
'eukygnfzno@rambler.ru':'3520959hXs1Zw',
'ljrolbwlad@rambler.ru':'0394475pK0dYa',
'gozpezocmj@rambler.ru':'8282635Gkvuvq',
'asytoiumwt@rambler.ru':'42141199FgP3H',
'fbiooohghv@rambler.ru':'7338453zMbWhb',
'ajwlalfqqu@rambler.ru':'3360915x1XVgt',
'cvegntetwm@rambler.ru':'8091607CSuKMf',
'jnhjnmicbt@rambler.ru':'6375986dokrgG',
'fnaauasmjz@rambler.ru':'4160248ztCRsJ',
'qnwmlvfwct@rambler.ru':'8367630XGXmxW',
'lkycbhjcwp@rambler.ru':'5255980KedZTc',
'bkyojwrkxl@rambler.ru':'1286663uHl4WQ',
'lxddybklck@rambler.ru':'1077242JFSyQN',
'chzhdkoxnp@rambler.ru':'0533445SI0q7c',
'ofjxkwwomf@rambler.ru':'04956317DKrSX',
'jlirgtapbl@rambler.ru':'8728917NdMxgN',
'dgcceghlse@rambler.ru':'2986381aT5V36',
'rkwfhcvlem@rambler.ru':'10022063K5qmY',
'orgjvhbrxw@rambler.ru':'0652659TopL8Z',
'opynskpmzp@rambler.ru':'2881423L4qs6x',
'pbqzrueeko@rambler.ru':'44469262tOGeK',
'raxzhngqti@rambler.ru':'3078265mgWYjl',
'ztnxozwuuj@rambler.ru':'0637919utKekj',
'gtxjzwlgio@rambler.ru':'3737088WWddrY',
'sjbflcwjgn@rambler.ru':'9791667kVGllD',
'znggdpfxzu@rambler.ru':'0209083jdisUI',
'gnvhlocnro@rambler.ru':'4361239Vu3OCl',
'vqeijhgrmo@rambler.ru':'5560137M1oKk2',
'meefvzfwqb@rambler.ru':'9793015vJE0qF',
'sclsjzvugn@rambler.ru':'4631432OQjvWt',
'ybbtiosefy@rambler.ru':'3511505pL04S1',
'agwqdadpkb@rambler.ru':'0930298CUZdLp',
'kudgvibwao@rambler.ru':'5791834nlLQtU',
'qyonxjqbxi@rambler.ru':'9390829m2Edz3',
'jhetdlhlqk@rambler.ru':'5530162MiLHZe',
'bsjvczarsc@rambler.ru':'5747155KvNjcL',
'wlcilpvzqu@rambler.ru':'2757580jLlM9M',
'xxdgcixidw@rambler.ru':'2867562O7zGft',
'wekduwrnkp@rambler.ru':'2646367TlIskI',
'keakcnrorg@rambler.ru':'9223165cV1Jj8',
'nzuspyevwr@rambler.ru':'2212416npkUqe',
'mgjfbgitts@rambler.ru':'7368986roeLXD',
'smfxvrnhmu@rambler.ru':'6947298Kau5qA',
'yvkelubdzf@rambler.ru':'5913332lXWtlC',
'bwywtjxybd@rambler.ru':'2766021wTSkeU',
'dlvyzavolw@rambler.ru':'274983252lHyu',
'oaudcugulf@rambler.ru':'4543030UHFWaV',
'zvqexaokhf@rambler.ru':'1453114PCheCq',
'pjuafpzpoo@rambler.ru':'8474216vNFUG0',
'ckryhpqogh@rambler.ru':'4791674aJHW43',
'vlkqstbhpd@rambler.ru':'3021260kBI3KU',
'jwuupemjpm@rambler.ru':'7769235y719L9',
'bmxuqrzcnk@rambler.ru':'1345552ExHXyu',
'fqrkonqkjc@rambler.ru':'4104158bVEORa',
'gizwbhyrfd@rambler.ru':'3863359lgfpTv',
'onghqwbvnz@rambler.ru':'8249537XWqpPk',
'aeyeyvlnkl@rambler.ru':'6025219f5mGom',
'qcwweqcqbx@rambler.ru':'2503306kHzKPD',
'vefmynztzu@rambler.ru':'1134939bhRpJS',
'qlkhitdctp@rambler.ru':'31621358ZPx5F',
'xhgfgecvrn@rambler.ru':'4116759TRhERi',
'globizrzui@rambler.ru':'9679753mLkmMd',
'vvfcuoibrf@rambler.ru':'13558992CDkJj',
'enccmwktap@rambler.ru':'7631476Lzr9hd',
'njbnyghvdq@rambler.ru':'48585907Qh2NS',
'cobadewaxd@rambler.ru':'6433228NMX7a0',
'zzvsuoiqfx@rambler.ru':'5067380KtnMTb',
'lkdcjpcqxu@rambler.ru':'8319085aRHdoT',
'zcabeofgox@rambler.ru':'0059181TJSaJq',
'rswrifhmtf@rambler.ru':'2987108xzf1Uy',
'gebzgyscic@rambler.ru':'6981082UOD1sL',
'yhncgfwjom@rambler.ru':'7866073mRMAal',
'pvvlmjmiwe@rambler.ru':'2807349CLUZie',
'towqdsigmc@rambler.ru':'48481486UnoRg',
'eyzwvxphxz@rambler.ru':'5532563Bskght',
'aruhbkpsud@rambler.ru':'8022722dNUe59',
'kckwnnvmwf@rambler.ru':'77502899D6ygI',
'emicquwuxf@rambler.ru':'2982514obBgCJ',
'pnefqbonja@rambler.ru':'1443294ZY7BgB',
'wlnecrzvkb@rambler.ru':'2016456ke4QRw',
'lucufydobd@rambler.ru':'4188202gvlmuR',
'obcheovoqy@rambler.ru':'34012721sYlv3',
'fjxwhhlhxp@rambler.ru':'1621680a9CbS0',
'rjggfmhckx@rambler.ru':'4470958ocoPjD',
'oqixhlbhlh@rambler.ru':'4902150aD8Tkr',
'zmlfdygkce@rambler.ru':'4809956HgOdyu',
'zdjqfhdafp@rambler.ru':'9142498RW8Ynh',
'cjoyoxsdby@rambler.ru':'108516737An82',
'hfrcbbwzgb@rambler.ru':'1732107RUVvSu',
'crkbywjfzg@rambler.ru':'9616254qbUhAG',
'luygpfibra@rambler.ru':'9488606qXIvQZ',
'xepjtcrrzo@rambler.ru':'3774977dMOr4c',
'ayrbethwst@rambler.ru':'4658060glYVyA',
'czhjnqqgdd@rambler.ru':'89865789wXqfK',
'oltotetppj@rambler.ru':'0936665mJL9H0',
'eaoeqvygrv@rambler.ru':'5348316HcEpsm',
'dkfvwvkotb@rambler.ru':'3366454MTGiOR',
'wavsfqiarg@rambler.ru':'4220587wVJ8gU',
'gkwlbrhwix@rambler.ru':'6383580cCHutT',
'uachryyzde@rambler.ru':'0643369cWRWhr',
'nuyfldwirg@rambler.ru':'29709163eKxWc',
'fnorovxtvk@rambler.ru':'469173140zLer',
'qrmnfyxdqj@rambler.ru':'7609701E9XfBC',
'ncupywgysj@rambler.ru':'8506439mTgrb6',
'ehhuextqqm@rambler.ru':'4136418EqGa4N',
'utasiosnxd@rambler.ru':'6230428wOiMLm',
'ppizzpzqod@rambler.ru':'6217530deEIGb',
'mgzczmjjpo@rambler.ru':'5974114gf7VLz',
'ezugyxxfkx@rambler.ru':'6920685aZVulS',
'vnuwwwuhuj@rambler.ru':'20889562nRk1x',
'xqkicchcbc@rambler.ru':'4345126XoitUD',
'hykbjrvqsw@rambler.ru':'8281493mLUbNt',
'etyqikxlam@rambler.ru':'1096360Cvg5n7',
'blnpfilkdh@rambler.ru':'6208964Fhgy1O',
'azawxjcfeh@rambler.ru':'8923382Pqo1jI',
'dyumumpgus@rambler.ru':'3454195S5FQ7d',
'ryejfejmef@rambler.ru':'1474062Y49oZE',
'uqyfeqyumv@rambler.ru':'4305431o270vK',
'vardlzqzas@rambler.ru':'8158325VAjymq',
'wvqbwbpofd@rambler.ru':'2037592lvIWZI',
'agsnpvxscg@rambler.ru':'676450330Gmzj',
'ctiwtwpowk@rambler.ru':'7004605qQOK5O',
'vvluscokds@rambler.ru':'2351339uVtaUb',
'gqtipysiyk@rambler.ru':'4672575GMSkQq',
'vwtjzupcul@rambler.ru':'6978060SRfKxQ',
'klvdgsoczb@rambler.ru':'8504791kNehzf',
'lavpussyin@rambler.ru':'1183746FmKlfU',
'xvzoptqyhd@rambler.ru':'7635851M7gCQO',
'yzkgydxjlr@rambler.ru':'3889248nBv9xb',
'tkuscgummb@rambler.ru':'2646861vfBmjy',
'ytbfnnlvuc@rambler.ru':'8680715wXqNoY',
'qrmyueqrpk@rambler.ru':'48163158cQzn3',
'nulburzrsp@rambler.ru':'4628721fbFYDx',
'xpsncakaar@rambler.ru':'8050121QgZtLE',
'rsfyuinlhi@rambler.ru':'7789677doEl7X',
'lruwhkjpmm@rambler.ru':'2407934PCrhbt',
'zqlboekoph@rambler.ru':'4540547BXedBD',
'djrmgdvpxk@rambler.ru':'2516345lt4GhI',
'cdyagajvqt@rambler.ru':'0457036J8b9x1',
'csbmtfyogo@rambler.ru':'8578398RoY5Me',
'mtgjgvchbf@rambler.ru':'6273263XOh0fb',
'hjovrkraea@rambler.ru':'1756354e4T9PL',
'wuasdmqayg@rambler.ru':'8983467Njjbfc',
'dnzaquycrh@rambler.ru':'3047369gLtNHO',
'rdptnhimnz@rambler.ru':'92217639LcTX1',
'yklofyaekj@rambler.ru':'0018913JhfLfv',
'zqfzplzlwp@rambler.ru':'6550676M1gwNy',
'fzcveyejbh@rambler.ru':'9098104PB57ol',
'qcpwhpqape@rambler.ru':'3277585gafS4o',
'xfitvnzvez@rambler.ru':'0023433CgWWiW',
'tiansbolvj@rambler.ru':'0200419d6c8hD',
'ibwukvjyxn@rambler.ru':'6846348Go4rB7',
'tfclkifgjn@rambler.ru':'9973469KBqk2S',
'yscehsgepj@rambler.ru':'0258935Wptd0G',
'webznumpmf@rambler.ru':'4342482ZhTyVk',
'xadehtuxys@rambler.ru':'94129234ZK2kl',
'wsfmuqnmjp@rambler.ru':'7886187uCcru0',
'mhovkuzfnl@rambler.ru':'3632660bLpvSw',
'pppuvtsuxu@rambler.ru':'6227635FqgnGa',
'vvezjeryic@rambler.ru':'7595367ZgjYIn',
'oiukjktkhx@rambler.ru':'35863397YZBFb',
'qswbndmblj@rambler.ru':'3563325a93EZ6',
'ztyfnsdrqa@rambler.ru':'7748929ZbfDrw',
'lrjduagkcj@rambler.ru':'8783147DV4pJe',
'fhrzanukuh@rambler.ru':'169703230lEf6',
'pqnnzwuuku@rambler.ru':'6446752B0qw8H',
'ndctkqjnfc@rambler.ru':'1534939xHfafC',
'tlzuekovcn@rambler.ru':'9668644RKjMla',
'ermdcrjyhu@rambler.ru':'9838788xXiLRC',
'qbfymlhpwj@rambler.ru':'3278597BlWafL',
'uuuzmgapoy@rambler.ru':'2535811Vz3dxV',
'chjolhsihy@rambler.ru':'8253848P8B5cd',
'rrakdmtsdb@rambler.ru':'0459246V4tjHK',
'ngkrbvqvha@rambler.ru':'9835759JQxkal',
'caxeoztjpa@rambler.ru':'1297098SSweKM',
'molnxkchzu@rambler.ru':'3122920NIh3iE',
'murnslgulf@rambler.ru':'1045964Oppb9c',
'qcjyautxca@rambler.ru':'6358075LUbp6R',
'amhlnrxaue@rambler.ru':'3401580IiYPYn',
'wexnexkcct@rambler.ru':'2157766eLIiqP',
'oplwkvkrct@rambler.ru':'7136350vkGkaT',
'pmddwbvmwv@rambler.ru':'3066705M2aCUh',
'aqjcdxeuuh@rambler.ru':'2077271RlOJ0c',
'baiivnfrdy@rambler.ru':'1327519LJwKyi',
'apvskvwhsv@rambler.ru':'2995739T8pCNZ',
'xsejblkgit@rambler.ru':'6224118EhnkyG',
'rxihtsvdxg@rambler.ru':'3045787jhQxfI',
'dgtmxgrdsm@rambler.ru':'0342058YAff0O',
'wuxaurjkuu@rambler.ru':'6231160X8CsYl',
'erimfuxfdl@rambler.ru':'1956070yzlgSl',
'ncklilvfts@rambler.ru':'5077711XhCUzu',
'eerlpvniie@rambler.ru':'6769422kteVgK',
'mcrtyjkbdi@rambler.ru':'5281059WC9HfI',
'izjnzlavcu@rambler.ru':'4201974Gjdy1B',
'tkrywugfgq@rambler.ru':'1037112WpAZzl',
'hpxzczhgwe@rambler.ru':'4522788wYVDJk',
'rtfanictwt@rambler.ru':'9292445IxACdk',
'lhschktxka@rambler.ru':'0731083E0ItX4',
'zfqfwvmnms@rambler.ru':'82390631NIbOF',
'rzaviakxlb@rambler.ru':'2230383uFiVmA',
'rmmueooozx@rambler.ru':'1531525wyFFSm',
'weasmvistt@rambler.ru':'7079364RGZCBs',
'qikszesoqz@rambler.ru':'6739326h2Wy4j',
'gosgrmonmh@rambler.ru':'7425012zw2LXl',
'vuhlehwstc@rambler.ru':'6477750sVXsV3',
'wcbmulbsbk@rambler.ru':'9889803qVwaj6',
'aejerwwnft@rambler.ru':'4598847uygrUg',
'rtrkjygdey@rambler.ru':'4810312JrG4Ti',
'uywyrkhuue@rambler.ru':'6593801fMGH6b',
'flqyimskwk@rambler.ru':'7856809GVZfzT',
'mqjqttpyui@rambler.ru':'3633261lxxEPt',
'asagkqfygx@rambler.ru':'90629300zd5Xm',
'bupfcjoqrc@rambler.ru':'7806644uXzkZy',
'twicbfjgoz@rambler.ru':'0187832xjeOz1',
}
receivers = ['sms@telegram.org, dmca@telegram.org, abuse@telegram.org, sticker@telegram.org, support@telegram.org']

router = Router()



# Dictionary to store temporary messages
user_messages = {}


class AuthState(StatesGroup):
    waiting_for_phone = State()
    waiting_for_code = State()
    waiting_for_plus1_content = State()
    waiting_for_plus3_content = State()
    waiting_for_kat1_content = State()
    waiting_for_kat2_content = State()
    waiting_for_plus22_content = State()
    waiting_for_plus222_content = State()
    waiting_for_username = State()
    waiting_for_tg_id = State()
    waiting_for_chat_link = State()
    waiting_for_violation_link = State()
    waiting_for_age = State()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    if message.from_user.id == 5176998143 or message.from_user.id == 8013867574  or message.from_user.id ==  6288265914:
        await message.answer(f'Привет админ')
        await message.answer('Выбери один из пунктов:', reply_markup=kb.modex)
    else:
        await message.answer(f'Привет {message.from_user.first_name}')
        await message.answer('Выбери один из пунктов:', reply_markup=kb.vibor)

@router.callback_query(F.data.startswith('modex'))
async def handle_category_selection(callback: CallbackQuery, state: FSMContext):
    category = callback.data
    await callback.answer()
    await state.update_data(selected_category=category)
    
    if category == 'modex0':
        await callback.message.answer('Пробив ещё не работает, жду хоть какое-то БД')
    elif category == 'modex1':
        await state.set_state(AuthState.waiting_for_username)
        await callback.message.answer("Введите юзер который надо снести")
    elif category == 'modex3':
        await state.set_state(AuthState.waiting_for_username)
        await callback.message.answer("Не работает ещё")

@router.message(AuthState.waiting_for_username)
async def process_username(message: Message, state: FSMContext):
    username = message.text
    await state.update_data(username=username)
    
    await state.set_state(AuthState.waiting_for_tg_id)
    await message.answer("Введите тг айди")

@router.message(AuthState.waiting_for_tg_id)
async def process_tg_id(message: Message, state: FSMContext):
    tg_id = message.text
    await state.update_data(tg_id=tg_id)
    
    await state.set_state(AuthState.waiting_for_chat_link)
    await message.answer("Введите ссылку на чат")

@router.message(AuthState.waiting_for_chat_link)
async def process_chat_link(message: Message, state: FSMContext):
    chat_link = message.text
    await state.update_data(chat_link=chat_link)
    
    await state.set_state(AuthState.waiting_for_violation_link)
    await message.answer("Введите ссылку на нарушение")

@router.message(AuthState.waiting_for_violation_link)
async def process_violation_link(message: Message, state: FSMContext):
    violation_link = message.text
    await state.update_data(violation_link=violation_link)
    user_data = await state.get_data()
    await message.answer(f"Вы ввели:\nИмя пользователя: {user_data['username']}\nTG ID: {user_data['tg_id']}\nСсылка на чат: {user_data['chat_link']}\nСсылка на нарушение: {user_data['violation_link']}")
    await message.answer(f"остальное на выхах добавится")
    




        
    



def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        if 'gmail.com' in sender_email:
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
        elif 'rambler.ru' in sender_email:
            smtp_server = 'smtp.rambler.ru'
            smtp_port = 587
        elif 'hotmail.com' in sender_email:
            smtp_server = 'smtp.office365.com'
            smtp_port = 587
        elif 'mail.ru' in sender_email:
            smtp_server = 'smtp.mail.ru'
            smtp_port = 587
        else:
            raise ValueError("Unsupported email provider")
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        server.quit()
        
        return True
    except Exception as e:
        return False

@router.callback_query(F.data.startswith('kat'))
async def handle_category_selection(callback: CallbackQuery, state: FSMContext):
    category = callback.data
    await callback.answer()
    await state.update_data(selected_category=category)
    
    if category == 'kat0':
        await callback.message.answer('Выберите вариант:', reply_markup=kb.vopros1)
    elif category == 'kat1':

        await callback.message.answer('Отправьте текст с фото/текст с видео')
        await callback.message.answer("❗❗В сообщении может присутствовать максимум 1 видео или 1 фото❗❗")
        await state.set_state(AuthState.waiting_for_kat1_content)


    elif category == 'kat2':
        await callback.message.answer('Напишите ваш тэг и причину разбана:')
        await state.set_state(AuthState.waiting_for_kat2_content)


@router.message(AuthState.waiting_for_kat1_content, F.photo)
async def handle_kat1_photo(message: Message, state: FSMContext, bot: Bot):
    photo = message.photo[-1]
    caption = message.caption or ""
    photo_file = await bot.get_file(photo.file_id)
    photo_bytes = await bot.download_file(photo_file.file_path)
    
    # Store the photo in temporary storage
    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'message': message,
            'photo': photo,
            'caption': caption,
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored photo message before forwarding to group with key {key}")

    # Send to group
    await bot.send_photo(
        chat_id=KAT3_GROUP_ID,
        photo=BufferedInputFile(photo_bytes.read(), filename="photo.jpg"),
        caption=caption
    )
    
    await message.answer("Сообщение успешно отправлено!")
    await state.clear()
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"ID: {message.from_user.id}"
    )






    

@router.message(AuthState.waiting_for_kat1_content, F.video)
async def handle_kat1_video(message: Message, state: FSMContext, bot: Bot):
    video = message.video
    caption = message.caption or ""
    video_file = await bot.get_file(video.file_id)
    video_bytes = await bot.download_file(video_file.file_path)
    
    # Store the video in temporary storage
    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'message': message,
            'video': video,
            'caption': caption,
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored video message before forwarding to group with key {key}")

    # Send to group
    await bot.send_video(
        chat_id=KAT3_GROUP_ID,
        video=BufferedInputFile(video_bytes.read(), filename="video.mp4"),
        caption=caption
    )
    
    await message.answer("Сообщение успешно отправлено!")
    await state.clear()
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"ID: {message.from_user.id}"
    )


@router.message(AuthState.waiting_for_kat1_content, F.text)
async def handle_kat1_text(message: Message, state: FSMContext, bot: Bot):
    text = message.text
    
    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'message': message,
            'text': text,
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored text message before forwarding to group with key {key}")

    # Send to group
    await bot.send_message(
        chat_id=GROUP_ID,
        text=f"Текст сообщения:\n{text}"
    )
    
    await message.answer("Текст успешно отправлен!")
    await state.clear()
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"ID: {message.from_user.id}"
    )




@router.callback_query(F.data == 'plus1')
async def handle_plus1(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Отправьте фото/видео и текст одним сообщением")
    await callback.message.answer("❗❗ПОСТЫ БУДУТ ПРИНИМАТЬСЯ , ТОЛЬКО С КООРДИНАТАМИ/АДРЕСОМ , ОСТАЛЬНОЕ ОТКЛОНИТСЯ❗❗")
    await state.set_state(AuthState.waiting_for_plus1_content)


@router.message(AuthState.waiting_for_plus1_content, F.photo)
async def handle_plus1_photo(message: Message, state: FSMContext, bot: Bot):
    photo = message.photo[-1]
    caption = message.caption or ""
    photo_file = await bot.get_file(photo.file_id)
    photo_bytes = await bot.download_file(photo_file.file_path)
    
    # Store the photo in temporary storage
    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'message': message,
            'photo': photo,
            'caption': caption,
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored photo message before forwarding to group with key {key}")

    # Send to group
    await bot.send_photo(
        chat_id=GROUP_ID,
        photo=BufferedInputFile(photo_bytes.read(), filename="photo.jpg"),
        caption=caption
    )
    
    await message.answer("Сообщение успешно отправлено!")
    await state.clear()
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"ID: {message.from_user.id}"
    )

    await bot.send_message(
        chat_id=GROUP_ID,
        text="Добавить в незакрашенные граффити?",
        reply_markup=kb.vopros3
    )

@router.message(AuthState.waiting_for_plus1_content, F.video)
async def handle_plus1_video(message: Message, state: FSMContext, bot: Bot):
    video = message.video
    caption = message.caption or ""
    video_file = await bot.get_file(video.file_id)
    video_bytes = await bot.download_file(video_file.file_path)
    
    # Store the video in temporary storage
    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'message': message,
            'video': video,
            'caption': caption,
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored video message before forwarding to group with key {key}")

    # Send to group
    await bot.send_video(
        chat_id=GROUP_ID,
        video=BufferedInputFile(video_bytes.read(), filename="video.mp4"),
        caption=caption
    )
    
    await message.answer("Сообщение успешно отправлено!")
    await state.clear()
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"ID: {message.from_user.id}"
    )

    await bot.send_message(
        chat_id=GROUP_ID,
        text="Добавить в незакрашенные граффити?",
        reply_markup=kb.vopros3
    )

@router.message(AuthState.waiting_for_plus1_content, F.text)
async def handle_plus1_text(message: Message, state: FSMContext, bot: Bot):
    text = message.text
    
    # Store the text in temporary storage
    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'message': message,
            'text': text,
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored text message before forwarding to group with key {key}")

    # Send to group
    await bot.send_message(
        chat_id=GROUP_ID,
        text=f"Текст сообщения:\n{text}"
    )
    
    await message.answer("Текст успешно отправлен!")
    await state.clear()
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"ID: {message.from_user.id}"
    )

    await bot.send_message(
        chat_id=GROUP_ID,
        text="Добавить в незакрашенные граффити?",
        reply_markup=kb.vopros3
    )





@router.callback_query(F.data == 'plus3')
async def handle_plus3(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Отправьте фото и текст одним сообщением")
    await callback.message.answer("❗❗ГРАФФИТИ БУДУТ ПРИНИМАТЬСЯ , ТОЛЬКО С КООРДИНАТАМИ/АДРЕСОМ , ОСТАЛЬНОЕ ОТКЛОНИТСЯ❗❗")
    await state.set_state(AuthState.waiting_for_plus3_content)

@router.message(AuthState.waiting_for_plus3_content, F.photo)
async def handle_plus3_content(message: Message, state: FSMContext, bot: Bot):
    photo = message.photo[-1]
    caption = message.caption or ""
    photo_file = await bot.get_file(photo.file_id)
    photo_bytes = await bot.download_file(photo_file.file_path)
    
    # Store the photo in temporary storage
    timestamp = datetime.now().timestamp()
    key = f"{message.from_user.id}_{message.chat.id}_{timestamp}"
    if key not in user_messages:
        user_messages[key] = {
            'message': message,
            'photo': photo,
            'caption': caption,
            'timestamp': datetime.now(),
            'key': key,
            'user_id': message.from_user.id,
            'chat_id': message.chat.id
        }
        print(f"Stored photo message before forwarding to group with key {key}")

    
    # Send to group
    await bot.send_photo(
        chat_id=GROUP_ID,
        photo=BufferedInputFile(photo_bytes.read(), filename="photo.jpg"),
        caption=caption
    )
    
    await message.answer("Фото и текст успешно отправлены!")
    await state.clear()


    await bot.send_message(
        chat_id=GROUP_ID,
        text="Говорят что закрасили",
        
    )





    await callback.message.answer('9-ая парковая д52 корпус 1, возле 3 подьезда')
    with open("app/foto/ii.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('9-ая парковая дом 52 корпус 1, между 1 и 2 подьездами')
    with open("app/foto/pp.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('11-ая Парковая улица, дом 36 строение 3')
    with open("app/foto/bb.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
        await callback.message.answer('6я парковая 29А')
    with open("app/foto/ff.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('Сиреневый бульвар, 23А. около входа в озон')
    with open("app/foto/fff.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('На перекрестке, на стороне возле дома 9-парковая 49к2')
    with open("app/foto/ppp.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    
    await callback.message.answer('5 парковая 64')
    with open("app/foto/bbuuu.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('3-я парковая улица. дом 39. корпус 1')
    with open("app/foto/yxx.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('Щелковский шоссе 81')
    with open("app/foto/axx.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('Измайловский проспект, 49')
    with open("app/foto/exx.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('Щелковское шоссе 69 , Пятерочка')
    with open("app/foto/xexe.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('9 парковка улица 57(2) , за домом')
    with open("app/foto/xaxa.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)
    await callback.message.answer('Сиреневый бульвар дом 40 корпус 1')
    with open("app/foto/xsxs.jpg", "rb") as file:
        photo = BufferedInputFile(file.read(), filename="photo.jpg")
        await callback.message.answer_photo(photo)

    await callback.message.answer('5-я Парковая улица, 57, обе автобусные остановки')
    await callback.message.answer('Видео или фото граффити выше нет')

    await callback.message.answer('Щелковское шоссе 47, Щелковское шоссе 45а. Подземный переход')
    with open("app/foto/vid.mp4", "rb") as file:
        video = BufferedInputFile(file.read(), filename="vid.mp4")
        await callback.message.answer_video(video)
    




@router.callback_query(F.data == 'plus222')
async def handle_plus222(callback: CallbackQuery, bot: Bot):
    await callback.answer()
    # Send checkmark emoji
    await callback.message.answer("✅")

    await callback.message.edit_reply_markup(reply_markup=None)

@router.callback_query(F.data == 'plus111')
async def handle_plus222(callback: CallbackQuery, bot: Bot):
    await callback.answer()
    # Send checkmark emoji
    await callback.message.answer("❌")

    await callback.message.edit_reply_markup(reply_markup=None)
