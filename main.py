from tkinter import *

listTags = ['hand1', 'hand2', 'hand3',
            'hand4', 'hand5', 'hand6',
            'hand7', 'hand8']

def StartButton():
    print(RadVar.get())
    if(RadVar.get() == '1'):
        for i in listTags:
            canvas.delete(i)
        #79 73 677 271
        labelAnsw["text"] = 'Impact current: ' + str(OneHandTouch()) + ' mA'
        if(OneHandTouch() <= 5):
            canvas.create_line(668, 317, 691, 276, width=3, fill = 'black',tags='hand1')
            canvas.create_line(691, 276, 696, 222, width=3, fill='black', tags='hand2')
            canvas.create_line(591, 319, 591, 405, width=3, fill='black', tags='hand3')
            canvas.create_image(589+24+12, 244+30+8, image = face1, tags = 'hand7')
        elif(5 < OneHandTouch() <= 50):
            canvas.create_line(668, 317, 691, 276, width=3, fill = 'black',tags='hand1')
            canvas.create_line(691, 276, 696, 222, width=3, fill='black', tags='hand2')
            canvas.create_line(591, 319, 581, 370, width=3, fill='black', tags='hand3')
            canvas.create_line(581, 370, 591, 405 , width=3, fill='black', tags='hand4')
            canvas.create_image(589 + 24 + 12, 244 + 30 + 8, image=face2, tags='hand7')
        elif(50 < OneHandTouch() <= 90):
            canvas.create_line(668, 317, 691, 276, width=3, fill = 'black',tags='hand1')
            canvas.create_line(691, 276, 696, 222, width=3, fill='black', tags='hand2')
            canvas.create_line(591, 319, 591, 405, width=3, fill='black', tags='hand3')
            canvas.create_image(589 + 41, 244+130, image=heart, tags='hand4')
            canvas.create_image(589 + 24 + 12, 244 + 30 + 8, image=face3, tags='hand5')
        else:
            canvas.create_line(668, 317, 691, 276, width=3, fill='black', tags='hand1')
            canvas.create_line(691, 276, 696, 222, width=3, fill='black', tags='hand2')
            canvas.create_line(591, 319, 591, 405, width=3, fill='black', tags='hand3')
            canvas.create_image(589 + 41, 244 + 85, image=fire, tags='hand4')
            canvas.create_image(589 + 24 + 12, 244 + 30 + 8, image=face3, tags='hand5')
    if(RadVar.get() == '2'):
        for i in listTags:
            canvas.delete(i)

        labelAnsw["text"] = 'Impact current: ' + str(TwoHandTouch()) + ' mA'
        if(TwoHandTouch() <= 5):
            canvas.create_line(668, 317, 691, 276, width=3, fill='black', tags='hand1')
            canvas.create_line(691, 276, 696, 222, width=3, fill='black', tags='hand2')
            canvas.create_line(591, 319, 585, 228, width=3, fill='black', tags='hand3')
            canvas.create_line(585, 228, 606, 160, width=3, fill='black', tags='hand4')
            canvas.create_image(589+24+12, 244+30+8, image = face1, tags = 'hand7')
        elif(5 < TwoHandTouch() <= 50):
            canvas.create_line(668, 317, 691, 276, width=3, fill='black', tags='hand1')
            canvas.create_line(691, 276, 696, 222, width=3, fill='black', tags='hand2')
            canvas.create_line(591, 319, 585, 228, width=3, fill='black', tags='hand3')
            canvas.create_line(585, 228, 606, 160, width=3, fill='black', tags='hand4')
            canvas.create_image(589 + 24 + 12, 244 + 30 + 8, image=face2, tags='hand7')
        elif(50 < TwoHandTouch() <= 90):
            canvas.create_line(668, 317, 691, 276, width=3, fill='black', tags='hand1')
            canvas.create_line(691, 276, 696, 222, width=3, fill='black', tags='hand2')
            canvas.create_line(591, 319, 585, 228, width=3, fill='black', tags='hand3')
            canvas.create_line(585, 228, 606, 160, width=3, fill='black', tags='hand4')
            canvas.create_image(589 + 41, 244+130, image=heart, tags='hand5')
            canvas.create_image(589 + 24 + 12, 244 + 30 + 8, image=face3, tags='hand6')
        else:
            canvas.create_line(668, 317, 691, 276, width=3, fill='black', tags='hand1')
            canvas.create_line(691, 276, 696, 222, width=3, fill='black', tags='hand2')
            canvas.create_line(591, 319, 585, 228, width=3, fill='black', tags='hand3')
            canvas.create_line(585, 228, 606, 160, width=3, fill='black', tags='hand4')
            canvas.create_image(589 + 41, 244 + 85, image=fire, tags='hand5')
            canvas.create_image(589 + 24 + 12, 244 + 30 + 8, image=face3, tags='hand6')

    if(RadVar.get() == '3'):
        for i in listTags:
            canvas.delete(i)
        labelAnsw["text"] = 'Impact current: ' + str(CorpWithout()) + ' mA'
        if(CorpWithout() <= 5):
            canvas.create_line(668, 317, 793, 228, width=3, fill='black', tags='hand1')
            canvas.create_line(591, 319, 591, 405, width=3, fill='black', tags='hand2')
            canvas.create_image(589+24+12, 244+30+8, image = face1, tags = 'hand7')
        elif(5 < CorpWithout() <= 50):
            canvas.create_line(668, 317, 793, 228, width=3, fill='black', tags='hand1')
            canvas.create_line(591, 319, 591, 405, width=3, fill='black', tags='hand2')
            canvas.create_image(589 + 24 + 12, 244 + 30 + 8, image=face2, tags='hand7')
        elif(50 < CorpWithout() <= 90):
            canvas.create_line(668, 317, 793, 228, width=3, fill='black', tags='hand1')
            canvas.create_line(591, 319, 591, 405, width=3, fill='black', tags='hand2')
            canvas.create_image(589 + 41, 244+130, image=heart, tags='hand5')
            canvas.create_image(589 + 24 + 12, 244 + 30 + 8, image=face3, tags='hand6')
        else:
            canvas.create_line(668, 317, 793, 228, width=3, fill='black', tags='hand1')
            canvas.create_line(591, 319, 591, 405, width=3, fill='black', tags='hand2')
            canvas.create_image(589 + 41, 244 + 85, image=fire, tags='hand5')
            canvas.create_image(589 + 24 + 12, 244 + 30 + 8, image=face3, tags='hand6')

    if(RadVar.get() == '4'):
        for i in listTags:
            canvas.delete(i)
        labelAnsw["text"] = 'Impact current: ' + str(CorpWith()) + ' mA'
        if(CorpWith() <= 5):
            canvas.create_line(668, 317, 793, 228, width=3, fill='black', tags='hand1')
            canvas.create_line(591, 319, 591, 405, width=3, fill='black', tags='hand3')
            canvas.create_line(870, 260, 870, 510, width=2, fill='black', tags='hand4')
            canvas.create_line(862, 504, 879, 504, width=2, fill='black', tags='hand5')
            canvas.create_line(866, 510, 875, 510, width=2, fill='black', tags='hand6')
            canvas.create_image(589+24+12, 244+30+8, image = face1, tags = 'hand7')
        elif(5 < CorpWith() <= 50):
            canvas.create_line(668, 317, 793, 228, width=3, fill='black', tags='hand1')
            canvas.create_line(591, 319, 591, 405, width=3, fill='black', tags='hand3')
            canvas.create_line(870, 260, 870, 510, width=2, fill='black', tags='hand4')
            canvas.create_line(862, 504, 879, 504, width=2, fill='black', tags='hand5')
            canvas.create_line(866, 510, 875, 510, width=2, fill='black', tags='hand6')
            canvas.create_image(589 + 24 + 12, 244 + 30 + 8, image=face2, tags='hand7')
        elif(50 < CorpWith() <= 90):
            canvas.create_line(668, 317, 793, 228, width=3, fill='black', tags='hand1')
            canvas.create_line(591, 319, 591, 405, width=3, fill='black', tags='hand3')
            canvas.create_line(870, 260, 870, 510, width=2, fill='black', tags='hand4')
            canvas.create_line(862, 504, 879, 504, width=2, fill='black', tags='hand5')
            canvas.create_line(866, 510, 875, 510, width=2, fill='black', tags='hand6')
            canvas.create_image(589 + 41, 244+130, image=heart, tags='hand7')
            canvas.create_image(589 + 24 + 12, 244 + 30 + 8, image=face3, tags='hand8')
        else:
            canvas.create_line(668, 317, 793, 228, width=3, fill='black', tags='hand1')
            canvas.create_line(591, 319, 591, 405, width=3, fill='black', tags='hand3')
            canvas.create_line(870, 260, 870, 510, width=2, fill='black', tags='hand4')
            canvas.create_line(862, 504, 879, 504, width=2, fill='black', tags='hand5')
            canvas.create_line(866, 510, 875, 510, width=2, fill='black', tags='hand6')
            canvas.create_image(589 + 41, 244 + 85, image=fire, tags='hand7')
            canvas.create_image(589 + 24 + 12, 244 + 30 + 8, image=face3, tags='hand8')


def OneHandTouch():
    #print(220000/(int(entryHandRes.get()) + int(entryBodyRes.get())))
    if((int(entryHandRes.get()) + int(entryBodyRes.get()) +
                         int(entryLegsRes.get()) + int(entryR0Res.get()) + int(entryGRNDRes.get())) == 0):
        return float('inf')
    else:
        return round(220000/(int(entryHandRes.get()) + int(entryBodyRes.get()) +
                         int(entryLegsRes.get()) + int(entryR0Res.get()) + int(entryGRNDRes.get())), 4)

def TwoHandTouch():
    if (int(entryHandRes.get()) + int(entryBodyRes.get()) == 0):
        return float('inf')
    else:
        return round(220000/(int(entryHandRes.get()) + int(entryBodyRes.get())), 4)

def CorpWithout():
    if(int(entryHandRes.get()) + int(entryBodyRes.get()) + int(entryLegsRes.get())
                   + int(entryR0Res.get()) + int(entryGRNDRes.get()) == 0):
        return float('inf')
    return round(220000/(int(entryHandRes.get()) + int(entryBodyRes.get()) + int(entryLegsRes.get())
                   + int(entryR0Res.get()) + int(entryGRNDRes.get())), 4)

def CorpWith():
    sum = int(entryHandRes.get()) + int(entryBodyRes.get()) + int(entryLegsRes.get()) + int(entryGRNDRes.get())
    if(int(entryCorpRes.get()) == 0):
        return CorpWithout()
    return round(220000 / (sum + (int(entryCorpRes.get()) + sum)) / int(entryCorpRes.get()), 4)

window = Tk()
window.title('ImpactCurrent')
window.geometry('1200x600')

'''All Images ---->'''
backGroundImg = PhotoImage(file = 'ImpactCurrent_Background.png')
btnStartImg = PhotoImage(file = 'ImpactCurrent_Btn.png')
humanImg = PhotoImage(file = 'ImpactCurrent_Human.png')
btnRecImg = PhotoImage(file = 'ImpactCurrent_Btn2.png')
btnRecImgPos1 = PhotoImage(file = 'ImpactCurrent_Btn2Pos1.png')
face1 = PhotoImage(file = 'ImpactCurrent_Face1.png')
face2 = PhotoImage(file = 'ImpactCurrent_Face2.png')
face3 = PhotoImage(file = 'ImpactCurrent_Face3.png')
fire = PhotoImage(file = 'ImpactCurrent_Fire.png')
heart = PhotoImage(file = 'ImpactCurrent_Heart.png')

canvas = Canvas(window, width=1200, height=600)
canvas.pack(fill = "both", expand = True)

canvas.create_image(0, 0, image = backGroundImg,
                    anchor = "nw")
canvas.create_image(589, 244, image = humanImg,
                    anchor = "nw")
'''<----- All buttons and Labels ----->'''
#88 409
btnMode = ['1', '2', '3', '4']
posRadioBtn = 409
RadVar = StringVar()
RadVar.set('1')
for i in btnMode:
    btnRadio = Radiobutton(text = i, value=i, variable=RadVar, bg='#A5DEED')
    btnRadio.place(x = 88, y =posRadioBtn)
    posRadioBtn += 24

labelBodyRes = Label(text ='BodyRes (Om)')
labelBodyRes.place(x = 750, y = 370)
entryBodyRes = Entry(width = 6)
entryBodyRes.place(x = 710, y = 370)
entryBodyRes.insert(0, 1000)

labelHandRes = Label(text = 'HandRes (Om)')
labelHandRes.place(x = 425, y = 370)
entryHandRes = Entry(width = 6)
entryHandRes.place(x = 510, y = 370)
entryHandRes.insert(0, 1000)

labelLegsRes = Label(text = 'LegsRes (Om)')
labelLegsRes.place(x = 750, y = 470)
entryLegsRes = Entry(width = 6)
entryLegsRes.place(x = 710, y = 470)
entryLegsRes.insert(0, 1000)

labelGRNDRes = Label(text = 'GRNDRes (Om)')
labelGRNDRes.place(x = 425, y = 470)
entryGRNDRes = Entry(width = 6)
entryGRNDRes.place(x = 510, y = 470)
entryGRNDRes.insert(0, 1000)

labelR0Res = Label(text = 'R0 (Om)')
labelR0Res.place(x = 176, y = 241)
entryR0Res = Entry(width = 6)
entryR0Res.place(x = 136, y = 241)
entryR0Res.insert(0, 1000)

labelCorpRes = Label(text = 'Corpus (Om)')
labelCorpRes.place(x = 930, y = 266)
entryCorpRes = Entry(width = 6)
entryCorpRes.place(x = 890, y = 266)
entryCorpRes.insert(0, 1000)

labelAnsw = Label(text = 'Impact current: ')
labelAnsw.place(x = 1020, y = 380)

# 192 435
btnStart = Button(window, image = btnStartImg, command=StartButton)
btnStart.place(x = 192, y = 435)

'''<-----'''

window.mainloop()


