from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from win32clipboard import OpenClipboard,EmptyClipboard,SetClipboardData,CF_DIB,CloseClipboard #pip install pywin32
from keyboard import press_and_release,add_hotkey #pip install keyboard
from PIL import Image,ImageDraw #pip install pillow
from io import BytesIO
from os import mkdir
def createNewFile(link=""):
    def typeFile(link="",rec=0):
        try:
            if(link=="db.txt"):
                with open('db.txt','w') as file:
                    file.write("Language:\nУкраїнська\nLanguages:\nУкраїнська;\nEnglish;\nEspanol;\nDeutsch;\n.\nHotkey:\non\n")
            elif(link[-4:]==".txt"):
                with open(link,'w') as file:
                    file.write("#error!\n"*33)
            elif(link[-4:]==".png"):
                image=Image.new('RGBA',(16,16),'#EEE1')
                image.save(link,"PNG")
            else:
                print("#file extension error!")
        except:
            try:
                for i in range(len(link)):
                    if(link[-i-1]=='/' or link[-i-1]=='\\'):
                        mkdir(link[:-i-1])
                if(rec):
                    print("#file error!")
                    return
                typeFile(link,1)
            except:
                print("#file error!")
    if(type(link)==str):
        typeFile(link)
        with open('file errors.txt','w') as file:
            file.write("Не вистачає файла:\n"+link+"\nЗамість нього була створена заглушка")
        print("Create new file:",link)
    elif(type(link)==list or type(link)==tuple):
        fileLink=[]
        with open('file errors.txt','w') as file:
            file.write("Не вистачає цих файлів:\n")
        for i in range(len(link)):
            try:
                file=open(link[i],'r')
                file.close()
            except:
                typeFile(link[i])
                fileLink.append(link[i])
                with open('file errors.txt','a+') as file:
                    file.write(link[i]+"\n")
        with open('file errors.txt','a+') as file:
            file.write("Замість них були створені заглушки")
        print("Create new files:",fileLink)
My_window=Tk()
translation=['',[],'']
onoffhotkey=BooleanVar(My_window)
try:
    with open('db.txt','r') as file:
        info=file.readlines()
except:
    createNewFile('db.txt')
    with open('db.txt','r') as file:
        info=file.readlines()
for i in range(len(info)):
    if(info[i]=="Language:\n"):
        translation[0]=info[i+1][:-1]
    if(info[i]=="Languages:\n"):
        for j in range(len(info)-i-1):
            if(info[j+i+1][:-1]!='.'):
                translation[1].append(info[j+i+1][:-2])
            else:
                break
    if(info[i]=="Hotkey:\n"):
        translation[2]=info[i+1][:-1]
        if(translation[2]=='on'):
            onoffhotkey.set(True)
        elif(translation[2]=='off'):
            onoffhotkey.set(False)
try:
    with open(f'translator/{translation[0]}.txt','r') as file:
        translationtext=file.readlines()
        for i in range(len(translationtext)):
            translationtext[i]=translationtext[i][0:-1]
except:
    haveNotFile=[]
    for i in range(len(translation[1])):
        haveNotFile.append(f'translator/{translation[1][i]}.txt')
    createNewFile(haveNotFile)
    with open(f'translator/{translation[0]}.txt','r') as file:
        translationtext=file.readlines()
        for i in range(len(translationtext)):
            translationtext[i]=translationtext[i][0:-1]
My_window.title(translationtext[0])
correction=IntVar()
typedata=IntVar()
correction.set(2)
typedata.set(3)
geom=[746,928]
data,bitdata='',''
heshtext=0
My_window.geometry(f"{geom[0]}x{geom[1]}+300+0")
My_window.resizable(width=False,height=False)
My_window["bg"]="#EEEEEE"
t1=Text(My_window,fg="#000000",bg="#FFFFFF",font=("Arial",12),width=82,height=3)
t1.place(x=2,y=0)
s1=Scale(My_window,orient=HORIZONTAL,relief=FLAT,length=geom[0]-160,from_=1,to=40,tickinterval=3,resolution=1,bg='#EEEEEE',font=("Arial",9))
s1.place(x=154,y=60)
l1=Label(My_window,text=translationtext[1],fg="#000000",bg="#EEEEEE",font=("Arial",12))
l1.place(x=5,y=77)
l2=Label(My_window,text=translationtext[2],fg="#000000",bg="#EEEEEE",font=("Arial",12))
l2.place(x=5,y=120)
r1=Radiobutton(My_window,text=translationtext[3],fg="#000000",bg="#EEEEEE",font=("Arial",12),variable=correction,value=1)
r1.place(x=230,y=120)
r2=Radiobutton(My_window,text=translationtext[4],fg="#000000",bg="#EEEEEE",font=("Arial",12),variable=correction,value=2)
r2.place(x=360,y=120)
r3=Radiobutton(My_window,text=translationtext[5],fg="#000000",bg="#EEEEEE",font=("Arial",12),variable=correction,value=3)
r3.place(x=490,y=120)
r4=Radiobutton(My_window,text=translationtext[6],fg="#000000",bg="#EEEEEE",font=("Arial",12),variable=correction,value=4)
r4.place(x=620,y=120)
l3=Label(My_window,text=translationtext[7],fg="#000000",bg="#EEEEEE",font=("Arial",12))
l3.place(x=5,y=155)
r5=Radiobutton(My_window,text=translationtext[8],fg="#000000",bg="#EEEEEE",font=("Arial",12),variable=typedata,value=1)
r5.place(x=230,y=155)
r6=Radiobutton(My_window,text=translationtext[9],fg="#000000",bg="#EEEEEE",font=("Arial",12),variable=typedata,value=2)
r6.place(x=360,y=155)
r7=Radiobutton(My_window,text=translationtext[10],fg="#000000",bg="#EEEEEE",font=("Arial",12),variable=typedata,value=3)
r7.place(x=490,y=155)
r8=Radiobutton(My_window,text=translationtext[11],fg="#000000",bg="#EEEEEE",font=("Arial",12),variable=typedata,value=4)
r8.place(x=620,y=155)
c1=Canvas(My_window,width=geom[0]-10,height=geom[0]-10,bg='#FFFFFF')
c1.place(x=3,y=185)
try:
    iconLink,icon=['icon/start.png','icon/open.png','icon/copy.png','icon/exit.png','icon/info.png','icon/setting.png','icon/none.png'],[]
    for i in range(len(iconLink)): #не задієні insert.png new.png save.png
        icon.append(PhotoImage(file=iconLink[i]))
except:
    icon=[]
    createNewFile(iconLink)
    for i in range(len(iconLink)):
        icon.append(PhotoImage(file=iconLink[i]))
AFPtemplate=[[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0],[0,1,0],[6,1,0],[0,2,0],[2,2,0],[3,2,0],[4,2,0],[6,2,0],[0,3,0],[2,3,0],
             [3,3,0],[4,3,0],[6,3,0],[0,4,0],[2,4,0],[3,4,0],[4,4,0],[6,4,0],[0,5,0],[6,5,0],[0,6,0],[1,6,0],[2,6,0],[3,6,0],[4,6,0],[5,6,0],[6,6,0],
             [1,1,1],[2,1,1],[3,1,1],[4,1,1],[5,1,1],[1,2,1],[5,2,1],[1,3,1],[5,3,1],[1,4,1],[5,4,1],[1,5,1],[2,5,1],[3,5,1],[4,5,1],[5,5,1],
             [0,7,1],[1,7,1],[2,7,1],[3,7,1],[4,7,1],[5,7,1],[6,7,1],[7,0,1],[7,1,1],[7,2,1],[7,3,1],[7,4,1],[7,5,1],[7,6,1],[7,7,1]]
AAPtemplate=[[0,0,0],[-1,-1,1],[-1,0,1],[-1,1,1],[0,-1,1],[0,1,1],[1,-1,1],[1,0,1],[1,1,1],[-2,-2,0],[-2,-1,0],[-2,0,0],[-2,1,0],
             [-2,2,0],[-1,-2,0],[-1,2,0],[0,-2,0],[0,2,0],[1,-2,0],[1,2,0],[2,-2,0],[2,-1,0],[2,0,0],[2,1,0],[2,2,0]]
VItemplate=[[-9,5],[-10,5],[-11,5],[-9,4],[-10,4],[-11,4],[-9,3],[-10,3],[-11,3],[-9,2],[-10,2],[-11,2],[-9,1],[-10,1],[-11,1],[-9,0],[-10,0],[-11,0]]
FStemplate1=[[-1,8],[-2,8],[-3,8],[-4,8],[-5,8],[-6,8],[-7,8],[8,-8],[8,-7],[8,-6],[8,-5],[8,-4],[8,-3],[8,-2],[8,-1]]
FStemplate2=[[8,0],[8,1],[8,2],[8,3],[8,4],[8,5],[8,7],[8,8],[7,8],[5,8],[4,8],[3,8],[2,8],[1,8],[0,8]]
LVRRB=[0,7,7,7,7,7,0,0,0,0,0,0,0,3,3,3,3,3,3,3,4,4,4,4,4,4,4,3,3,3,3,3,3,3,0,0,0,0,0,0]
CCI=[[10,9,8,8],[12,11,16,10],[14,13,16,12]]
TNV=['0','1','2','3','4','5','6','7','8','9']
TANV=['0','1','2','3','4','5','6','7','8','9',
      'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','$','%','*','+','-','.','/',':']
LFIS=[['111011111000100','111001011110011','111110110101010','111100010011101','110011000101111','110001100011000','110110001000001','110100101110110'],
      ['101010000010010','101000100100101','101111001111100','101101101001011','100010111111001','100000011001110','100111110010111','100101010100000'],
      ['011010101011111','011000001101000','011111100110001','011101000000110','010010010110100','010000110000011','010111011011010','010101111101101'],
      ['001011010001001','001001110111110','001110011100111','001100111010000','000011101100010','000001001010101','000110100001100','000100000111011'],]
AVIS=['000111110010010100','001000010110111100','001001101010011001','001010010011010011','001011101111110110','001100011101100010','001101100001000111',
      '001110011000001101','001111100100101000','010000101101111000','010001010001011101','010010101000010111','010011010100110010','010100100110100110',
      '010101011010000011','010110100011001001','010111011111101100','011000111011000100','011001000111100001','011010111110101011','011011000010001110',
      '011100110000011010','011101001100111111','011110110101110101','011111001001010000','100000100111010101','100001011011110000','100010100010111010',
      '100011011110011111','100100101100001011','100101010000101110','100110101001100100','100111010101000001','101000110001101001']
APLT=[[-1,-1,-1,-1,-1,-1,-1],[6,18,-1,-1,-1,-1,-1],[6,22,-1,-1,-1,-1,-1],[6,26,-1,-1,-1,-1,-1],[6,30,-1,-1,-1,-1,-1],
      [6,34,-1,-1,-1,-1,-1],[6,22,38,-1,-1,-1,-1],[6,24,42,-1,-1,-1,-1],[6,26,46,-1,-1,-1,-1],[6,28,50,-1,-1,-1,-1],
      [6,30,54,-1,-1,-1,-1],[6,32,58,-1,-1,-1,-1],[6,34,62,-1,-1,-1,-1],[6,26,46,66,-1,-1,-1],[6,26,48,70,-1,-1,-1],
      [6,26,50,74,-1,-1,-1],[6,30,54,78,-1,-1,-1],[6,30,56,82,-1,-1,-1],[6,30,58,86,-1,-1,-1],[6,34,62,90,-1,-1,-1],
      [6,28,50,72,94,-1,-1],[6,26,50,74,98,-1,-1],[6,30,54,78,102,-1,-1],[6,28,54,80,106,-1,-1],[6,32,58,84,110,-1,-1],
      [6,30,58,86,114,-1,-1],[6,34,62,90,118,-1,-1],[6,26,50,74,98,122,-1],[6,30,54,78,102,126,-1],[6,26,52,78,104,130,-1],
      [6,30,56,82,108,134,-1],[6,34,60,86,112,138,-1],[6,30,58,86,114,142,-1],[6,34,62,90,118,146,-1],[6,30,54,78,102,126,150],
      [6,24,50,76,102,128,154],[6,28,54,80,106,132,158],[6,32,58,84,110,136,162],[6,26,54,82,110,138,166],[6,30,58,86,114,142,170]]
CCVMEC=[[[41,25,17,10],[34,20,14,8],[27,16,11,7],[17,10,7,4]],
        [[77,47,32,20],[63,38,26,16],[48,29,20,12],[34,20,14,8]],
        [[127,77,53,32],[101,61,42,26],[77,47,32,20],[58,35,24,15]],
        [[187,114,78,48],[149,90,62,38],[111,67,46,28],[82,50,34,21]],
        [[255,154,106,65],[202,122,84,52],[144,87,60,37],[106,64,44,27]],
        [[322,195,134,82],[255,154,106,65],[178,108,74,45],[139,84,58,36]],
        [[370,224,154,95],[293,178,122,75],[207,125,86,53],[154,93,64,39]],
        [[461,279,192,118],[365,221,152,93],[259,157,108,66],[202,122,84,52]],
        [[552,335,230,141],[432,262,180,111],[312,189,130,80],[235,143,98,60]],
        [[652,395,271,167],[513,311,213,131],[364,221,151,93],[288,174,119,74]],
        [[772,468,321,198],[604,366,251,155],[427,259,177,109],[331,200,137,85]],
        [[883,535,367,226],[691,419,287,177],[489,296,203,125],[374,227,155,96]],
        [[1022,619,425,262],[796,483,331,204],[580,352,241,149],[427,259,177,109]],
        [[1101,667,458,282],[871,528,362,223],[621,376,258,159],[468,283,194,120]],
        [[1250,758,520,320],[991,600,412,254],[703,426,292,180],[530,321,220,136]],
        [[1408,854,586,361],[1082,656,450,277],[775,470,322,198],[602,365,250,154]],
        [[1548,938,644,397],[1212,734,504,310],[876,531,364,224],[674,408,280,173]],
        [[1725,1046,718,442],[1346,816,560,345],[948,574,394,243],[746,452,310,191]],
        [[1903,1153,792,488],[1500,909,624,384],[1063,644,442,272],[813,493,338,208]],
        [[2061,1249,858,528],[1600,970,666,410],[1159,702,482,297],[919,557,382,235]],
        [[2232,1352,929,572],[1708,1035,711,438],[1224,742,509,314],[969,587,403,248]],
        [[2409,1460,1003,618],[1872,1134,779,480],[1358,823,565,348],[1056,640,439,270]],
        [[2620,1588,1091,672],[2059,1248,857,528],[1468,890,611,376],[1108,672,461,284]],
        [[2812,1704,1171,721],[2188,1326,911,561],[1588,963,661,407],[1228,744,511,315]],
        [[3057,1853,1273,784],[2395,1451,997,614],[1718,1041,715,440],[1286,779,535,330]],
        [[3283,1990,1367,842],[2544,1542,1059,652],[1804,1094,751,462],[1425,864,593,365]],
        [[3517,2132,1465,902],[2701,1637,1125,692],[1933,1172,805,496],[1501,910,625,385]],
        [[3669,2223,1528,940],[2857,1732,1190,732],[2085,1263,868,534],[1581,958,658,405]],
        [[3909,2369,1628,1002],[3035,1839,1264,778],[2181,1322,908,559],[1677,1016,698,430]],
        [[4158,2520,1732,1066],[3289,1994,1370,843],[2358,1429,982,604],[1782,1080,742,457]],
        [[4417,2677,1840,1132],[3486,2113,1452,894],[2473,1499,1030,634],[1897,1150,790,486]],
        [[4686,2840,1952,1201],[3693,2238,1538,947],[2670,1618,1112,684],[2022,1226,842,518]],
        [[4965,3009,2068,1273],[3909,2369,1628,1002],[2805,1700,1168,719],[2157,1307,898,553]],
        [[5253,3183,2188,1347],[4134,2506,1722,1060],[2949,1787,1228,756],[2301,1394,958,590]],
        [[5529,3351,2303,1417],[4343,2632,1809,1113],[3081,1867,1283,790],[2361,1431,983,605]],
        [[5836,3537,2431,1496],[4588,2780,1911,1176],[3244,1966,1351,832],[2524,1530,1051,647]],
        [[6153,3729,2563,1577],[4775,2894,1989,1224],[3417,2071,1423,876],[2625,1591,1093,673]],
        [[6479,3927,2699,1661],[5039,3054,2099,1292],[3599,2181,1499,923],[2735,1658,1139,701]],
        [[6743,4087,2809,1729],[5313,3220,2213,1362],[3791,2298,1579,972],[2927,1774,1219,750]],
        [[7089,4296,2953,1817],[5596,3391,2331,1435],[3993,2420,1663,1024],[3057,1852,1273,784]]]
ECCWBI=[[[19,7,1,19,0,0],[16,10,1,16,0,0],[13,13,1,13,0,0],[9,17,1,9,0,0]],
        [[34,10,1,34,0,0],[28,16,1,28,0,0],[22,22,1,22,0,0],[16,28,1,16,0,0]],
        [[55,15,1,55,0,0],[44,26,1,44,0,0],[34,18,1,17,0,0],[26,22,2,13,0,0]],
        [[80,20,1,80,0,0],[64,18,2,32,0,0],[48,26,2,24,0,0],[36,16,4,9,0,0]],
        [[108,26,1,108,0,0],[86,24,2,43,0,0],[62,18,2,15,2,16],[46,22,2,11,2,12]],
        [[136,18,2,68,0,0],[108,16,4,27,0,0],[76,24,4,19,0,0],[60,28,4,15,0,0]],
        [[156,20,2,78,0,0],[124,18,4,31,0,0],[88,18,2,14,4,15],[66,26,4,13,1,14]],
        [[194,24,2,97,0,0],[154,22,2,38,2,39],[110,22,4,18,2,19],[86,26,4,14,2,15]],
        [[232,30,2,116,0,0],[182,22,3,36,2,37],[132,20,4,16,4,17],[100,24,4,12,4,13]],
        [[274,18,2,68,2,69],[216,26,4,43,1,44],[154,24,6,19,2,20],[122,28,6,15,2,16]],
        [[324,20,4,81,0,0],[254,30,1,50,4,51],[180,28,4,22,4,23],[140,24,3,12,8,13]],
        [[370,24,2,92,2,93],[290,22,6,36,2,37],[206,26,4,20,6,21],[158,28,7,14,4,15]],
        [[428,26,4,107,0,0],[334,22,8,37,1,38],[244,24,8,20,4,21],[180,22,12,11,4,12]],
        [[461,30,3,115,1,116],[365,24,4,40,5,41],[261,20,11,16,5,17],[197,24,11,12,5,13]],
        [[523,22,5,87,1,88],[415,24,5,41,5,42],[295,30,5,24,7,25],[223,24,11,12,7,13]],
        [[589,24,5,98,1,99],[453,28,7,45,3,46],[325,24,15,19,2,20],[253,30,3,15,13,16]],
        [[647,28,1,107,5,108],[507,28,10,46,1,47],[367,28,1,22,15,23],[283,28,2,14,17,15]],
        [[721,30,5,120,1,121],[563,26,9,43,4,44],[397,28,17,22,1,23],[313,28,2,14,19,15]],
        [[795,28,3,113,4,114],[627,26,3,44,11,45],[445,26,17,21,4,22],[341,26,9,13,16,14]],
        [[861,28,3,107,5,108],[669,26,3,41,13,42],[485,30,15,24,5,25],[385,25,28,15,10,16]],
        [[932,28,4,116,4,117],[714,26,17,42,0,0],[512,28,17,22,6,23],[406,30,19,16,6,17]],
        [[1006,28,2,111,7,112],[782,28,17,46,0,0],[568,30,7,24,16,25],[442,24,34,13,0,0]],
        [[1094,30,4,121,5,122],[860,28,4,47,14,48],[614,30,11,24,14,25],[464,30,16,15,14,16]],
        [[1174,30,6,117,4,118],[914,28,6,45,14,46],[664,30,11,24,16,25],[514,30,30,16,2,17]],
        [[1276,26,8,106,4,107],[1000,28,8,47,13,48],[718,30,7,24,22,25],[538,30,22,15,13,16]],
        [[1370,28,10,114,2,115],[1062,28,19,46,4,47],[754,47,28,22,6,23],[596,30,33,16,4,17]],
        [[1468,30,8,122,4,123],[1128,28,22,45,3,46],[808,30,8,23,26,24],[628,30,12,15,28,16]],
        [[1531,30,3,117,10,118],[1193,28,3,45,23,46],[871,30,4,24,31,25],[661,30,11,15,31,16]],
        [[1631,30,7,116,7,117],[1267,28,21,45,7,46],[911,30,1,23,37,24],[701,30,19,15,26,16]],
        [[1735,30,5,115,10,116],[1373,28,19,47,10,48],[985,48,30,15,24,25],[745,30,23,15,25,16]],
        [[1843,30,13,115,3,116],[1455,28,2,46,29,47],[1033,30,42,24,1,25],[793,30,23,15,28,16]],
        [[1955,30,17,115,0,0],[1541,28,10,46,23,47],[1115,30,10,24,35,25],[845,30,19,15,35,16]],
        [[2071,30,17,115,1,116],[1631,28,14,46,21,47],[1171,30,29,24,19,25],[901,30,11,15,46,16]],
        [[2191,30,13,115,6,116],[1725,28,14,46,23,47],[1231,30,44,24,7,25],[961,30,59,16,1,17]],
        [[2306,30,12,121,7,122],[1812,28,12,47,26,48],[1286,30,39,24,14,25],[986,30,22,15,41,16]],
        [[2434,30,6,121,14,122],[1914,28,6,47,34,48],[1354,30,46,24,10,25],[1054,30,2,15,64,16]],
        [[2566,30,17,122,4,123],[1992,28,29,46,14,47],[1426,30,49,24,10,25],[1096,30,24,15,46,16]],
        [[2702,30,4,122,18,123],[2102,28,13,46,32,47],[1502,30,48,24,14,25],[1142,30,42,15,32,16]],
        [[2812,30,20,117,4,118],[2216,28,40,47,7,48],[1582,30,43,24,22,25],[1222,30,10,15,67,16]],
        [[2956,30,19,118,6,119],[2334,28,18,47,31,48],[1666,30,34,24,34,25],[1276,30,20,15,61,16]]]
def openfile(link=""):
    global data,heshtext
    if(link==""):
        name=filedialog.askopenfilenames(parent=My_window,initialdir='/Users/User/Documents',initialfile='image',filetypes=[("All files","*")])
        gen=1
    else:
        name=(link,)
        gen=0
    try:
        with open(name[0],'rb') as file:
            data=file.read()
    except:
        messagebox.showerror(title=translationtext[21],message=translationtext[22])
        return
    typedata.set(3)
    t1.delete(0.1,END)
    t1.insert(END,data)
    heshtext=hash(t1.get(0.1,END))
    if(gen):
        QRCodeGenerator()
def info():
    messagebox.showinfo(title=translationtext[23],message=translationtext[24]+'\n'+translationtext[25])
def copy():
    try:
        image=Image.open('QR code.png')
    except:
       createNewFile('QR code.png') 
    output=BytesIO()
    image.convert("RGB").save(output,"BMP")
    copydata=output.getvalue()[14:]
    output.close()
    OpenClipboard()
    EmptyClipboard()
    SetClipboardData(CF_DIB,copydata)
    CloseClipboard()
def settings(t,s=0):
    try:
        with open('db.txt','r') as file:
            info=file.readlines()
    except:
        createNewFile('db.txt')
    for i in range(len(info)):
        if(info[i]=="Language:\n" and t=="Language:\n"):
            info[i+1]=f"{s}\n"
        if(info[i]=="Hotkey:\n" and t=="Hotkey:\n"):
            if(info[i+1]=='on\n'):
                info[i+1]='off\n'
            elif(info[i+1]=='off\n'):
                info[i+1]='on\n'
    infostr=""
    for i in range(len(info)):
        infostr=infostr+info[i]
    with open('db.txt','w') as file:
        file.write(infostr)
    return s
def CorrectData():
    global data,TNV,TANV
    td=typedata.get()
    if(td==1):
        if((set(data)-set(TNV))!=set()):
            an=messagebox.askyesno(title=translationtext[28],message=translationtext[29])
            if(an):
                typedata.set(3)
                data=bytes(t1.get(0.1,END),'utf-8')
                return 1
            return 0
        return 1
    if(td==2):
        if((set(data)-set(TANV))!=set()):
            an=messagebox.askyesno(title=translationtext[28],message=translationtext[29])
            if(an):
                typedata.set(3)
                data=bytes(t1.get(0.1,END),'utf-8')
                return 1
            return 0
        return 1
    if(td==3):
        if(type(data)==str):
            data=bytes(data,'utf-8')
        return 1
    if(td==4):
        def bytesToInt(b):
            n=0
            for i in range(len(b)):
                n=n+b[-i-1]*256**i
            return n
        for i in range(len(data)):
            ok=0
            b=bytesToInt(bytes(data[i],'Shift JIS'))
            if((33088<b and b<40956) or (57408<b and b<60351)):
                ok=1
            if(ok==0):
                an=messagebox.askyesno(title=translationtext[28],message=translationtext[29])
                if(an):
                    typedata.set(3)
                    data=bytes(data,'utf-8')
                    return 1
                return 0
        return 1
def FindMinSizeQRCode():
    global data,CCVMEC
    V=s1.get()
    while(V<=40 and len(data)>CCVMEC[V-1][correction.get()-1][typedata.get()-1]):
        V=V+1
    if(V>40):
        messagebox.showerror(title=translationtext[21],message=translationtext[26]+f"{CCVMEC[39][correction.get()-1][typedata.get()-1]}"+translationtext[27])
        return
    if(V>s1.get()):
        s1.set(V)
def DataEncoding():
    global bitdata,CCI,ECCWBI,TANV
    nbits=ECCWBI[s1.get()-1][correction.get()-1][0]*8
    MI=["0001","0010","0100","1000","0111"]
    bitdata=MI[typedata.get()-1]
    if(1<=s1.get() and s1.get()<=9):
        b=bin(len(data))[2:]
        bitdata=bitdata+'0'*(CCI[0][typedata.get()-1]-len(b))+b
    elif(10<=s1.get() and s1.get()<=26):
        b=bin(len(data))[2:]
        bitdata=bitdata+'0'*(CCI[1][typedata.get()-1]-len(b))+b
    elif(27<=s1.get() and s1.get()<=40):
        b=bin(len(data))[2:]
        bitdata=bitdata+'0'*(CCI[2][typedata.get()-1]-len(b))+b
    if(typedata.get()==1):
        for i in range(len(data)//3):
            b=bin(int(data[i*3:i*3+3]))[2:]
            lb=len(str(int(data[i*3:i*3+3])))
            if(lb==3):
                bitdata=bitdata+'0'*(10-len(b))+b
            elif(lb==2):
                bitdata=bitdata+'0'*(7-len(b))+b
            elif(lb==1):
                bitdata=bitdata+'0'*(4-len(b))+b
        if(len(data)%3!=0):
            b=bin(int(data[len(data)%3*-1:]))[2:]
            lb=len(data)%3
            if(lb==2):
                bitdata=bitdata+'0'*(7-len(b))+b
            elif(lb==1):
                bitdata=bitdata+'0'*(4-len(b))+b
    elif(typedata.get()==2):
        for i in range(len(data)//2):
            b=bin(TANV.index(data[i*2])*45+TANV.index(data[i*2+1]))[2:]
            bitdata=bitdata+'0'*(11-len(b))+b
        if(len(data)%2!=0):
            b=bin(TANV.index(data[-1]))[2:]
            bitdata=bitdata+'0'*(6-len(b))+b
    elif(typedata.get()==3):
        for i in range(len(data)):
            b=bin(int(data[i]))[2:]
            bitdata=bitdata+'0'*(8-len(b))+b
    elif(typedata.get()==4):
        def bytesToInt(b):
            n=0
            for i in range(len(b)):
                n=n+b[-i-1]*256**i
            return n
        for i in range(len(data)):
            b=bytesToInt(bytes(data[i],'Shift JIS'))
            if(33088<b and b<40956):
                b=b-33088
                mb,lb=b//256,b%256
                b=bin(mb*192+lb)[2:]
                bitdata=bitdata+'0'*(13-len(b))+b
            elif(57408<b and b<60351):
                b=b-49472
                mb,lb=b//256,b%256
                b=bin(mb*192+lb)[2:]
                bitdata=bitdata+'0'*(13-len(b))+b
    if(len(bitdata)+4>nbits):
        bitdata=bitdata+'0'*(nbits-len(bitdata))
    else:
        bitdata=bitdata+'0000'
    if(len(bitdata)%8!=0):
        bitdata=bitdata+'0'*(8-len(bitdata)%8)
    while(len(bitdata)<nbits):
        bitdata=bitdata+'1110110000010001'
    bitdata=bitdata[:nbits]
    print(bitdata,type(bitdata),len(bitdata))


def ErrorCorrectionCoding(ndata,ncor):
    BytesCorrection=[0]*ncor
    #складний алгоритм що повертає байти корекції
    return BytesCorrection

def StructureFinalMessage():
    global bitdata,ECCWBI,LVRRB
    V,cor,ndata,codewords,ib=s1.get()-1,correction.get()-1,[],[],0
    for i in range(ECCWBI[V][cor][2]):
        ndata.append([])
        for j in range(ECCWBI[V][cor][3]):
            ndata[i].append(int(bitdata[ib*8:ib*8+8],2))
            ib=ib+1
    for i in range(ECCWBI[V][cor][4]):
        ndata.append([])
        for j in range(ECCWBI[V][cor][5]):
            ndata[-1].append(int(bitdata[ib*8:ib*8+8],2))
            ib=ib+1
    for i in range(len(ndata)):
        codewords.append(ErrorCorrectionCoding(ndata[i],ECCWBI[V][cor][1]))
    bitdata=""
    for i in range(len(ndata[-1])):
        for j in range(len(ndata)):
            try:
                b=bin(ndata[j][i])[2:]
                bitdata=bitdata+'0'*(8-len(b))+b
            except IndexError:
                pass
    for i in range(len(codewords[0])):
        for j in range(len(codewords)):
            b=bin(codewords[j][i])[2:]
            bitdata=bitdata+'0'*(8-len(b))+b
    print("Bits corection to QRCode")
    bitdata=bitdata+"0"*LVRRB[s1.get()-1]


def RemainderBits():
    global bitdata,LVRRB
    bitdata=bitdata+"0"*LVRRB[s1.get()-1]
def CreateQRCode():
    QRCode=[[]]
    S=17+s1.get()*4
    for i in range(S):
        QRCode[0].append(0)
    for i in range(S-1):
        QRCode.append(QRCode[0].copy())
    return QRCode
def QRCodeTemplate(QRCode,TFN=(1,0,-1)):
    global AFPtemplate,AAPtemplate,APLT
    V=s1.get()
    S=17+V*4
    if(TFN[2]>=0):
        for i in range(9):
            QRCode[i][8]=TFN[2]
            QRCode[-i][8]=TFN[2]
            QRCode[8][i]=TFN[2]
            QRCode[8][-i]=TFN[2]
    for i in range(S):
        if(i%2==0):
            QRCode[i][6]=TFN[0]
            QRCode[6][i]=TFN[0]
        else:
            QRCode[i][6]=TFN[1]
            QRCode[6][i]=TFN[1]
    for i in range(len(AFPtemplate)):
        QRCode[AFPtemplate[i][1]][AFPtemplate[i][0]]=TFN[AFPtemplate[i][2]]
        QRCode[-AFPtemplate[i][1]-1][AFPtemplate[i][0]]=TFN[AFPtemplate[i][2]]
        QRCode[AFPtemplate[i][1]][-AFPtemplate[i][0]-1]=TFN[AFPtemplate[i][2]]
    QRCode[-8][8]=TFN[0]
    for i in range(7):
        for j in range(7):
            if(APLT[V-1][i]>0 and APLT[V-1][j]>0):
                if(APLT[V-1][i]==6 or APLT[V-1][j]==6):
                    if(not((APLT[V-1][i]==6 and APLT[V-1][j]==6)or(APLT[V-1][i]==6 and APLT[V-1][j]==S-7)or(APLT[V-1][i]==S-7 and APLT[V-1][j]==6))):
                        for k in range(len(AAPtemplate)):
                            QRCode[APLT[V-1][i]+AAPtemplate[k][0]][APLT[V-1][j]+AAPtemplate[k][1]]=TFN[AAPtemplate[k][2]]
                else:
                    for k in range(len(AAPtemplate)):
                        QRCode[APLT[V-1][i]+AAPtemplate[k][0]][APLT[V-1][j]+AAPtemplate[k][1]]=TFN[AAPtemplate[k][2]]
    if(V>=7):
        for i in range(6):
            for j in range(3):
                QRCode[-j-9][i]=TFN[2]
                QRCode[i][-j-9]=TFN[2]
    return QRCode
def BitsInQRCode(QRCode):
    global bitdata
    n=0
    S=17+s1.get()*4
    vector=1
    cursor=[S-1,S-1]
    for i in range(S*S-S):
        if(QRCode[cursor[0]][cursor[1]]==0):
            QRCode[cursor[0]][cursor[1]]=int(bitdata[n])
            n=n+1
            if(n>=len(bitdata)):
                break
        if(i%2==0):
            cursor[1]=cursor[1]-1
        else:
            cursor[0]=cursor[0]-vector
            cursor[1]=cursor[1]+1
        if(cursor[0]<0 or cursor[0]>S-1):
            vector=vector*-1
            cursor[0]=cursor[0]-vector
            cursor[1]=cursor[1]-2
        if(cursor[1]==6):
            cursor[1]=cursor[1]-1
    return QRCode
def QRCodeVersionInformation(QRCode):
    global VItemplate,AVIS
    V=s1.get()
    for i in range(len(VItemplate)):
        QRCode[VItemplate[i][0]][VItemplate[i][1]]=int(AVIS[V-7][i])
        QRCode[VItemplate[i][1]][VItemplate[i][0]]=int(AVIS[V-7][i])
    return QRCode
def Copy2DList(OldList2D):
    List2D=[]
    for i in range(len(OldList2D)):
        List2D.append(OldList2D[i].copy())
    return List2D
def DataMasking(QRCode,DoNotMask,mask):
    global FStemplate1,FStemplate2,LFIS
    for i in range(len(LFIS[0][0])):
        QRCode[FStemplate1[i][0]][FStemplate1[i][1]]=int(LFIS[correction.get()-1][mask][i])
        QRCode[FStemplate2[i][0]][FStemplate2[i][1]]=int(LFIS[correction.get()-1][mask][i])
    if(mask==0):
        for i in range(len(QRCode)):
            for j in range(len(QRCode)):
                if((i+j)%2==0 and DoNotMask[i][j]==0):
                    QRCode[i][j]=QRCode[i][j]^1
    elif(mask==1):
        for i in range(len(QRCode)):
            for j in range(len(QRCode)):
                if(i%2==0 and DoNotMask[i][j]==0):
                    QRCode[i][j]=QRCode[i][j]^1
    elif(mask==2):
        for i in range(len(QRCode)):
            for j in range(len(QRCode)):
                if(j%3==0 and DoNotMask[i][j]==0):
                    QRCode[i][j]=QRCode[i][j]^1
    elif(mask==3):
        for i in range(len(QRCode)):
            for j in range(len(QRCode)):
                if((i+j)%3==0 and DoNotMask[i][j]==0):
                    QRCode[i][j]=QRCode[i][j]^1
    elif(mask==4):
        for i in range(len(QRCode)):
            for j in range(len(QRCode)):
                if((i//2+j//3)%2==0 and DoNotMask[i][j]==0):
                    QRCode[i][j]=QRCode[i][j]^1
    elif(mask==5):
        for i in range(len(QRCode)):
            for j in range(len(QRCode)):
                if((i*j)%2+(i*j)%3==0 and DoNotMask[i][j]==0):
                    QRCode[i][j]=QRCode[i][j]^1
    elif(mask==6):
        for i in range(len(QRCode)):
            for j in range(len(QRCode)):
                if(((i*j)%3+i*j)%2==0 and DoNotMask[i][j]==0):
                    QRCode[i][j]=QRCode[i][j]^1
    elif(mask==7):
        for i in range(len(QRCode)):
            for j in range(len(QRCode)):
                if(((i*j)%3+i+j)%2==0 and DoNotMask[i][j]==0):
                    QRCode[i][j]=QRCode[i][j]^1
    return QRCode
def QRCodePenalty(QRCode):
    Penalty=0
    ColRep=1
    for i in range(len(QRCode)):
        for j in range(1,len(QRCode)):
            if(QRCode[i][j]==QRCode[i][j-1]):
                ColRep=ColRep+1
            else:
                if(ColRep>=5):
                    Penalty=Penalty+ColRep-2
                ColRep=1
    if(ColRep>=5):
        Penalty=Penalty+ColRep-2
    ColRep=1
    for i in range(len(QRCode)):
        for j in range(1,len(QRCode)):
            if(QRCode[j][i]==QRCode[j][i-1]):
                ColRep=ColRep+1
            else:
                if(ColRep>=5):
                    Penalty=Penalty+ColRep-2
                ColRep=1
    if(ColRep>=5):
        Penalty=Penalty+ColRep-2
    for i in range(1,len(QRCode)):
        for j in range(1,len(QRCode)):
            if(QRCode[i][j]==QRCode[i][j-1] and QRCode[i][j]==QRCode[i-1][j] and QRCode[i][j]==QRCode[i-1][j-1]):
                Penalty=Penalty+3
    pattern=['10111010000','00001011101']
    for i in range(len(QRCode)):
        for j in range(len(QRCode)-len(pattern[0])+1):
            equal=1
            for k in range(len(pattern[0])):
                if(QRCode[i][j+k]!=int(pattern[0][k])):
                    equal=0
                    break
            if(equal):
                Penalty=Penalty+40
            equal=1
            for k in range(len(pattern[0])):
                if(QRCode[i][j+k]!=int(pattern[1][k])):
                    equal=0
                    break
            if(equal):
                Penalty=Penalty+40
    for i in range(len(QRCode)):
        for j in range(len(QRCode)-len(pattern[0])+1):
            equal=1
            for k in range(len(pattern[0])):
                if(QRCode[j+k][i]!=int(pattern[0][k])):
                    equal=0
                    break
            if(equal):
                Penalty=Penalty+40
            equal=1
            for k in range(len(pattern[0])):
                if(QRCode[j+k][i]!=int(pattern[1][k])):
                    equal=0
                    break
            if(equal):
                Penalty=Penalty+40    
    SumQRCode=0
    SizeQRCode=len(QRCode)**2
    for i in range(len(QRCode)):
        SumQRCode=SumQRCode+sum(QRCode[i])
    Penalty=Penalty+min(int(abs((((SumQRCode*100)/SizeQRCode)//5)-10)),int(abs((((SumQRCode*100)/SizeQRCode)//5+1)-10)))*10
    return Penalty
def MaskingQRCode(QRCode):
    PenaltyMasking=[0]*8
    DoNotMask=QRCodeTemplate(CreateQRCode(),(1,1,1))
    for i in range(len(PenaltyMasking)):
        PenaltyMasking[i]=QRCodePenalty(DataMasking(Copy2DList(QRCode),DoNotMask,i))
    print(PenaltyMasking,min(PenaltyMasking),PenaltyMasking.index(min(PenaltyMasking)))
    QRCode=DataMasking(QRCode,DoNotMask,PenaltyMasking.index(min(PenaltyMasking)))
    return QRCode
def DrawQRCode(QRCode):
    c1.delete("all")
    c1size=geom[0]-6
    MQRCode=c1size//(len(QRCode)+8)
    offset=(c1size-len(QRCode)*MQRCode)//2
    for i in range(len(QRCode)):
        for j in range(len(QRCode[0])):
            if(QRCode[i][j]):
                c1.create_rectangle(j*MQRCode+offset,i*MQRCode+offset,j*MQRCode+offset+MQRCode-1,i*MQRCode+offset+MQRCode-1,fill='#000',outline='#000')
def SaveQRCode(QRCode):
    QuietZone=4
    image=Image.new('1',(len(QRCode)+QuietZone*2,len(QRCode)+QuietZone*2),'#FFF')
    draw=ImageDraw.Draw(image)
    for i in range(len(QRCode)):
        for j in range(len(QRCode[0])):
            if(QRCode[j][i]):
                draw.point((i+QuietZone,j+QuietZone),(0))
            else:
                draw.point((i+QuietZone,j+QuietZone),(255))
    image.save("QR code.png", "PNG")
def CommandProcessing():
    global data
    try:
        if(data[:5]=="/open"):
            argument=data[6:]
            try:
                for i in range(len(argument)):
                    if(argument[i]=='\\'):
                        argument=argument[:i]+'/'+argument[i+1:]
                    elif(argument[i]=='\n'):
                        argument=argument[:i]+argument[i+1:]
            except IndexError:
                pass
            openfile(argument)
    except IndexError:
        return
def QRCodeGenerator():
    global data,heshtext
    if(heshtext!=hash(t1.get(0.1,END))):
        try:
            f=lambda d: f(d[:-1]) if d[-1]=='\n' else d
            data=f(t1.get(0.1,END))
            heshtext=hash(t1.get(0.1,END))
            if(data[0]=="/"):
                CommandProcessing()
        except IndexError:
            messagebox.showinfo(title=translationtext[28],message=translationtext[30])
    if(not CorrectData()):
        return
    FindMinSizeQRCode()
    DataEncoding()
    StructureFinalMessage() #потребує реалізації алгоритма виправлення помилок Ріда-Соломона. Поки не розібрався зі складною математикою
    QRCode=CreateQRCode()
    QRCode=QRCodeTemplate(QRCode,(1,1,1))
    QRCode=BitsInQRCode(QRCode)
    QRCode=QRCodeTemplate(QRCode,(1,0,0))
    if(s1.get()>=7):
        QRCode=QRCodeVersionInformation(QRCode)
    QRCode=MaskingQRCode(QRCode)
    print(type(data),len(data),data)
    print(type(bitdata),len(bitdata),bitdata)
    print(QRCode)
    DrawQRCode(QRCode)
    SaveQRCode(QRCode)
def MenuSettings():
    global icon
    mainmenu=Menu(My_window)
    My_window.config(menu=mainmenu)
    filemenu=Menu(mainmenu, tearoff=0)
    filemenu.add_command(label=translationtext[13],accelerator="Ctrl+O",image=icon[1],compound='left',command=openfile)
    filemenu.add_command(label=translationtext[14],accelerator="Ctrl+C",image=icon[2],compound='left',command=copy)
    filemenu.add_command(label=translationtext[12],accelerator="Enter",image=icon[0],compound='left',command=QRCodeGenerator)
    filemenu.add_separator()
    filemenu.add_command(label=translationtext[15],accelerator="Alt+F4",image=icon[-1],compound='left',command=quit)
    settings_menu=Menu(tearoff=0)
    for i in range(len(translation[1])):
        settings_menu.add_command(label=translation[1][i],command=lambda t='Language:\n',s=translation[1][i]: settings(t,s))
    settingsmenu=Menu(mainmenu, tearoff=0)
    settingsmenu.add_command(label=translationtext[16],image=icon[4],compound='left',command=info)
    settingsmenu.add_separator()
    settingsmenu.add_cascade(label=translationtext[17],image=icon[5],compound='left',menu=settings_menu)
    settingsmenu.add_checkbutton(label=translationtext[18],accelerator=translation[2],onvalue=1,offvalue=0,variable=onoffhotkey,command=lambda: settings('Hotkey:\n'))
    mainmenu.add_cascade(label=translationtext[19],menu=filemenu)
    mainmenu.add_cascade(label=translationtext[20], menu=settingsmenu)
    if(translation[2]=='on'):
        add_hotkey('enter',QRCodeGenerator)
        add_hotkey('ctrl+o',openfile)
        add_hotkey('ctrl+c',copy)
b1=Button(My_window,text='✔',bg='#FFFFFF',command=QRCodeGenerator)
b1.place(x=719,y=140)
MenuSettings()
t1.insert(0.1,translationtext[-1])
My_window.mainloop()
#Всю інформацію про генерацію QR code я взяв з https://www.thonky.com/qr-code-tutorial
#А зацікавився темою після цього відео https://www.youtube.com/watch?v=dRO2c8dj3RY&t=824s рекомендую подивитися