from cmu_graphics import *
###Zombie Slayer Undead Bounty###
#Website name is https://pond-succulent-vise.glitch.me/#
#Also make sure to click on your reward from the cache. You will not get it if yo do not click on it#
#Add any glitches that needs to be fixed below#


#Add any comments below#


#Code Below#
from time import sleep
import random
#app properties
app.background='navy'
app.stepsPerSecond= 5
app.level=0
app.health=100
app.scoped=2
app.Wlevel=0
#person fill changes
skinColors = ['black', 'red', 'blue', 'green', 'purple', 'gold', gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top'), 'hotPink', gradient('black', 'white', 'black', 'white', 'black', 'white', 'black', 'white', start='top')]
#lobby variables
playerSpot = Oval(200, 300, 100, 30, fill=None, border='green', borderWidth=7)
Header = Label('Zombie Slayer', 200, 50, size=30, font='grenze', fill=gradient('black', 'red', start='top'))
Subtitle = Label('Undead Bounty', 200, 80, size=40, font='grenze', fill=gradient('black', 'red', start='top'))
selection = Label('Selected!', 200, 350, size=25, visible=False)
#Variables for Locker
acc = Group(
    Rect(10000, 200, 150, 50, fill=None, border='black', visible=False, align='center'),
    Label('Accessories', 10000, 200, size=25, visible=False)
    )
acc.visible=False
skin = Group(
    Rect(10000, 100, 100, 50, fill=None, border='black', visible=False, align='center'),
    Label('Skins', 10000, 100, size=25, visible=False)
    )
skin.visible=False
wrap = Group(
    Rect(10000, 300, 100, 50, fill=None, border='black', visible=False, align='center'),
    Label('Scopes', 10000, 300, size=25, visible=False)
    )
wrap.visible=False
#Emote Variables
cape = Line(226, 178, 154, 153, fill='red', visible=False)
shot = Oval(256, 113, 5, 10, fill=gradient('black', 'orange', start='bottom-left'), visible=False, rotateAngle=45)
bulletL = Line(283, 55, 285, 50, visible=False)
def Superman():
    gun.visible=False
    person.rotateAngle=90
    cape.visible=True
CancelEmote = Group(
    Rect(50, 90, 50, 25, fill='white', visible=False, align='center'),
    Label('Cancel', 50, 90, visible=False)
    )
CancelEmote.centerX=10000
Emote = Label('Emotes', 10000, 100, size=25, visible=False)
Emote1 = Label('Superman', 10000, 115, size=10, visible=False)
Emote2 = Label('Handstand', 10000, 130, size=10, visible=False)
Emote3 = Label('Shoot', 10000, 160, size=10, visible=False)
Emote4 = Label('Yay!', 10000, 145, size=10)
Emote5 = Label('You suck', 10000, 205, size=10)
Emote6 = Label('Dab', 10000, 175, size=10)
Emote7 = Label('Dance Party', 10000, 190, size=10)
Emotes = Group(Emote1, Emote2, Emote3, Emote4, Emote5, Emote6, Emote7)
dancePerson = Group(
    Line(200, 250, 200, 150, lineWidth=4),
    Line(200, 250, 170, 300, lineWidth=4),
    Line(200, 250, 220, 300, lineWidth=4),
    Line(200, 175, 160, 210, lineWidth=4),
    Line(200, 175, 250, 140, lineWidth=4),
    Circle(200, 150, 20, align='bottom')
    )
dancePerson.centerX=10000
dabPerson = Group(
    Line(200, 250, 200, 150, lineWidth=4),
    Line(200, 250, 170, 300, lineWidth=4),
    Line(200, 250, 220, 300, lineWidth=4),
    Line(200, 160, 225, 140, lineWidth=4),
    Line(200, 175, 250, 140, lineWidth=4),
    Circle(200, 150, 20, align='bottom')
    )
dabPerson.centerX=10000
discoBall = Circle(10000, 100, 15, fill=gradient('blue', 'white', 'purple'))

#Top button variables
lobby = Group(
    Rect(0, 0 , 50, 25, fill=None, border='black'),
    Label('Lobby', 25, 12.5)
    )
lobby.visible=False
locker = Group(
    Rect(50, 0, 50, 25, fill=None, border='black'),
    Label('Locker', 75, 12.5)
    )
locker.visible=False
itemShop = Group(
    Rect(100, 0, 75, 25, fill=None, border='black'),
    Label('Item Shop', 137, 12.5, size=14)
    )
itemShop.visible=False
cache = Group(
    Rect(175, 0, 50, 25, fill=None, border='black'),
    Label('Cache', 200, 12.5, size=14)
    )
cache.visible=False
battlePass = Group(
    Rect(0, 23, 75, 25, fill=None, border='black'),
    Label('Warriors Pass', 37, 35, size=11)
    )
battlePass.bought=False
battlePass.visible=False
obj = Group(
    Rect(75, 23, 60, 25, fill=None, border='black'),
    Label('Objectives', 105, 35, size=11)
    )
obj.visible=False
#Weapons
gun = Group(
    Line(160, 210, 240, 185, lineWidth=15),
    Line(160, 210, 120, 225, lineWidth=5),
    Polygon(235, 180, 255, 160, 270, 200, 240, 195),
    Rect(200, 200, 10, 30)
    )

pick = Group(
    Line(300, 185, 160, 220, fill=gradient('brown', 'chocolate'), lineWidth=7),
    Arc(295, 185, 100, 100, 0, 135, fill=gradient('skyBlue', 'skyBlue', 'blue'))
    )
starWandShop = Group(
    Line(200, 185, 57, 251, fill=gradient('blue', 'purple'), lineWidth=7),
    Star(200, 185, 30, 5, fill=gradient('purple', 'darkOrchid'))
    )
emPick = Group(
    Line(300, 185, 160, 220, fill=gradient('brown', 'chocolate'), lineWidth=7),
    Arc(295, 185, 100, 100, 0, 135, fill=gradient('green', 'lightGreen'))
    )
doublePick1 = Group(
    Line(160, 250, 160, 170, lineWidth=5, fill=gradient('white', 'silver', 'silver'), rotateAngle=340),
    Rect(153, 200, 50, 25, fill=gradient('red', 'darkRed'), align='bottom-right', rotateAngle=335)
    )
doublePick2 = Group(
    Line(240, 145, 248, 240, lineWidth=5, fill=gradient('white', 'silver', 'silver'), rotateAngle=35),
    Rect(260, 185, 50, 25, fill=gradient('red', 'darkRed'), align='bottom-left', rotateAngle=35)
    )
doublePick = Group(doublePick2, doublePick1)
doublePick.centerX=10000
emPick.centerX=10000
emPick.toFront()
starWandShop.centerX=10000
starWandShop.centerY=175
pick.toFront()
gun.toFront()
weaponList = [gun, pick, starWandShop, emPick, doublePick]
pick.centerX=10000
weapon = Group(
    Rect(10000, 100, 100, 50, fill=None, border='black', align='center'),
    Label('Weapons', 10000, 100, size=20)
    )
pickLab = Group(
    Rect(10000, 125, 150, 50, fill=None, border='black', align='center'),
    Label('Diamond Pickaxe', 10000, 125, size=15)
    )
gunLab = Group(
    Rect(10000, 200, 100, 50, fill=None, border='black', align='center'),
    Label('Regular Gun', 10000, 200, size=15)
    )

emPickLab = Group(
    Rect(10000, 125, 150, 50, fill=None, border='black', align='center'),
    Label('Emerald Pickaxe', 10000, 125, size=15)
    )
doublePickLab = Group(
    Rect(10000, 200, 150, 50, fill=None, border='black', align='center'),
    Label('Dual Wield', 10000, 200, size=15)
    )
#Item Shop variables
goldSkin = Group(
    Line(100, 250, 100, 150, lineWidth=4, fill='gold'),
    Line(100, 250, 70, 300, lineWidth=4, fill='gold'),
    Line(100, 250, 120, 300, lineWidth=4, fill='gold'),
    Line(100, 175, 60, 210, lineWidth=4, fill='gold'),
    Line(100, 175, 140, 185, lineWidth=4, fill='gold'),
    Circle(100, 150, 20, align='bottom', fill='gold')
    )
goldSkin.visible=False
goldLab = Label('Gold Skin = 100 S.S', 10000, 325, fill='gold', size=15)
gold = Group(
    Rect(175, 100, 100, 50, fill=None, border='black'),
    Label('Gold', 225, 125, size=25)
    )
gold.visible=False
shopCrosshair = Group(
    Circle(300, 200, 75, fill=None, border='black'),
    Line(300, 275, 300, 127),
    Line(375, 200, 225, 200),
    Circle(300, 200, 5, fill='blue')
    )
shopCrossLab = Label('Blue Dot Scope = 10 S.S', 10000, 325, size=15, visible=False)
shopCrosshair.visible=False
shopCrosshair.bought=False
goldSkin.bought=False
page2 = Group(
    Rect(10000, 75, 35, 35, fill=None, border='black', align='center'),
    RegularPolygon(10000, 75, 15, 3, rotateAngle=90)
    )
page1 = Group(
    Rect(10000, 75, 35, 35, fill=None, border='black', align='center'),
    RegularPolygon(10000, 75, 15, 3, rotateAngle=270)
    )
starWandShop = Group(
    Line(200, 185, 57, 251, fill=gradient('blue', 'purple'), lineWidth=7),
    Star(200, 185, 30, 5, fill=gradient('purple', 'darkOrchid'))
    )
starWandShop.centerX=10000
wandLab = Label('Star Wand = 50 S.S', 10000, 325, size=15)
starWandShop.bought=False
wand = Group(
    Rect(10000, 275, 100, 50, fill=None, border='black', align='center'),
    Label('Star Wand', 10000, 275, size=20)
    )
LLab = Label('L', 200, 175, size=50, fill='green')
LBack = Rect(200, 175, 50, 50, align='center', fill='white')
LSign = Group(
    LLab,
    LBack
    )
LLab.toFront()
ShopL =  Group(
    Line(200, 250, 200, 150, lineWidth=4),
    Line(200, 250, 170, 300, lineWidth=4),
    Line(200, 250, 220, 300, lineWidth=4),
    Line(200, 175, 160, 210, lineWidth=4),
    Line(200, 175, 240, 185, lineWidth=4),
    Circle(200, 150, 20, align='bottom'),
    LSign
    )
ShopL.centerX=300
ShopL.visible=False
Emote5Lab = Label('You Suck Emote = 25 S.S', 10000, 325, size=15)
Emote5.bought=False
#Person fill variables
person = Group(
    Line(200, 250, 200, 150, lineWidth=4),
    Line(200, 250, 170, 300, lineWidth=4),
    Line(200, 250, 220, 300, lineWidth=4),
    Line(200, 175, 160, 210, lineWidth=4),
    Line(200, 175, 240, 185, lineWidth=4),
    Circle(200, 150, 20, align='bottom')
    )
red = Group(
    Label('Red', 10000, 125, size=25),
    Rect(10000, 125, 100, 50, fill=None, border='black', align='center')
    )
blue = Group(
    Label('Blue', 10000, 200, size=25),
    Rect(10000, 200, 100, 50, fill=None, border='black', align='center')
    )
green = Group(
    Label('Green', 10000, 275, size=25),
    Rect(10000, 275, 100, 50, fill=None, border='black', align='center')
    )
Purple = Group(
    Label('Purple', 10000, 350, size=25),
    Rect(10000, 350, 100, 50, fill=None, border='black', align='center')
    )
black = Group(
    Rect(10000, 350, 100, 50, fill=None, border='black', align='center'),
    Label('Black', 10000, 350, size=25)
    )
#Play Variables
UseGun = Line(200, 400, 200, 300, lineWidth=15, fill='grey', arrowEnd=True)
UseGun.visible=False
PlayButton = Rect(350, 250, 90, 50, fill=None, border='black', align='center', visible=False)
Play = Label('Play', 350, 250, size=25, visible=False)
StartButton = Rect(200, 350, 90, 50, fill=None, border='black', align='center')
Start = Label('Start', 200, 350, size=25)
messageDie = Label('You Died', 10000, 200, size=25)
zomb1 = Group(
    Circle(200, 20, 10, fill='green'),
    Line(200, 20, 200, 60, lineWidth=7, fill='green'),
    Line(200, 40, 180, 20, fill='green', lineWidth=5),
    Line(200, 40, 220, 20, fill='green', lineWidth=5),
    Line(200, 55, 180, 80, fill='green', lineWidth=5),
    Line(200, 60, 220, 80, fill='green', lineWidth=5)
    )
zomb2 = Group(
    Circle(35, 35, 10, fill='green'),
    Line(35, 35, 35, 75, lineWidth=7, fill='green'),
    Line(35, 55, 65, 35, fill='green', lineWidth=5),
    Line(35, 55, 15, 35, fill='green', lineWidth=5),
    Line(35, 70, 15, 100, fill='green', lineWidth=5),
    Line(35, 70, 50, 100, fill='green', lineWidth=5)
    )
zomb3 = Group(
    Circle(340, 35, 10, fill='green'),
    Line(340, 35, 340, 75, lineWidth=7, fill='green'),
    Line(340, 55, 375, 35, fill='green', lineWidth=5),
    Line(340, 55, 305, 35, fill='green', lineWidth=5),
    Line(340, 70, 320, 100, fill='green', lineWidth=5),
    Line(340, 70, 360, 100, fill='green', lineWidth=5)
    )
zombies = Group(zomb1, zomb2, zomb3)
easy = Label('Easy', 350, 290, size=15, visible=False)
medium = Label('Medium', 350, 310, size=15, visible=False)
hard = Label('Hard', 350, 330, size=15, visible=False)
impossible = Label('Impossible', 350, 350, size=15, visible=False)
HealthBar = Rect(60, 380, 100, 25, fill=None, border='black', align='center')
Health = Line(12, 380, 108, 380, fill='green', lineWidth=22)
HealthBar.visible=False
Health.visible=False
for zomb in zombies.children:
    zomb.smallW=zomb.width
    zomb.smallH=zomb.height
    zomb.largeW=zomb.width*2
    zomb.largeH=zomb.height*2
    zomb.centerX=10000
weaponSlot1 = Group(
    Rect(350, 350, 50, 50, fill=None, border='black'),
    Line(375, 395, 375, 365, fill='grey', arrowEnd=True)
    )
weaponSlot1.centerX=10000
weaponSlot2 = Group(
    Circle(375, 375, 15, fill='oliveDrab'),
    Rect(350, 350, 50, 50, fill=None, border='black'),
    Line(375, 360, 375, 390),
    Line(363, 367, 387, 367),
    Line(360, 375, 390, 375),
    Line(363, 383, 387, 383),
    Line(375, 360, 375, 355),
    Circle(380, 355, 5, fill=None, border='black')
    )
weaponSlot2.centerX=10000
weaponSlot3 = Group(
    Rect(300, 350, 50, 50, fill=None, border='black', align='top-right'),
    Line(260, 390, 285, 370),
    Arc(285, 370, 20, 20, 315, 180)
    )
weaponSlot3.centerX=10000
grenadeHold = Group(
    Oval(200, 375, 40, 50, fill='oliveDrab'),
    Line(200, 350, 200, 400),
    Line(185, 360, 215, 360),
    Line(180, 375, 220, 375),
    Line(185, 390, 215, 390),
    Line(200, 350, 200, 340),
    Circle(210, 340, 10, fill=None, border='black')
    )
grenadeHold.visible=False
grenadeCount = Label(3, 10000, 390, size=10)
ammoCount = Label(100, 10000, 390, size=10)
ammo = Group(
    Rect(100, 100, 7, 20, fill=rgb(205, 127, 50)),
    Rect(109, 100, 7, 20, fill=rgb(205, 127, 50)),
    Rect(118, 100, 7, 20, fill=rgb(205, 127, 50))
    )
ammo.centerX=10000
medKit = Group(
    Rect(100, 100, 40, 20, fill='red', align='center'),
    Label('+', 100, 102, size=40, fill='white')
    )
medKit.visible=False
zombCount = Label(0, 10000, 10000)
zombSpawn1 = Group(
    Rect(200, 10, 20, 50, fill=gradient('darkOrchid', 'orchid', 'purple')),
    Line(200, 20, 185, 10, fill='purple'),
    Line(220, 45, 230, 35, fill='purple')
    )
zombSpawn1.visible=False
zombSpawn1Bar = Rect(210, 75, 50, 10, fill=None, border='black', align='center')
zombSpawn1health = Line(187, 75, 233, 75, fill='green', lineWidth=8)
zombSpawn1Bar.visible=False
zombSpawn1health.visible=False
winMes = Label('You Won!', 200, 200, visible=False)
onLight = Label('Click here to turn lights on', 10000, 40, size=12, fill='white')
zomb1Eyes = Group(
    Circle(230, 162, 5, fill='yellow'),
    Circle(242, 162, 5, fill='yellow')
    )
zomb2Eyes = Group(
    Circle(200, 200, 5, fill='yellow'),
    Circle(212, 200, 5, fill='yellow')
    )
zomb3Eyes = Group(
    Circle(200, 200, 5, fill='yellow'),
    Circle(212, 200, 5, fill='yellow')
    )
zombieEyes = Group(zomb1Eyes, zomb2Eyes, zomb3Eyes)
zomb2Eyes.visible=False
zomb1Eyes.visible=False
zomb3Eyes.visible=False
selection3 = Label('', 325, 60)
#Currency Variables
currency= Group(
    Label('S.S Moula', 360, 15, size=15, fill='red', bold=True, font='grenze'),
    Rect(400, 0, 140, 35, align='top-right', fill=None, border='black')
    )
icon = Group(
    Circle(315, 15, 8, fill='green'),
    Star(315, 15, 8, 7, fill='silver')
    )
currencyCount = Label(0, 285, 15, size=25, fill='red')
#Username and Level variables
username = Group(
    Rect(75, 175, 100, 25, fill=None, border='black', align='center'),
    Label('Username', 75, 175, size=15)
    )
accLevel = Label(0, 385, 50, size=15, visible=False, fill='white')

#Scope Variables
dotScope = Circle(200, 200, 5, visible=False)
crosshair = Group(
    Line(200, 300, 200, 100),
    Line(100, 200, 300, 200)
    )
crosshair.visible=False
scopeIndex = [dotScope, crosshair]
dotsIndex = ['green', 'red', None, 'blue']
lens = Group(
    Circle(200, 200, 100, fill='white', visible=False, opacity=20),
    dotScope,
    crosshair
    )
scope = Group(
    Circle(200, 200, 600, fill=None, border='black', borderWidth=520, visible=False),
    lens
    )
scope.visible=False
redDotLabel = Group(
    Rect(10000, 100, 100, 50, fill=None, border='black', align='center'),
    Label('Red Dot', 10000, 100, size=20)
    )
greenDotLabel = Group(
    Rect(10000, 300, 100, 50, fill=None, border='black', align='center'),
    Label('Green Dot', 10000, 300, size=20)
    )
CrosshairLabel = Group(
    Rect(10000, 200, 100, 50, fill=None, border='black', align='center'),
    Label('Crosshair', 10000, 200, size=20)
    )
blueCrossLab = Group(
    Rect(10000, 75, 100, 50, fill=None, border='black'),
    Label('Blue Dot', 10000, 100, size=15)
    )
#3rd and 1st person variables
third = Group(
    Rect(10000, 335, 80, 30, fill=None, border='black', align='center'),
    Label('3rd Person', 10000, 335, size=15)
    )
first = Group(
    Rect(10000, 335, 100, 50, fill=None, border='black', align='center'),
    Label('1st Person', 10000, 335, size=15)
    )
#mouse
mouse = Circle(200, 200, 1, visible=False)
#Easter Egg Variables
spot = Circle(300, 300, 1, visible=True)
hint1 = Label('Hint #1: I turn polar bears white, I make you cry, I make you go to the bathroom', 200, 100, size=10, visible=False, fill='white')
hint1con = Label('I make you comb your hair, I make celebrities look stupid, and normal people look like celebrities', 200, 115, size=9, visible=False, fill='white')
hint1Q = Label('What am I?', 200, 130, visible=False, fill='white', size=15)
hint2 = Label('Hint #2: 94% of Harvard students got that riddle wrong but 84% kindergarteners got it right', 200, 150, size=9, fill='white', visible=False)
passEnt = Rect(10000, 200, 100, 25, fill=None, border='black', align='center')
passLab = Label('Click here to enter password', 10000, 175, size=10)
infMoney = Group(
    Rect(10000, 200, 200, 25, fill=None, border='black', align='center'),
    Label('Click here for infinite money!', 10000, 200, size=15, fill='white')
    )
person.moneyGlitch=False
#Cache Variables
cachePlay = RegularPolygon(10000, 250, 100, 4, fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top'))
cacheCount = Label(0, 10000, 115, size=20)
texturedSkin = Group(
    Line(200, 250, 200, 150, lineWidth=4, fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top')),
    Line(200, 250, 170, 300, lineWidth=4, fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top')),
    Line(200, 250, 220, 300, lineWidth=4, fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top')),
    Line(200, 175, 160, 210, lineWidth=4, fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top')),
    Line(200, 175, 240, 185, lineWidth=4, fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top')),
    Circle(200, 150, 20, align='bottom', fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top'))
    )
texturedSkin.centerX=10000
pinkSkin = Group(
    Line(200, 250, 200, 150, lineWidth=4, fill='hotpink'),
    Line(200, 250, 170, 300, lineWidth=4, fill='hotpink'),
    Line(200, 250, 220, 300, lineWidth=4, fill='hotpink'),
    Line(200, 175, 160, 210, lineWidth=4, fill='hotpink'),
    Line(200, 175, 240, 185, lineWidth=4, fill='hotpink'),
    Circle(200, 150, 20, align='bottom', fill='hotpink')
    )
pinkSkin.centerX=10000
emPickCache = Group(
    Line(300, 185, 160, 220, fill=gradient('brown', 'chocolate'), lineWidth=7),
    Arc(295, 185, 100, 100, 0, 135, fill=gradient('green', 'lightGreen'))
    )
doublePickCache = Group(
    Line(160, 250, 160, 170, lineWidth=5, fill=gradient('white', 'silver', 'silver'), rotateAngle=340),
    Rect(153, 200, 50, 25, fill=gradient('red', 'darkRed'), align='bottom-right', rotateAngle=335),
    Line(240, 145, 248, 240, lineWidth=5, fill=gradient('white', 'silver', 'silver'), rotateAngle=35),
    Rect(260, 185, 50, 25, fill=gradient('red', 'darkRed'), align='bottom-left', rotateAngle=35)
    )
CheckeredSkin=Group(
    Line(200, 250, 200, 150, lineWidth=4, fill=gradient('black', 'white', 'black', 'white', 'black', 'white', 'black', 'white', start='top')),
    Line(200, 250, 170, 300, lineWidth=4, fill=gradient('black', 'white', 'black', 'white', 'black', 'white', 'black', 'white', start='top')),
    Line(200, 250, 220, 300, lineWidth=4, fill=gradient('black', 'white', 'black', 'white', 'black', 'white', 'black', 'white', start='top')),
    Line(200, 175, 160, 210, lineWidth=4, fill=gradient('black', 'white', 'black', 'white', 'black', 'white', 'black', 'white', start='top')),
    Line(200, 175, 240, 185, lineWidth=4, fill=gradient('black', 'white', 'black', 'white', 'black', 'white', 'black', 'white', start='top')),
    Circle(200, 150, 20, align='bottom', fill=gradient('black', 'white', 'black', 'white', 'black', 'white', 'black', 'white', start='top'))
    )
CheckeredSkin.centerX=10000
doublePickCache.centerX=10000
emPickCache.centerX=10000
youGotMes = Label('You Got...', 10000, 100, size=20, fill='white')
cacheChoice = [texturedSkin, dabPerson, dancePerson, pinkSkin, emPickCache, doublePickCache, CheckeredSkin]
textSkinLab = Group(
    Rect(10000, 200, 130, 50, fill=None, border='black', align='center'),
    Label('Rainbow Skin', 10000, 200, size=20)
    )
pinkSkinLab = Group(
    Rect(10000, 275, 100, 50, fill=None, border='black', align='center'),
    Label('Pink', 10000, 275, size=20)
    )
checkeredSkinLab = Group(
    Rect(10000, 350, 100, 50, fill=None, border='black', align='center'),
    Label('Checkered', 10000, 350, size=20)
    )
texturedSkin.have=False
dabPerson.have=False
dancePerson.have=False
pinkSkin.have=False
emPick.have=False
doublePick.have=False
CheckeredSkin.have=False
#Battle Pass Variables
battleRewards = Group(
    RegularPolygon(44, 200, 10, 4, fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top')),
    Label(1, 44, 150, size=15),
    RegularPolygon(121, 200, 10, 4, fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top')),
    Label(2, 121, 150, size=15),
    RegularPolygon(200, 200, 10, 4, fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top')),
    Label(3, 200, 150, size=15),
    RegularPolygon(262, 200, 10, 4, fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top')),
    Label(4, 262, 150, size=15),
    RegularPolygon(302, 200, 10, 4, fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top')),
    Label(5, 302, 150, size=15),
    RegularPolygon(340, 200, 10, 4, fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top')),
    Label(6, 340, 150, size=15),
    RegularPolygon(370, 200, 10, 4, fill=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', start='top')),
    Label(7, 370, 150, size=15),
    )
battleRewards.visible=False
levels = Line(10, 200, 400, 200, lineWidth=40, dashes=(68, 10), fill='black', visible=False)
onArrow = Line(25, 230, 25, 260, arrowStart = True, visible=False)
onArrow.centerX=-33
BatpassLab = Group(
    Label('Buy pass', 10000, 300, size=15),
    Rect(10000, 300, 100, 50, fill=None, border='black', align='center')
    )
selection2 = Label('This costs 500 S.S', 200, 350, size=15, visible=False)
#Objective Variables
obj1 = Label('Do the Superman in game', 100, 100, size=15, visible=False)
obj2 = Label('Take the L on a zombie', 100, 150, size=15, visible=False)
obj3 = Label('Get a kill with a grenade', 100, 200, size=15, visible=False)
obj4 = Label('Heal', 100, 250, size=15, visible=False)
obj5 = Label('Win 1 game', 100, 300, size=15, visible=False)
obj1Count = Label(0, 10000, 10000)
obj2Count = Label(0, 10000, 10000)
obj3Count = Label(0, 10000, 10000)
obj4Count = Label(0, 10000, 10000)
obj5Count = Label(0, 10000, 10000)
def objCount():
    if (obj1.fill=='green'):
        onArrow.centerX = onArrow.centerX + 77
        if (onArrow.centerX>260):
            cacheCount.value += 2
        else:
            cacheCount.value+=1
def objCount2():
    if (obj2.fill=='green'):
        onArrow.centerX=onArrow.centerX + 77
        if (onArrow.centerX>260):
            cacheCount.value += 2
        else:
            cacheCount.value+=1
def objCount3():
    if (obj3.fill=='green'):
        onArrow.centerX=onArrow.centerX + 77
        if (onArrow.centerX>260):
            cacheCount.value += 2
        else:
            cacheCount.value+=1
def objCount4():
    if (obj4.fill=='green'):
        onArrow.centerX=onArrow.centerX + 77
        if (onArrow.centerX>260):
            cacheCount.value += 2
        else:
            cacheCount.value+=1
def objCount5():
    if (obj5.fill=='green'):
        onArrow.centerX=onArrow.centerX + 77
        if (onArrow.centerX>260):
            cacheCount.value += 2
        else:
            cacheCount.value+=1
CTC1 = Group(
    Rect(70, 125, 100, 20, align='center', fill=None, border='black'),
    Label('Click here to complete', 70, 125, size=9, bold=True)
    )
CTC1.centerX=10000
CTC2 = Group(
    Rect(70, 125, 100, 20, align='center', fill=None, border='black'),
    Label('Click here to complete', 70, 125, size=9, bold=True)
    )
CTC2.centerX=10000
CTC3 = Group(
    Rect(70, 125, 100, 20, align='center', fill=None, border='black'),
    Label('Click here to complete', 70, 125, size=9, bold=True)
    )
CTC3.centerX=10000
CTC4 = Group(
    Rect(70, 125, 100, 20, align='center', fill=None, border='black'),
    Label('Click here to complete', 70, 125, size=9, bold=True)
    )
CTC4.centerX=10000
CTC5 = Group(
    Rect(70, 125, 100, 20, align='center', fill=None, border='black'),
    Label('Click here to complete', 70, 125, size=9, bold=True)
    )
CTC5.centerX=10000
CTC6 = Group(
    Rect(70, 125, 100, 20, align='center', fill=None, border='black'),
    Label('Click here to complete', 70, 125, size=9, bold=True)
    )
CTC6.centerX=10000
CTC7 = Group(
    Rect(70, 125, 100, 20, align='center', fill=None, border='black'),
    Label('Click here to complete', 70, 125, size=9, bold=True)
    )
CTC7.centerX=10000
CTC8 = Group(
    Rect(70, 125, 100, 20, align='center', fill=None, border='black'),
    Label('Click here to complete', 70, 125, size=9, bold=True)
    )
CTC8.centerX=10000
CTC9 = Group(
    Rect(70, 125, 100, 20, align='center', fill=None, border='black'),
    Label('Click here to complete', 70, 125, size=9, bold=True)
    )
CTC9.centerX=10000
CTC10 = Group(
    Rect(70, 125, 100, 20, align='center', fill=None, border='black'),
    Label('Click here to complete', 70, 125, size=9, bold=True)
    )
CTC10.centerX=10000
background = Rect(0, 0, 400, 400, fill='orange')
background.visible=False
texturedSkin.removed=False
texturedSkin.removed=False
dabPerson.removed=False
dancePerson.removed=False
pinkSkin.removed=False
emPick.removed=False
doublePick.removed=False
CheckeredSkin.removed=False
#Mouse Press Events
def onMousePress(mouseX, mouseY):
    if (Start.hits(mouseX, mouseY)):
        lobby.visible=True
        username.centerX=10000
        Start.centerX=10000
        StartButton.visible=False
    #Scope Mouse Events
    dotScope.fill = dotsIndex[app.scoped]
    if (wrap.hits(mouseX, mouseY)):
        redDotLabel.centerX=100
        greenDotLabel.centerX=100
        CrosshairLabel.centerX=100
        skin.centerX=10000
        wrap.centerX=10000
        gold.centerX=10000
        weapon.centerX=10000
        if (shopCrosshair.bought==True):
            blueCrossLab.centerX=225
            blueCrossLab.visible=True
    if (selection.value=='Purchased'):
        shopCrossLab.fill='green'
        selection.value='You already own this'
        accLevel.value+=1
    elif (redDotLabel.hits(mouseX, mouseY)):
        app.scoped=1
    elif (greenDotLabel.hits(mouseX, mouseY)):
        app.scoped=0
    elif (CrosshairLabel.hits(mouseX, mouseY)):
        app.scoped=2
    elif (blueCrossLab.hits(mouseX, mouseY)):
        app.scoped=3
    #Emote Mouse events
    if (person.hits(mouseX, mouseY)):
        if (app.background != 'black'):
            Emote.centerX=325
            Emote.visible=True
            Emote.toFront()
    if (Emote.hits(mouseX, mouseY)):
        gold.centerX=10000
        Emote1.centerX=325
        Emote2.centerX=325
        Emote3.centerX=325
        Emote4.centerX=325
        Emote1.visible=True
        Emote2.visible=True
        Emote3.visible=True
        if (dancePerson.have==True):
            Emote7.centerX=325
        if (dabPerson.have==True):
            Emote6.centerX=325
        if (Emote5.bought==True):
            Emote5.visible=True
            Emote5.centerX=325
            Emote5.centerY=160
            Emote3.centerY=205
        if ((app.background=='white') or (app.background=='black')):
            Emote3.centerX=10000
        if (app.Wlevel>0):
            Emote3.centerX=10000
    if (selection.value=='Purchased!'):
        Emote5Lab.fill='green'
        selection.value='You already own that'
        accLevel.value+=1
    if (Emote1.hits(mouseX, mouseY)):
        Superman()
        person.centerX=playerSpot.centerX
        CancelEmote.centerX=50
        weaponList[app.Wlevel].visible=False
        cape.centerX=person.centerX - 10
        cape.centerY=person.centerY - 10
    elif (Emote2.hits(mouseX, mouseY)):
        CancelEmote.centerX=50
        weaponList[app.Wlevel].visible=False
        cape.visible=False
        person.rotateAngle=180
    elif (Emote3.hits(mouseX, mouseY)):
        gun.rotateAngle=135
        shot.visible=True
        bulletL.visible=True
        CancelEmote.centerX=50
    elif (Emote4.hits(mouseX, mouseY)):
        CancelEmote.centerX=50
        weaponList[app.Wlevel].visible=False
        person.centerY=person.centerY - 50
        sleep(0.5)
        person.centerY=person.centerY + 50
        sleep(0.5)
        person.centerY=person.centerY - 50
        sleep(0.5)
        person.centerY=person.centerY + 50
    elif (Emote5.hits(mouseX, mouseY)):
        if (app.background=='white'):
            LLab.size=20
            LBack.width=20
            LBack.height=20
            LBack.centerX=LLab.centerX
            LBack.centerY=LLab.centerY
            LSign.centerX=person.centerX
            LSign.centerY=person.top
        if (app.background=='navy'):
            LLab.size=40
            LBack.width=40
            LBack.height=40
            LBack.centerX=LLab.centerX
            LBack.centerY=LLab.centerY
            LSign.centerX=person.centerX
            LSign.centerY=person.top
        CancelEmote.centerX=50
        LSign.visible=True
        LSign.centerX=person.centerX
        weaponList[app.Wlevel].visible=False
        person.rotateAngle=45
        sleep(0.5)
        person.rotateAngle=315
        sleep(0.5)
        person.rotateAngle=45
        sleep(0.5)
        person.rotateAngle=315
    elif (Emote6.hits(mouseX, mouseY)):
        person.centerX=10000
        dabPerson.centerX=200
        dancePerson.centerX=10000
        dabPerson.fill=skinColors[app.level]
        CancelEmote.centerX=50
        weaponList[app.Wlevel].visible=False
        if (app.background=='white'):
            dabPerson.width=40
            dabPerson.height=80
            dabPerson.centerY=350
    elif (Emote7.hits(mouseX, mouseY)):
        dancePerson.centerX=200
        dancePerson.fill=skinColors[app.level]
        CancelEmote.centerX=50
        dabPerson.centerX=10000
        person.centerX=10000
        weaponList[app.Wlevel].visible=False
        discoBall.centerX=dancePerson.centerX
        discoBall.centerY=dancePerson.top - 20
        discoBall.visible=True
        if (app.background=='white'):
            dancePerson.width=40
            dancePerson.height=80
            dancePerson.centerY=350
            discoBall.centerX=dancePerson.centerX
            discoBall.centerY=dancePerson.top - 20
            discoBall.visible=True
            discoBall.radius=10
    #Username Mouse Events
    if (username.hits(mouseX, mouseY)):
        response=app.getTextInput('Create your Username!')
        label = Label(response, 325, 50, size=15, fill='white')
        accLevel.visible=True
        accLevel.centerX=label.centerX + 60
    #Locker Mouse Events
    if (locker.hits(mouseX, mouseY)):
        Header.value='Locker'
        Subtitle.visible=False
        gun.centerX=10000
        playerSpot.visible=False
        acc.visible=True
        acc.centerX=200
        person.centerX=10000
        selection.visible=False
        pick.centerX=10000
        PlayButton.centerX=10000
        Play.centerX=10000
        easy.centerX=10000
        medium.centerX=10000
        hard.centerX=10000
        impossible.centerX=10000
        username.centerX=10000
        redDotLabel.centerX=10000
        greenDotLabel.centerX=10000
        CrosshairLabel.centerX=10000
        blueCrossLab.centerX=10000
        goldSkin.visible=False
        goldLab.centerX=10000
        shopCrosshair.visible=False
        shopCrossLab.centerX=10000
        third.centerX=10000
        first.centerX=10000
        selection.centerX=10000
        page2.centerX=10000
        page1.centerX=10000
        weapon.centerX=10000
        pickLab.centerX=10000
        gunLab.centerX=10000
        starWandShop.centerX=10000
        starWandShop.visible=False
        wandLab.centerX=10000
        wand.centerX=10000
        weaponList[app.Wlevel].visible=False
        ShopL.visible=False
        Emote5Lab.centerX=10000
        cachePlay.centerX=10000
        cacheCount.centerX=10000
        youGotMes.centerX=10000
        texturedSkin.centerX=10000
        emPick.centerX=10000
        doublePick.centerX=10000
        pinkSkin.centerX=10000
        CheckeredSkin.centerX=10000
        dabPerson.centerX=10000
        dancePerson.centerX=10000
        red.centerX=10000
        blue.centerX=10000
        green.centerX=10000
        Purple.centerX=10000
        black.centerX=10000
        textSkinLab.centerX=10000
        pinkSkinLab.centerX=10000
        checkeredSkinLab.centerX=10000
        gold.centerX=10000
        Emote.centerX=10000
        Emote1.centerX=10000
        Emote2.centerX=10000
        Emote3.centerX=10000
        Emote4.centerX=10000
        Emote5.centerX=10000
        Emote6.centerX=10000
        Emote7.centerX=10000
        emPickLab.centerX=10000
        doublePickLab.centerX=10000
        emPickCache.centerX=10000
        doublePickCache.centerX=10000
        doublePick.centerX=10000
        levels.visible=False
        onArrow.visible=False
        battleRewards.visible=False
        BatpassLab.centerX=10000
        selection2.visible=False
        obj1.visible=False
        obj2.visible=False
        obj3.visible=False
        obj4.visible=False
        obj5.visible=False
    elif (acc.hits(mouseX, mouseY)):
        acc.centerX=10000
        skin.visible=True
        skin.centerX=100
        wrap.visible=True
        wrap.centerX=100
        weapon.centerX=100
        weapon.centerY=200

    if (selection.value=='purchased'):
        goldLab.fill='green'
        selection.value='You already own that'
        accLevel.value+=1

    elif (weapon.hits(mouseX, mouseY)):
        weapon.centerX=10000
        skin.centerX=10000
        wrap.centerX=10000
        pickLab.centerX=100
        gunLab.centerX=100
        selection.centerX=10000
        if (emPick.have==True):
            emPickLab.centerX=275
        if (doublePick.have==True):
            doublePickLab.centerX=275
        if (starWandShop.bought==True):
            wand.centerX=100
            wand.visible=True
    if (selection.value=='purchased!'):
        wandLab.fill='green'
        selection.value='You already own this'
        accLevel.value+=1
    #Weapon Change Properties
    if (pickLab.hits(mouseX, mouseY)):
        app.Wlevel=1
    elif (gunLab.hits(mouseX, mouseY)):
        app.Wlevel=0
    elif (wand.hits(mouseX, mouseY)):
        app.Wlevel=2
    elif (emPickLab.hits(mouseX, mouseY)):
        app.Wlevel=3
    elif (doublePickLab.hits(mouseX, mouseY)):
        app.Wlevel=4
    #Person fill events
    if (black.hits(mouseX, mouseY)):
        app.level=0

    elif (red.hits(mouseX, mouseY)):
        app.level=1
    elif (blue.hits(mouseX, mouseY)):
        app.level=2
    elif (green.hits(mouseX, mouseY)):
        app.level=3
    elif (Purple.hits(mouseX, mouseY)):
        app.level=4
    elif (gold.hits(mouseX, mouseY)):
        app.level=5
    elif (textSkinLab.hits(mouseX, mouseY)):
        app.level=6
    elif (pinkSkinLab.hits(mouseX, mouseY)):
        app.level=7
    elif (checkeredSkinLab.hits(mouseX, mouseY)):
        app.level=8

    #Lobby Events
    if (lobby.hits(mouseX, mouseY)):
        app.health=100
        ammo.visible=False
        app.background='navy'
        starWandShop.visible=False
        UseGun.visible=False
        Health.visible=False
        HealthBar.visible=False
        zomb1.visible=False
        zomb2.visible=False
        zomb3.visible=False
        Header.centerX=200
        Header.value='Zombie Slayer'
        Header.visible=True
        Subtitle.visible=True
        Subtitle.value='Undead Bounty'
        playerSpot.visible=True
        acc.visible=False
        skin.visible=False
        person.centerX=200
        selection.visible=False
        person.fill= skinColors[app.level]
        weaponList[app.Wlevel].centerX=195
        weaponList[app.Wlevel].centerY=195
        weaponList[app.Wlevel].visible=True
        weaponList[app.Wlevel].toFront()
        if (app.Wlevel>0):
            if (weaponList[app.Wlevel].width<100):
                weaponList[app.Wlevel].width*=2
                weaponList[app.Wlevel].height*=2
        if (app.Wlevel==1):
            pick.centerX=pick.centerX + 20
            pick.centerY=pick.centerY - 20
            pick.width=160
            pick.height=80
        elif (app.Wlevel==3):
            emPick.centerX=emPick.centerX + 20
            emPick.centerY=emPick.centerY - 20
            emPick.width=160
            emPick.height=80
        elif (app.Wlevel==4):
            doublePick.centerX=doublePick.centerX + 7
            doublePick.width=175
            doublePick.height=110
        elif (app.Wlevel==2):
            starWandShop.centerX=starWandShop.centerX + 20
            starWandShop.centerY=starWandShop.centerY - 20
            starWandShop.width=160
            starWandShop.height=80
        elif (app.Wlevel==0):
            pick.centerX=10000
            doublePick.centerX=10000
            starWandShop.centerX=10000
            emPick.centerX=10000
        red.centerX=10000
        blue.centerX=10000
        green.centerX=10000
        Purple.centerX=10000
        black.centerX=10000
        PlayButton.centerX=350
        Play.centerX=350
        messageDie.centerX=10000
        easy.centerX=350
        medium.centerX=350
        hard.centerX=350
        impossible.centerX=350
        goldLab.centerX=10000
        redDotLabel.centerX=10000
        greenDotLabel.centerX=10000
        CrosshairLabel.centerX=10000
        PlayButton.centerX=Play.centerX
        itemShop.visible=True
        battlePass.visible=True
        obj.visible=True
        locker.visible=True
        cache.visible=True
        PlayButton.visible=True
        easy.visible=True
        medium.visible=True
        hard.visible=True
        impossible.visible=True
        wrap.centerX=10000
        goldSkin.visible=False
        goldLab.centerX=10000
        shopCrosshair.visible=False
        shopCrossLab.centerX=10000
        blueCrossLab.centerX=10000
        gold.centerX=10000
        first.centerX=10000
        third.centerX=10000
        person.width=80
        person.height=200
        person.centerY=205
        person.visible=True
        selection.centerX=10000
        locker.centerX=75
        itemShop.centerX=137
        Play.visible=True
        icon.visible=True
        currency.visible=True
        currencyCount.visible=True
        hint1.visible=False
        hint1con.visible=False
        hint1Q.visible=False
        hint2.visible=False
        passEnt.centerX=10000
        BatpassLab.centerX=10000
        passLab.centerX=10000
        infMoney.centerX=10000
        page2.centerX=10000
        page1.centerX=10000
        weapon.centerX=10000
        pickLab.centerX=10000
        gunLab.centerX=10000
        wandLab.centerX=10000
        wand.centerX=10000
        ShopL.visible=False
        Emote5Lab.centerX=10000
        cachePlay.centerX=10000
        cacheCount.centerX=10000
        youGotMes.centerX=10000
        texturedSkin.centerX=10000
        emPickLab.centerX=10000
        doublePickLab.centerX=10000
        pinkSkin.centerX=10000
        CheckeredSkin.centerX=10000
        dabPerson.centerX=10000
        textSkinLab.centerX=10000
        pinkSkinLab.centerX=10000
        checkeredSkinLab.centerX=10000
        dancePerson.centerX=10000
        UseGun.lineWidth=20
        UseGun.x1=200
        UseGun.y1=400
        UseGun.x2=200
        UseGun.y2=300
        emPickCache.centerX=10000
        doublePickCache.centerX=10000
        battlePass.centerX=37
        obj.centerX=105
        cache.centerX=200
        levels.visible=False
        onArrow.visible=False
        battleRewards.visible=False
        BatpassLab.centerX=10000
        selection2.visible=False
        obj1.visible=False
        obj2.visible=False
        obj3.visible=False
        weaponSlot1.centerX=10000
        weaponSlot2.centerX=10000
        grenadeCount.centerX=10000
        ammo.visible=False
        ammoCount.centerX=10000
        ammoCount.value=100
        grenadeCount.value=3
        grenadeHold.visible=False
        medKit.visible=False
        obj4.visible=False
        zombSpawn1.visible=False
        zombSpawn1Bar.visible=False
        zombSpawn1health.visible=False
        zombSpawn1health.x2=233
        winMes.visible=False
        obj5.visible=False
        weaponSlot3.centerX=10000
        zombCount.value=0
        for zombEye in zombieEyes.children:
            zombEye.visible=False
    #Gamemode events
    elif (easy.hits(mouseX, mouseY)):
        app.stepsPerSecond=1
    elif (medium.hits(mouseX, mouseY)):
        app.stepsPerSecond=5
    elif (hard.hits(mouseX, mouseY)):
        app.stepsPerSecond=10
    elif (impossible.hits(mouseX, mouseY)):
        app.stepsPerSecond=20
    #Play Events
    elif (PlayButton.hits(mouseX, mouseY)):
        lobby.centerX=10000
        battlePass.centerX=10000
        itemShop.centerX=10000
        cache.centerX=10000
        locker.centerX=10000
        obj.centerX=10000
        person.centerX=10000
        gun.visible=False
        weaponList[app.Wlevel].visible=False
        playerSpot.visible=False
        Header.visible=False
        Subtitle.visible=False
        PlayButton.centerX=10000
        Play.centerX=10000
        pick.centerX=10000
        Emote.centerX=10000
        Emote1.centerX=10000
        Emote2.centerX=10000
        Emote3.centerX=10000
        Emote4.centerX=10000
        Emote5.centerX=10000
        Emote6.centerX=10000
        Emote7.centerX=10000
        CancelEmote.centerX=10000
        app.background='green'
        username.centerX=10000
        tip1='1. Hit the zombies in its weakpoints, not all clicks do damage'
        tip1call = Label(tip1, 200, 100, size=14)
        tip2 = '2. Every zombie kill you get, you get 1 S.S'
        tip2call=Label(tip2, 150, 200, size=14)
        tip3 = '3. Use the money to go buy skins from the item shop!'
        tip3call = Label(tip3, 175, 300, size=14)
        l = 'Loading...'
        load = Label(l, 40, 390, size=15)
        easy.centerX=10000
        medium.centerX=10000
        hard.centerX=10000
        impossible.centerX=10000
        sleep(3)
        tip3call.visible=False
        tip2call.visible=False
        tip1call.visible=False
        load.value=''
        app.background='white'
        UseGun.visible=True
        HealthBar.visible=True
        Health.visible=True
        zomb1.centerX=200
        zomb1.visible=True
        zomb2.visible=True
        zomb3.visible=True
        username.centerX=10000
        third.centerX=60
        first.centerX=10000
        gold.centerX=10000
        weaponSlot1.centerX=325
        weaponSlot2.centerX=375
        weaponSlot3.centerX=275
        grenadeCount.centerX=390
        ammoCount.centerX=335
        zombSpawn1.visible=True
        zombSpawn1Bar.visible=True
        zombSpawn1health.visible=True
    if (zomb1.hits(mouseX, mouseY)):
        if (ammoCount.value>0):
            if (UseGun.visible==True):
                zomb1.centerY=25
                currencyCount.value += 1
                zombCount.value += 1
                ammo.centerX=zomb1.centerX
    if (zomb2.hits(mouseX, mouseY)):
        if (ammoCount.value>0):
            if (UseGun.visible==True):
                zomb2.centerY=25
                zomb2.centerX=15
                zombCount.value +=1
                currencyCount.value += 1
                ammo.centerX=zomb2.centerX
        if (weaponList[app.Wlevel].visible==True):
            if (zomb1.centerY>=person.centerY - 50):
                zomb1.centerY=25
                zombCount.value +=1
                currencyCount.value += 1
                ammo.centerX=zomb1.centerX
        if (weaponList[app.Wlevel].visible==True):
            if (zomb2.centerY>=person.centerY - 50):
                zomb2.centerY=25
                zomb2.centerX=15
                zombCount.value +=1
                currencyCount.value += 1
                ammo.centerX=zomb2.centerX
    if (zomb3.hits(mouseX, mouseY)):
        if (ammoCount.value>0):
            if (UseGun.visible==True):
                zomb3.centerX=340
                zomb3.centerY=25
                zombCount.value +=1
                currencyCount.value += 1
                ammo.centerX=zomb3.centerX
        if (weaponList[app.Wlevel].visible==True):
            if (zomb3.centerY>=person.centerY - 50):
                zomb3.centerY=25
                zomb3.centerX=340
                zombCount.value +=1
                currencyCount.value += 1
                ammo.centerX=zomb3.centerX
    if (app.health==100):
        Health.x2=108
    #Item Shop Events
    if (itemShop.hits(mouseX, mouseY)):
        Header.value='Item'
        Subtitle.value='Shop'
        Subtitle.visible=True
        gun.centerX=10000
        playerSpot.visible=False
        acc.centerX=10000
        acc.visible=False
        person.centerX=10000
        selection.visible=False
        pick.centerX=10000
        PlayButton.centerX=10000
        Play.centerX=10000
        easy.centerX=10000
        medium.centerX=10000
        hard.centerX=10000
        impossible.centerX=10000
        username.centerX=10000
        goldSkin.visible=True
        goldLab.centerX=100
        redDotLabel.centerX=10000
        greenDotLabel.centerX=10000
        CrosshairLabel.centerX=10000
        skin.centerX=10000
        wrap.centerX=10000
        shopCrosshair.visible=True
        shopCrossLab.centerX=300
        shopCrossLab.visible=True
        blueCrossLab.centerX=10000
        third.centerX=10000
        first.centerX=10000
        selection.centerX=100
        if (goldLab.fill=='green'):
            selection.centerX=100
            selection.visible=True
            selection.value='You already have this'
        page2.centerX=335
        page1.centerX=295
        weapon.centerX=10000
        pickLab.centerX=10000
        gunLab.centerX=10000
        starWandShop.centerX=10000
        wandLab.centerX=10000
        wand.centerX=10000
        weaponList[app.Wlevel].visible=False
        black.centerX=10000
        ShopL.visible=False
        Emote5Lab.centerX=10000
        cachePlay.centerX=10000
        cacheCount.centerX=10000
        youGotMes.centerX=10000
        texturedSkin.centerX=10000
        pinkSkin.centerX=10000
        CheckeredSkin.centerX=10000
        dabPerson.centerX=10000
        emPick.centerX=10000
        doublePick.centerX=10000
        textSkinLab.centerX=10000
        pinkSkinLab.centerX=10000
        checkeredSkinLab.centerX=10000
        dancePerson.centerX=10000
        red.centerX=10000
        blue.centerX=10000
        green.centerX=10000
        Purple.centerX=10000
        black.centerX=10000
        gold.centerX=10000
        Emote.centerX=10000
        Emotes.centerX=10000
        emPickLab.centerX=10000
        doublePickLab.centerX=10000
        emPickCache.centerX=10000
        doublePickCache.centerX=10000
        doublePick.centerX=10000
        levels.visible=False
        onArrow.visible=False
        battleRewards.visible=False
        BatpassLab.centerX=10000
        selection2.visible=False
        obj1.visible=False
        obj2.visible=False
        obj3.visible=False
        obj4.visible=False
        obj5.visible=False
    if (goldLab.hits(mouseX, mouseY)):
        if (currencyCount.value>=100):
            selection.visible=True
            selection.size=15
            goldSkin.bought=True
            selection.centerX=100
            if (goldLab.fill != 'green'):
                currencyCount.value-=100
                selection.value='purchased'
        elif (currencyCount.value<100):
            selection.value='You do not have enough S.S to purchase this'
            selection.centerX=200
            selection.size=15
            selection.visible=True
            goldSkin.bought=False
    if (page2.hits(mouseX, mouseY)):
        goldSkin.visible=False
        goldLab.centerX=10000
        shopCrosshair.visible=False
        shopCrossLab.centerX=10000
        starWandShop.centerX=100
        starWandShop.visible=True
        wandLab.centerX=100
        ShopL.visible=True
        Emote5Lab.centerX=300
        page2.centerX=10000
    if (Emote5Lab.hits(mouseX, mouseY)):
        if (currencyCount.value>=25):
            selection.visible=True
            selection.size=15
            selection.centerX=300
            Emote5.bought=True
            if (Emote5Lab.fill != 'green'):
                currencyCount.value -= 25
                selection.value='Purchased!'
        elif (currencyCount.value < 25):
            selection.value='You do not have enough S.S to purchase this'
            selection.centerX=200
            selection.size=15
            selection.visible=True
            Emote5.bought=False
    if (wandLab.hits(mouseX, mouseY)):
        if (currencyCount.value>=50):
            selection.visible=True
            selection.size=15
            selection.centerX=100
            starWandShop.bought=True
            if (wandLab.fill != 'green'):
                currencyCount.value -= 50
                selection.value='purchased!'
        elif (currencyCount.value<50):
            selection.value='You do not have enough S.S to purchase this'
            selection.centerX=200
            selection.size=15
            selection.visible=True
            starWandShop.bought=False

    elif (page1.hits(mouseX, mouseY)):
        goldSkin.visible=True
        goldLab.centerX=100
        shopCrosshair.visible=True
        shopCrossLab.centerX=300
        starWandShop.centerX=10000
        wandLab.centerX=10000
        ShopL.visible=False
        page2.centerX=335
        Emote5Lab.centerX=10000

    #Crosshair bought events
    if (shopCrossLab.hits(mouseX, mouseY)):
        if (currencyCount.value>=10):
            selection.visible=True
            shopCrosshair.bought=True
            selection.size=15
            selection.centerX=300
            if (shopCrossLab.fill != 'green'):
                currencyCount.value-=10
                selection.value='Purchased'
        elif (currencyCount.value<10):
            selection.visible=True
            selection.size=15
            selection.value='You do not have enough S.S to purchase this'
            selection.centerX=200
            shopCrosshair.bought=False
    #First and third person events
    if (third.hits(mouseX, mouseY)):
        person.visible=True
        person.centerX=200
        person.centerY=350
        person.width=40
        person.height=80
        person.fill=skinColors[app.level]
        UseGun.lineWidth=5
        #UseGun.height=50
        UseGun.y1=333
        UseGun.x1=200
        UseGun.x2=180
        UseGun.y2=305
        third.centerX=10000
        first.centerX=60
        if (Health.x2 <= 12):
            app.health=0
        if (grenadeHold.visible==True):
            weaponList[app.Wlevel].visible=False
            grenadeHold.centerX=person.centerX + 20
            grenadeHold.centerY=person.centerY - 10
            grenadeHold.width=20
            grenadeHold.height=20
        if (weaponList[app.Wlevel].visible==True):
            if (app.Wlevel==1):
                weaponList[app.Wlevel].centerX=person.centerX - 20
                weaponList[app.Wlevel].centerY=person.centerY - 15
                weaponList[app.Wlevel].width =  weaponList[app.Wlevel].width=92
                weaponList[app.Wlevel].height =  weaponList[app.Wlevel].height=44
            elif (app.Wlevel==2):
                weaponList[app.Wlevel].centerX=person.centerX - 15
                weaponList[app.Wlevel].centerY=person.centerY - 5
                weaponList[app.Wlevel].width =  weaponList[app.Wlevel].width=92
                weaponList[app.Wlevel].height =  weaponList[app.Wlevel].height=44
            elif (app.Wlevel==3):
                weaponList[app.Wlevel].centerX=person.centerX - 20
                weaponList[app.Wlevel].centerY=person.centerY - 15
                weaponList[app.Wlevel].width =  weaponList[app.Wlevel].width=92
                weaponList[app.Wlevel].height =  weaponList[app.Wlevel].height=44
            elif (app.Wlevel==4):
                weaponList[app.Wlevel].centerX=person.centerX
                weaponList[app.Wlevel].centerY=person.centerY - 15
                weaponList[app.Wlevel].width =  weaponList[app.Wlevel].width=92
                weaponList[app.Wlevel].height =  weaponList[app.Wlevel].height=44
            if (UseGun.visible==True):
                weaponList[app.Wlevel].visible=False
    elif (first.hits(mouseX, mouseY)):
        person.visible=False
        UseGun.lineWidth=20
        UseGun.x1=200
        UseGun.y1=400
        UseGun.x2=200
        UseGun.y2=300
        third.centerX=60
        first.centerX=10000
        if (Health.x2 <= 12):
            app.health=0
        if (grenadeHold.visible==True):
            grenadeHold.centerX=200
            grenadeHold.centerY=375
            grenadeHold.width=50
            grenadeHold.height=50
        if (weaponList[app.Wlevel].visible==True):
            weaponList[app.Wlevel].centerX=200
            weaponList[app.Wlevel].centerY=350
            weaponList[app.Wlevel].width=160
            weaponList[app.Wlevel].height=80
        else:
            weaponList[app.Wlevel].centerX=10000
    #Easter Egg events        
    if (mouse.hitsShape(spot)):
        if (Header.value=='Zombie Slayer'):
            app.background='blue'
            person.centerX=10000
            gun.visible=False
            pick.visible=False
            playerSpot.visible=False
            username.centerX=10000
            locker.centerX=10000
            battlePass.centerX=10000
            cache.centerX=10000
            itemShop.centerX=10000
            currency.visible=False
            currencyCount.visible=False
            icon.visible=False
            Header.value='Enter the Password'
            Subtitle.visible=False
            Play.visible=False
            PlayButton.centerX=10000
            easy.centerX=10000
            medium.centerX=10000
            hard.centerX=10000
            impossible.centerX=10000
            hint1.visible=True
            hint1con.visible=True
            hint2.visible=True
            hint1Q.visible=True
            passEnt.centerX=200
            passLab.centerX=200
            infMoney.centerX=10000
            acc.centerX=10000
            cache.centerX=10000
            obj.centerX=10000
    if (passLab.hits(mouseX, mouseY)):
        message = app.getTextInput('Enter the Passcode!')
        mesLab = Label(message, 200, 200, size=15)
        if (mesLab.value=='Nothing'):
            hint1.visible=False
            hint1con.visible=False
            hint2.visible=False
            hint1Q.visible=False
            passEnt.centerX=10000
            passLab.centerX=10000
            app.background=gradient('red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', start='left')
            mesLab.visible=False
            infMoney.centerX=200
            Header.value='You Got It Right!'
        else:
            app.background='red'
            hint1.visible=False
            hint1con.visible=False
            hint2.visible=False
            hint1Q.visible=False
            passEnt.centerX=10000
            passLab.centerX=10000
            mesLab.visible=False
            infMoney.centerX=10000
            Header.visible=False
    if (infMoney.hits(mouseX, mouseY)):
        person.moneyGlitch=True
    #Cache Events
    if (cache.hits(mouseX, mouseY)):
        Header.value='Caches'
        Subtitle.visible=False
        gun.centerX=10000
        playerSpot.visible=False
        acc.visible=True
        acc.centerX=10000
        person.centerX=10000
        selection.visible=False
        pick.centerX=10000
        PlayButton.centerX=10000
        Play.centerX=10000
        easy.centerX=10000
        medium.centerX=10000
        hard.centerX=10000
        impossible.centerX=10000
        username.centerX=10000
        redDotLabel.centerX=10000
        greenDotLabel.centerX=10000
        CrosshairLabel.centerX=10000
        blueCrossLab.centerX=10000
        goldSkin.visible=False
        goldLab.centerX=10000
        shopCrosshair.visible=False
        shopCrossLab.centerX=10000
        gold.centerX=10000
        third.centerX=10000
        first.centerX=10000
        selection.centerX=10000
        page2.centerX=10000
        page1.centerX=10000
        weapon.centerX=10000
        pickLab.centerX=10000
        gunLab.centerX=10000
        starWandShop.centerX=10000
        starWandShop.visible=False
        wandLab.centerX=10000
        wand.centerX=10000
        weaponList[app.Wlevel].visible=False
        black.centerX=10000
        ShopL.visible=False
        Emote5Lab.centerX=10000
        CancelEmote.centerX=10000
        cachePlay.centerX=200
        cacheCount.centerX=200
        cacheCount.visible=True
        youGotMes.centerX=10000
        dancePerson.centerX=10000
        red.centerX=10000
        blue.centerX=10000
        green.centerX=10000
        Purple.centerX=10000
        black.centerX=10000
        textSkinLab.centerX=10000
        pinkSkinLab.centerX=10000
        checkeredSkinLab.centerX=10000
        gold.centerX=10000
        Emote.centerX=10000
        Emotes.centerX=10000
        emPickLab.centerX=10000
        doublePickLab.centerX=10000
        doublePick.centerX=10000
        levels.visible=False
        onArrow.visible=False
        battleRewards.visible=False
        BatpassLab.centerX=10000
        selection2.visible=False
        obj1.visible=False
        obj2.visible=False
        obj3.visible=False
        obj4.visible=False
        obj5.visible=False
    elif (cachePlay.hits(mouseX, mouseY)):
        if (cacheCount.value > 0):
            cacheCount.visible=True
            cachePlay.centerX=10000
            choices = choice(cacheChoice).centerX=200
            youGotMes.centerX=200
            cacheCount.value -= 1
        elif (cacheCount.value<=0):
            cacheCount.visible=True
            cachePlay.centerX=200
            youGotMes.centerX=10000
    if (texturedSkin.hits(mouseX, mouseY)):
        texturedSkin.have=True
        if (texturedSkin.removed==False):
            cacheChoice.remove(texturedSkin)
            texturedSkin.removed=True
    elif (emPickCache.hits(mouseX, mouseY)):
        emPick.have=True
        if (emPick.removed==False):
            emPick.removed=True
            cacheChoice.remove(emPickCache)
    elif (doublePickCache.hits(mouseX, mouseY)):
        doublePick.have=True
        if (doublePick.removed==False):
            doublePick.removed=True
            cacheChoice.remove(doublePickCache)
    elif (pinkSkin.hits(mouseX, mouseY)):
        pinkSkin.have=True
        if (pinkSkin.removed==False):
            pinkSkin.removed=True
            cacheChoice.remove(pinkSkin)
    elif (CheckeredSkin.hits(mouseX, mouseY)):
        CheckeredSkin.have=True
        if (CheckeredSkin.removed==False):
            CheckeredSkin.removed=True
            cacheChoice.remove(CheckeredSkin)

    elif (dabPerson.hits(mouseX, mouseY)):
        dabPerson.have=True
        if (dabPerson.removed==False):
            dabPerson.removed=True
            cacheChoice.remove(dabPerson)

    elif (dancePerson.hits(mouseX, mouseY)):
        dancePerson.have=True
        if (dancePerson.removed==False):
            dancePerson.removed=True
            cacheChoice.remove(dancePerson)

    if (skin.hits(mouseX, mouseY)):
        acc.centerX=10000
        skin.centerX=10000
        wrap.centerX=10000
        red.centerX=100
        blue.centerX=100
        green.centerX=100
        Purple.centerX=100
        black.centerX=225
        selection.centerX=10000
        weapon.centerX=10000

        if (texturedSkin.have==True):
            textSkinLab.centerX=225
            textSkinLab.visible=True

        if (pinkSkin.have==True):
            pinkSkinLab.centerX=225

        if (CheckeredSkin.have==True):
            checkeredSkinLab.centerX=340

        if (goldSkin.bought==True):
            gold.centerX=225
            gold.centerY=125
            gold.visible=True

    if (CancelEmote.hits(mouseX, mouseY)):
        person.rotateAngle=360
        weaponList[app.Wlevel].visible=True
        cape.visible=False
        CancelEmote.centerX=10000
        Emotes.centerX=10000
        LSign.visible=False
        shot.visible=False
        bulletL.visible=False
        gun.rotateAngle=360
        weaponList[app.Wlevel].centerX=200
        person.fill=skinColors[app.level]
        dabPerson.centerX=10000
        discoBall.visible=False
        dancePerson.centerX=10000
        if (person.centerX != 200):
            person.centerX=200
        if (app.background=='white'):
            grenadeHold.centerX=person.centerX + 20
            grenadeHold.centerY=person.centerY-10
            if (app.Wlevel==0):
                weaponList[app.Wlevel].visible=False

            elif (app.Wlevel>0):
                weaponSlot3.centerX=275
                if (UseGun.visible==True):
                    weaponList[app.Wlevel].visible=False

                elif (grenadeHold.visible==True):
                     weaponList[app.Wlevel].visible=False

                else:
                     weaponList[app.Wlevel].visible=False
            UseGun.x1=200
            first.centerX=60
            weaponSlot1.centerX=325
            weaponSlot2.centerX=375
        if (app.background != 'white'):
            lobby.centerX=25
        if (app.background=='navy'):
            locker.centerX=75
            itemShop.centerX=137
            cache.centerX=200
            battlePass.centerX=37
            obj.centerX=105
            Play.centerX=350
            PlayButton.centerX=350
            easy.centerX=350
            medium.centerX=350
            hard.centerX=350
            impossible.centerX=350
    if (battlePass.hits(mouseX, mouseY)):
        Header.value='Warriors'
        Subtitle.value='Pass'
        Subtitle.visible=True
        gun.centerX=10000
        playerSpot.visible=False
        acc.visible=True
        acc.centerX=10000
        person.centerX=10000
        selection.visible=False
        pick.centerX=10000
        PlayButton.centerX=10000
        Play.centerX=10000
        easy.centerX=10000
        medium.centerX=10000
        hard.centerX=10000
        impossible.centerX=10000
        username.centerX=10000
        redDotLabel.centerX=10000
        greenDotLabel.centerX=10000
        CrosshairLabel.centerX=10000
        blueCrossLab.centerX=10000
        goldSkin.visible=False
        goldLab.centerX=10000
        shopCrosshair.visible=False
        shopCrossLab.centerX=10000
        gold.centerX=10000
        third.centerX=10000
        first.centerX=10000
        selection.centerX=10000
        page2.centerX=10000
        page1.centerX=10000
        weapon.centerX=10000
        pickLab.centerX=10000
        gunLab.centerX=10000
        starWandShop.centerX=10000
        starWandShop.visible=False
        wandLab.centerX=10000
        wand.centerX=10000
        weaponList[app.Wlevel].visible=False
        black.centerX=10000
        ShopL.visible=False
        Emote5Lab.centerX=10000
        CancelEmote.centerX=10000
        cachePlay.centerX=10000
        cacheCount.centerX=10000
        cacheCount.visible=False
        youGotMes.centerX=10000
        dancePerson.centerX=10000
        red.centerX=10000
        blue.centerX=10000
        green.centerX=10000
        Purple.centerX=10000
        black.centerX=10000
        textSkinLab.centerX=10000
        pinkSkinLab.centerX=10000
        checkeredSkinLab.centerX=10000
        gold.centerX=10000
        Emote.centerX=10000
        Emotes.centerX=10000
        emPickLab.centerX=10000
        doublePickLab.centerX=10000
        doublePick.centerX=10000
        levels.visible=True
        onArrow.visible=True
        battleRewards.visible=True
        battleRewards.toFront()
        obj1.visible=False
        obj2.visible=False
        obj3.visible=False
        obj4.visible=False
        obj5.visible=False
        if (battlePass.bought==False):
            selection2.visible=True
            BatpassLab.centerX=200
            selection2.value='This costs 500 S.S'
        else:
            selection2.visible=False
            BatpassLab.centerX=10000

    if (BatpassLab.hits(mouseX, mouseY)):
        if (currencyCount.value>=500):
            battlePass.bought=True
            currencyCount.value-=500
            BatpassLab.centerX=10000
            levels.visible=False
            battleRewards.visible=False
            icon.centerX=200
            icon.centerY=200
            icon.width=200
            icon.height=200
            selection2.value='Warrior Pass Bought!'
            selection2.size=25
            selection2.fill='white'
            sleep(3)
            icon.centerX=315
            icon.centerY=15
            icon.width=20
            icon.height=20
            selection2.visible=False
            levels.visible=True
            battleRewards.visible=True
        else:
            selection2.value='You do not have enough S.S to purchase this'
    if (obj.hits(mouseX, mouseY)):
        Header.value='Objectives'
        Subtitle.visible=False
        gun.centerX=10000
        playerSpot.visible=False
        acc.visible=True
        acc.centerX=10000
        person.centerX=10000
        selection.visible=False
        pick.centerX=10000
        PlayButton.centerX=10000
        Play.centerX=10000
        easy.centerX=10000
        medium.centerX=10000
        hard.centerX=10000
        impossible.centerX=10000
        username.centerX=10000
        redDotLabel.centerX=10000
        greenDotLabel.centerX=10000
        CrosshairLabel.centerX=10000
        blueCrossLab.centerX=10000
        goldSkin.visible=False
        goldLab.centerX=10000
        shopCrosshair.visible=False
        shopCrossLab.centerX=10000
        gold.centerX=10000
        third.centerX=10000
        first.centerX=10000
        selection.centerX=10000
        page2.centerX=10000
        page1.centerX=10000
        weapon.centerX=10000
        pickLab.centerX=10000
        gunLab.centerX=10000
        starWandShop.centerX=10000
        starWandShop.visible=False
        wandLab.centerX=10000
        wand.centerX=10000
        weaponList[app.Wlevel].visible=False
        black.centerX=10000
        ShopL.visible=False
        Emote5Lab.centerX=10000
        CancelEmote.centerX=10000
        cachePlay.centerX=10000
        cacheCount.centerX=10000
        cacheCount.visible=False
        youGotMes.centerX=10000
        dancePerson.centerX=10000
        red.centerX=10000
        blue.centerX=10000
        green.centerX=10000
        Purple.centerX=10000
        black.centerX=10000
        textSkinLab.centerX=10000
        pinkSkinLab.centerX=10000
        checkeredSkinLab.centerX=10000
        gold.centerX=10000
        Emote.centerX=10000
        Emote1.centerX=10000
        Emote2.centerX=10000
        Emote3.centerX=10000
        Emote4.centerX=10000
        Emote5.centerX=10000
        Emote6.centerX=10000
        Emote7.centerX=10000
        emPickLab.centerX=10000
        doublePickLab.centerX=10000
        doublePick.centerX=10000
        levels.visible=False
        onArrow.visible=False
        selection2.visible=False
        battleRewards.visible=False
        battleRewards.toFront()
        BatpassLab.centerX=10000
        selection2.visible=False
        obj1.visible=True
        obj2.visible=True
        obj3.visible=True
        obj4.visible=True
        obj5.visible=True
    if (person.rotateAngle==90):
        if (battlePass.bought==True):
            if (app.background=='white'):
                if (obj1Count.value < 1):
                    CTC1.centerX=75
                else:
                    CTC1.centerX=10000
    if (CTC1.hits(mouseX, mouseY)):
        obj1Count.value += 1
        CTC1.centerX=10000
        obj1.fill='green'
        objCount()
    if (LSign.visible==True):
        if (battlePass.bought==True):
            if (app.background=='white'):
                if (obj2Count.value < 1):
                    CTC2.centerX=75
                else:
                    CTC2.centerX=10000
    if (CTC2.hits(mouseX, mouseY)):
        obj2Count.value+=1
        CTC2.centerX=10000
        obj2.fill='green'
        objCount2()

    if (CTC3.hits(mouseX, mouseY)):
        obj3Count.value += 1
        CTC3.centerX=10000
        obj3.fill='green'
        objCount3()

    if (CTC4.hits(mouseX, mouseY)):
        obj4Count.value += 1
        CTC4.centerX=10000
        obj4.fill='green'
        objCount4()

    if (CTC5.hits(mouseX, mouseY)):
        obj5Count.value += 1
        CTC5.centerX=10000
        obj5.fill='green'
        objCount5()
    #WeaponSlot Mouse Events
    if (weaponSlot2.hits(mouseX, mouseY)):
        weaponList[app.Wlevel].visible=False
        if (third.centerX==60):
            grenadeHold.visible=True
            UseGun.visible=False
            grenadeHold.centerX=200
            grenadeHold.centerY=365
            grenadeHold.width=35
            grenadeHold.height=70
        if (first.centerX==60):
            UseGun.visible=False
            grenadeHold.visible=True
            grenadeHold.centerX=person.centerX + 20
            grenadeHold.centerY=person.centerY-10
            grenadeHold.width=20
            grenadeHold.height=20
        if (grenadeCount.value == 0):
            grenadeHold.visible=False
    if (weaponSlot1.hits(mouseX, mouseY)):
        weaponList[app.Wlevel].visible=False
        if (third.centerX==60):
            UseGun.visible=True
            grenadeHold.visible=False
        if (first.centerX==60):
            UseGun.visible=True
            grenadeHold.visible=False
            UseGun.x1=person.centerX
            UseGun.y1=person.centerY-10
            UseGun.lineWidth=3
    if (weaponSlot3.hits(mouseX, mouseY)):
        if (third.centerX==60):
            UseGun.visible=False
            grenadeHold.visible=False
            weaponList[app.Wlevel].centerX=200
            weaponList[app.Wlevel].visible=True
            weaponList[app.Wlevel].centerY=350
        if (first.centerX==60):
            grenadeHold.visible=False
            UseGun.visible=False
            weaponList[app.Wlevel].visible=True
            if (weaponList[app.Wlevel].visible==True):
                if (app.Wlevel==1):
                    weaponList[app.Wlevel].centerX=person.centerX
                    weaponList[app.Wlevel].centerY=person.centerY - 13
                    weaponList[app.Wlevel].width =  weaponList[app.Wlevel].width=92
                    weaponList[app.Wlevel].height =  weaponList[app.Wlevel].height=44
                if (app.Wlevel==2):
                    weaponList[app.Wlevel].centerX=person.centerX - 15
                    weaponList[app.Wlevel].centerY=person.centerY - 5
                    weaponList[app.Wlevel].width =  weaponList[app.Wlevel].width=92
                    weaponList[app.Wlevel].height =  weaponList[app.Wlevel].height=44
                if (app.Wlevel==3):
                    weaponList[app.Wlevel].centerX=person.centerX
                    weaponList[app.Wlevel].centerY=person.centerY - 13
                    weaponList[app.Wlevel].width =  weaponList[app.Wlevel].width=92
                    weaponList[app.Wlevel].height =  weaponList[app.Wlevel].height=44

                if (app.Wlevel==4):
                    weaponList[app.Wlevel].centerX=person.centerX
                    weaponList[app.Wlevel].centerY=person.centerY - 15
                    weaponList[app.Wlevel].width =  weaponList[app.Wlevel].width=92
                    weaponList[app.Wlevel].height =  weaponList[app.Wlevel].height=44
    if (third.centerX==60):
        if (weaponSlot3.hits(mouseX, mouseY)):
            if (app.Wlevel != 4):
                weaponList[app.Wlevel].width=160
                weaponList[app.Wlevel].height=80
            else:
                weaponList[app.Wlevel].width=175
                weaponList[app.Wlevel].height=110
    if (app.Wlevel == 0):
        if (app.background != 'black'):
            UseGun.fill='black'
            weaponSlot3.centerX=10000
    else:
        if (app.background=='black'):
            UseGun.fill='grey'
            weaponSlot3.centerX=275
    #Grenade mouse Events
    if (grenadeHold.hits(mouseX, mouseY)):
        if (grenadeCount.value>0):
            if (grenadeHold.visible==True):
                grenadeHold.centerY=200
                grenadeHold.width=10
                grenadeHold.height=10
                sleep(1)
                background.visible=True
                sleep(1)
                grenadeHold.centerY=375
                grenadeHold.width=40
                grenadeHold.height=50
                background.visible=False
                currencyCount.value += 3
                grenadeCount.value-=1
                if (battlePass.bought==True):
                    zombCount.value += 3
                for zomb in zombies.children:
                    zomb.centerY=25
            if (first.centerX==60):
                grenadeHold.centerX=person.centerX + 20
                grenadeHold.centerY=person.centerY-10
                grenadeHold.width=20
                grenadeHold.height=20
            if (grenadeCount.value == 0):
                grenadeHold.visible=False
    if (UseGun.visible==True):
        if (ammoCount.value>0):
            ammoCount.value -= 1
    for emote in Emotes.children:
        if (emote.hits(mouseX, mouseY)):
            Emote.centerX=10000
            Emote1.centerX=10000
            Emote2.centerX=10000
            Emote3.centerX=10000
            Emote4.centerX=10000
            Emote5.centerX=10000
            Emote6.centerX=10000
            Emote7.centerX=10000
            lobby.centerX=10000
            locker.centerX=10000
            itemShop.centerX=10000
            cache.centerX=10000
            battlePass.centerX=10000
            obj.centerX=10000
            Play.centerX=10000
            PlayButton.centerX=10000
            easy.centerX=10000
            medium.centerX=10000
            hard.centerX=10000
            impossible.centerX=10000
            first.centerX=10000
            weaponSlot1.centerX=10000
            weaponSlot2.centerX=10000
            weaponSlot3.centerX=10000
    if (zombCount.value == 20):
        medKit.visible=True
        medKit.centerX=zomb1.centerX
    elif (zombCount.value == 40):
        medKit.visible=True
        medKit.centerX=zomb1.centerX
    elif (zombCount.value == 60):
        medKit.visible=True
        medKit.centerX=zomb1.centerX
    elif (zombCount.value == 80):
        medKit.visible=True
        medKit.centerX=zomb1.centerX
    elif (zombCount.value == 100):
        medKit.visible=True
        medKit.centerX=zomb1.centerX
    elif (zombCount.value == 120):
        medKit.visible=True
        medKit.centerX=zomb1.centerX
    elif (zombCount.value == 140):
        medKit.visible=True
        medKit.centerX=zomb1.centerX
    elif (zombCount.value == 160):
        medKit.visible=True
        medKit.centerX=zomb1.centerX
    if (person.hitsShape(zombSpawn1)):
        if (zombSpawn1health.x2 > 194):
            zombSpawn1health.x2-=0.5
        else:
            for zomb in zombies.children:
                zomb.centerX=10000
            app.health=100
            first.centerX=10000
            weaponSlot1.centerX=10000
            weaponSlot2.centerX=10000
            weaponSlot3.centerX=10000
            grenadeCount.visible=False
            ammoCount.visible=False
            selection3.value=''
            onLight.centerX=10000
            zombSpawn1.visible=False
            zombSpawn1Bar.visible=False
            zombSpawn1health.visible=False
            lobby.centerX=25
            winMes.visible=True
            person.centerX=10000
            UseGun.centerX=10000
            grenadeHold.centerX=10000
            app.background='green'
            Emotes.centerX=10000
    if (zombCount.value==50):
        app.background='black'
        onLight.centerX=325
        zomb1Eyes.visible=True
        zomb2Eyes.visible=True
        zomb3Eyes.visible=True
        zomb1.visible=False
        zomb2.visible=False
        zomb3.visible=False
        if (app.level==0):
            person.fill='grey'
        if (app.Wlevel==0):
            UseGun.fill='grey'
    elif (zombCount.value==100):
        app.background='black'
        onLight.centerX=325
        zomb1Eyes.visible=True
        zomb2Eyes.visible=True
        zomb3Eyes.visible=True
        zomb1.visible=False
        zomb2.visible=False
        zomb3.visible=False
        if (app.level==0):
            person.fill='grey'
        if (app.Wlevel==0):
            UseGun.fill='grey'
    elif (zombCount.value==150):
        app.background='black'
        onLight.centerX=325
        zomb1Eyes.visible=True
        zomb2Eyes.visible=True
        zomb3Eyes.visible=True
        zomb1.visible=False
        zomb2.visible=False
        zomb3.visible=False
        if (app.level==0):
            person.fill='grey'
        if (app.Wlevel==0):
            UseGun.fill='grey'
    elif (zombCount.value==200):
        app.background='black'
        onLight.centerX=325
        zomb1Eyes.visible=True
        zomb2Eyes.visible=True
        zomb3Eyes.visible=True
        zomb1.visible=False
        zomb2.visible=False
        zomb3.visible=False
        if (app.level==0):
            person.fill='grey'
        if (app.Wlevel==0):
            UseGun.fill='grey'
    elif (zombCount.value==250):
        app.background='black'
        onLight.centerX=325
        zomb1Eyes.visible=True
        zomb2Eyes.visible=True
        zomb3Eyes.visible=True
        zomb1.visible=False
        zomb2.visible=False
        zomb3.visible=False
        if (app.level==0):
            person.fill='grey'
        if (app.Wlevel==0):
            UseGun.fill='grey'
    if (onLight.hits(mouseX, mouseY)):
        app.background='white'
        onLight.centerX=10000
        zomb1Eyes.visible=False
        zomb2Eyes.visible=False
        zomb3Eyes.visible=False
        zomb1.visible=True
        zomb2.visible=True
        zomb3.visible=True
        currencyCount.value -= 20
        zombSpawn1.centerX=200
        zombSpawn1Bar.visible=True
        zombSpawn1health.visible=True
    if (zomb1.hits(mouseX, mouseY)):
        ammo.visible=True
        ammo.centerX=zomb1.centerX
        ammo.centerY=zomb1.centerY
        ammo.toFront()

    elif (zomb2.hits(mouseX, mouseY)):
        ammo.visible=True
        ammo.centerX=zomb2.centerX
        ammo.centerY=zomb2.centerY
        ammo.toFront()

    elif (zomb3.hits(mouseX, mouseY)):
        ammo.visible=True
        ammo.centerX=zomb3.centerX
        ammo.centerY=zomb3.centerY
        ammo.toFront()
def onMouseMove(mouseX, mouseY):
    #Play Button events
    if (PlayButton.contains(mouseX, mouseY)):
        PlayButton.fill='green'
    else:
        PlayButton.fill=None
    mouse.centerX = mouseX
    mouse.centerY = mouseY
#Gun Move game events
    if (zombSpawn1health.x2 > 194):
        UseGun.x2 = 0 + (mouseX / 1)

#Scope events
    if (scope.visible==True):
        scope.centerX=mouseX
        scope.centerY=mouseY
    else:
        scope.centerX=10000
#Zombie gets bigger events
    for zomb in zombies.children:
        if (lens.hitsShape(zomb)):
            zomb.width=zomb.largeW
            zomb.height=zomb.largeH
        else:
            zomb.width=zomb.smallW
            zomb.height=zomb.smallH
def onStep():
    #animated money
    icon.rotateAngle+=30
    #Zombie play events
    if (app.background=='white'):
        zombSpawn1.centerX=200
        zombSpawn1.visible=True
        if (zombSpawn1health.x2 > 194):
            zomb1.centerY +=10
            zomb2.centerX+=6
            zomb2.centerY+=10
            zomb3.centerX-=6
            zomb3.centerY+=12
            zomb2.centerX=zomb1.centerX - 30
            zomb3.centerX=zomb1.centerX + 30
            onLight.centerX=10000
            if (app.level==0):
                person.fill='black'
    if (app.background=='white'):
        if (UseGun.visible==True):
            zomb1.centerX=UseGun.centerX
        elif (grenadeHold.visible==True):
            zomb1.centerX=grenadeHold.centerX
        elif (weaponList[app.Wlevel].centerY==350):
            zomb1.centerX=weaponList[app.Wlevel].centerX
        else:
            zomb1.centerX=person.centerX
    if (app.background=='black'):
        if (zombSpawn1health.x2 > 194):
            zomb1Eyes.centerX=zomb1.centerX
            zomb1Eyes.centerY=zomb1.centerY-20
            zomb2Eyes.centerX=zomb2.centerX
            zomb2Eyes.centerY=zomb2.centerY-20
            zomb3Eyes.centerX=zomb3.centerX
            zomb3Eyes.centerY=zomb3.centerY-20
            zomb1.centerY +=10
            zomb2.centerX+=6
            zomb2.centerY+=10
            zomb3.centerX-=6
            zomb3.centerY+=10
            zomb2.centerX=zomb1.centerX - 30
            zomb3.centerX=zomb1.centerX + 30
            zombSpawn1.centerX=10000
            zombSpawn1Bar.visible=False
            zombSpawn1health.visible=False
            if (app.level==0):
                person.fill='grey'
            else:
                person.fill=skinColors[app.level]
            for zombEyes in zombieEyes.children:
                if (zombEyes.centerY>400):
                    zombEyes.centerY=25
                else:
                    zombEyes.centerY+=10
                    for zomb in zombies.children:
                        zomb.centerY += 10
            if (UseGun.visible==True):
                zomb1.centerX=UseGun.centerX
            elif (grenadeHold.visible==True):
                zomb1.centerX=grenadeHold.centerX
            elif (weaponList[app.Wlevel].centerY==350):
                zomb1.centerX=weaponList[app.Wlevel].centerX
            else:
                zomb1.centerX=person.centerX
    if (zomb1.hitsShape(UseGun)==True):
        if (UseGun.visible==True):
            app.health-=10
            zomb1.centerY=25
            Health.x2-=10
        if (first.centerX==60):
            if (grenadeHold.visible==False):
                if (zomb1.hitsShape(person)):
                    if (app.background != 'green'):
                        app.health-=10
                        zomb1.centerY=25
                        Health.x2-=10

        if (grenadeHold.visible==True):
            if (zomb1.hitsShape(grenadeHold)):
                if (app.background != 'green'):
                    app.health-=10
                    zomb1.centerY=25
                    Health.x2-=10

        if (weaponList[app.Wlevel].centerY==350):
            if (zomb1.hitsShape(weaponList[app.Wlevel])):
                if (app.background != 'green'):
                    app.health-=10
                    zomb1.centerY=25
                    Health.x2-=10

    elif (zomb2.hitsShape(UseGun)==True):
        if (UseGun.visible==True):
            if (app.background != 'green'):
                app.health-=10
                zomb2.centerY=25
                zomb2.centerX=15
                Health.x2-=10

        if (first.centerX==60):
            if (grenadeHold.visible==False):
                if (zomb2.hitsShape(person)):
                    if (app.background != 'green'):
                        app.health-=10
                        zomb2.centerY=25
                        zomb2.centerX=15
                        Health.x2-=10

        if (grenadeHold.visible==True):
            if (zomb2.hitsShape(grenadeHold)):
                if (app.background != 'green'):
                    app.health-=10
                    zomb2.centerY=25
                    zomb2.centerX=15
                    Health.x2-=10

        if (weaponList[app.Wlevel].centerY==350):
            if (zomb2.hitsShape(weaponList[app.Wlevel])):
                if (app.background != 'green'):
                    app.health-=10
                    zomb2.centerY=25
                    zomb2.centerX=15
                    Health.x2-=10

    elif (zomb3.hitsShape(UseGun)==True):
        if (UseGun.visible==True):
            if (app.background != 'green'):
                app.health-=10
                zomb3.centerY=25
                zomb3.centerX=340
                Health.x2-=10

        if (first.centerX==60):
            if (grenadeHold.visible==False):
                if (zomb3.hitsShape(person)):
                    if (app.background != 'green'):
                        app.health-=10
                        zomb3.centerY=25
                        zomb3.centerX=340
                        Health.x2-=10

        if (grenadeHold.visible==True):
            if (zomb3.hitsShape(grenadeHold)):
                if (app.background != 'green'):
                    app.health-=10
                    zomb3.centerY=25
                    zomb3.centerX=340
                    Health.x2-=10

        if (weaponList[app.Wlevel].centerY==350):
            if (zomb3.hitsShape(weaponList[app.Wlevel])):
                if (app.background != 'green'):
                    app.health-=10
                    zomb3.centerY=25
                    zomb3.centerX=340
                    Health.x2-=10

    #Die events
    if (Health.x2<=12):
        app.health=0

    if (app.health==0):
        first.centerX=10000
        weaponSlot1.centerX=10000
        weaponSlot2.centerX=10000
        weaponSlot3.centerX=10000
        grenadeCount.visible=False
        ammoCount.visible=False
        selection3.value=''
        onLight.centerX=10000
        zombSpawn1.visible=False
        zombSpawn1Bar.visible=False
        zombSpawn1health.visible=False
        lobby.centerX=25
        app.background='red'
        UseGun.visible=False
        zomb1.visible=False
        zomb2.visible=False
        zomb3.visible=False
        person.visible=False
        grenadeHold.visible=False
        messageDie.centerX=200
        weaponList[app.Wlevel].toFront()

    #Zombies that miss, reset
    for zomb in zombies.children:
        if (zomb.centerY>400):
            zomb.centerY=25

    #Easter egg animation events
    if (person.moneyGlitch==True):
        currencyCount.value+=100
        if (currencyCount.value>=1100):
            currencyCount.value=0

    if (app.background=='white'):
        zombSpawn1.visible=True
        zombSpawn1Bar.visible=True
        zombSpawn1health.visible=True
        ammoCount.visible=True
        grenadeCount.visible=True

    if (grenadeCount.value<3):
        if (battlePass.bought==True):
            if (obj3Count.value < 1):
                CTC3.centerX=75
            else:
                CTC3.centerX=10000

    if (winMes.visible==True):
        if (battlePass.bought==True):
            if (obj5Count.value < 1):
                CTC5.centerX=75
            else:
                CTC5.centerX=10000

    if (app.background=='black'):
        person.fill='grey'
    else:
        person.fill=skinColors[app.level]

def onKeyPress(key):

    #scope visibility events
    if (key=='z'):
        if (UseGun.visible==True):
            if (app.background=='white'):
                if (scope.visible == True):
                    scope.visible = False
                else:
                    scope.visible = True
        elif (grenadeHold.visible==True):
            scope.visible=False
    #Person Move events
    if ((app.background == 'white') or (app.background=='black')):
        if (key == 'w'):
            if (first.centerX==60):
                person.centerY -=20
                UseGun.centerY -= 20
                grenadeHold.centerY -= 20
                if (weaponList[app.Wlevel].visible==True):
                    weaponList[app.Wlevel].centerY -= 20
        if (key =='s'):
            if (first.centerX==60):
                person.centerY+=20
                UseGun.centerY += 20
                grenadeHold.centerY += 20
                if (weaponList[app.Wlevel].visible==True):
                    weaponList[app.Wlevel].centerY += 20
        if (key =='a'):
            if (first.centerX==60):
                person.centerX-=20
                UseGun.centerX -= 20
                grenadeHold.centerX -= 20
                if (weaponList[app.Wlevel].visible==True):
                    weaponList[app.Wlevel].centerX -= 20
        if (key =='d'):
            if (first.centerX==60):
                person.centerX+=20
                UseGun.centerX += 20
                grenadeHold.centerX += 20
                if (weaponList[app.Wlevel].visible==True):
                    weaponList[app.Wlevel].centerX += 20
    #Ammo Pickup
    if ((app.background=='white') or (app.background=='black')):
        if (person.hitsShape(ammo)):
            if (key=='r'):
                ammo.centerX=10000
                ammoCount.value+=20
        if (person.hitsShape(medKit)):
            if (key=='r'):
                medKit.visible=False
                Health.x2=108
                app.health=100
                if (battlePass.bought==True):
                    if (app.background !='black'):
                        if (obj4Count.value < 1):
                            CTC4.centerX=75
                        else:
                            CTC4.centerX=10000

def onKeyHold(keys):
    if ((app.background == 'white') or (app.background=='black')):
        if ('w' in keys):
            if (first.centerX==60):
                person.centerY -=20
                UseGun.centerY -= 20
                grenadeHold.centerY -= 20
                if (weaponList[app.Wlevel].visible==True):
                    weaponList[app.Wlevel].centerY -= 20
        if ('s' in keys):
            if (first.centerX==60):
                person.centerY+=20
                UseGun.centerY += 20
                grenadeHold.centerY += 20
                if (weaponList[app.Wlevel].visible==True):
                    weaponList[app.Wlevel].centerY += 20
        if ('a' in keys):
            if (first.centerX==60):
                person.centerX-=20
                UseGun.centerX -= 20
                grenadeHold.centerX -= 20
                if (weaponList[app.Wlevel].visible==True):
                    weaponList[app.Wlevel].centerX -= 20
        if ('d' in keys):
            if (first.centerX==60):
                person.centerX+=20
                UseGun.centerX += 20
                grenadeHold.centerX += 20
                if (weaponList[app.Wlevel].visible==True):
                    weaponList[app.Wlevel].centerX += 20




cmu_graphics.run()