import g2d
from random import randint


X_CANVAS = 500
Y_CANVAS = 500
MAN_SPEED = 15
W_CAR = 33
H_CAR = 85


difficolta = 1 # 1 - 3
skin = 1 # 1 - 2

x_man = 250
velocita = 8 #VELOCITA INIZIALE
velocita_massima = 80
punti = 0
cont = 0
inizializzato = True


class Car:
    def __init__(self,corsia):
        self._y = 0 - randint(100, 1200)
        self._x = 0
        self._type = randint(1, 8)
        if corsia == 1:
            self._x = 53# 1
        elif corsia == 2:
            self._x = 153 # 2
        elif corsia == 3:
            self._x = 250  # 3
        elif corsia == 4:
            self._x = 347
        elif corsia == 5:
            self._x = 447
            
    def inizializza(self):
        self._y = 0 - randint(100, 1200)
        self._type = randint(1, 8)
            
    def avanza(self):
        self._y+= velocita
        if self._y > randint(900, 9000):
            self._y = - 100
            self._type = randint(1, 8)
            
    def printCar(self):
        if self._type == 1: g2d.draw_image("img/car1.png",(self._x-W_CAR,self._y),(W_CAR*2,H_CAR))          
        elif self._type == 2: g2d.draw_image("img/car2.png",(self._x-W_CAR,self._y),(W_CAR*2,H_CAR))
        elif self._type == 3: g2d.draw_image("img/car3.png",(self._x-W_CAR,self._y),(W_CAR*2,H_CAR))
        elif self._type == 4: g2d.draw_image("img/car4.png",(self._x-W_CAR,self._y),(W_CAR*2,H_CAR))
        elif self._type == 5: g2d.draw_image("img/car5.png",(self._x-W_CAR,self._y),(W_CAR*2,H_CAR))
        elif self._type == 6: g2d.draw_image("img/car6.png",(self._x-W_CAR,self._y),(W_CAR*2,H_CAR))
        elif self._type == 7: g2d.draw_image("img/car7.png",(self._x-W_CAR,self._y),(W_CAR*2,H_CAR))
        elif self._type == 8: g2d.draw_image("img/car8.png",(self._x-W_CAR,self._y),(W_CAR*2,H_CAR))
    
    def collisione(self, man_x, man_y) -> bool:
        global inizializzato
        car_left = self._x - W_CAR
        car_right = self._x + W_CAR
        car_top = self._y
        car_bottom = self._y + H_CAR


        man_left = man_x - 15
        man_right = man_x + 15
        man_top = man_y + 4
        man_bottom = man_y + 76

        if (car_right > man_left and car_left < man_right and car_bottom > man_top and car_top < man_bottom):
            inizializzato = False
            return True
        return False


car1 = Car(1)
car2 = Car(2)
car3 = Car(3)
car4 = Car(4)
car5 = Car(5)

def inizializzaGioco():
    global x_man, velocita, punti, velocita_massima
    car1.inizializza()
    car2.inizializza()
    car3.inizializza()
    car4.inizializza()
    car5.inizializza()
    x_man = 250
    velocita = 8
    punti = 0

def printBG():
    g2d.draw_image("img/BG.png",(0,0),(X_CANVAS,Y_CANVAS))

def printMenu():
    g2d.draw_image("img/menu.png",(0,0),(X_CANVAS,Y_CANVAS))
    
def printMenuC():
    g2d.draw_image("img/menuC.png",(0,0),(X_CANVAS,Y_CANVAS))
    
    
def printMan():
    global skin
    if skin == 1:
        g2d.draw_image("img/man1.png",(x_man-15,Y_CANVAS-100),(x_man+15,Y_CANVAS-100+97))
    elif skin == 2:
        g2d.draw_image("img/man2.png",(x_man-15,Y_CANVAS-100),(x_man+15,Y_CANVAS-100+97))

def printGM(score):
    g2d.draw_image("img/gameOver.png",(0,0),(X_CANVAS,Y_CANVAS))
    g2d.set_color((200,0,0))
    g2d.draw_text(str(score),(330,415),27)

def play() -> int:
    global x_man, velocita, cont, inizializzato, punti, pause
    cont += 1
    keys = g2d.current_keys()
    if ("d" in keys or "ArrowRight" in keys)and x_man < 450:
        x_man += MAN_SPEED
    elif ("a" in keys or "ArrowLeft" in keys)and x_man > 50:
        x_man -= MAN_SPEED
    elif "LeftButton" in g2d.current_keys() or "RightButton" in g2d.current_keys():
        xm, xy = g2d.mouse_pos();
        if xm < x_man -10:
            x_man -= MAN_SPEED
        elif xm > x_man + 10:
            x_man += MAN_SPEED
    elif "Escape" in keys:
        inizializzato = False
        return -2
    

    if x_man < 50:
        x_man = 50
    elif x_man > 450:
        x_man = 450
        
    printBG()
    printMan()

    car1.printCar()
    car1.avanza()
    car2.printCar()
    car2.avanza()    
    car3.printCar()
    car3.avanza()    
    car4.printCar()
    car4.avanza()
    car5.printCar()
    car5.avanza()
    
    if car1.collisione(x_man,Y_CANVAS - 100) or car2.collisione(x_man,Y_CANVAS - 100) or car3.collisione(x_man,Y_CANVAS - 100) or car4.collisione(x_man,Y_CANVAS - 100) or car5.collisione(x_man,Y_CANVAS - 100):
            inizializzato = False
            return 1
    
    if velocita < velocita_massima:
        if cont % 300 == 0:
            velocita+=1
            if difficolta >= 2:
                velocita+=1
                if difficolta == 3:
                    velocita+=1
        if cont % 50 == 0:
            punti+= 1
            
    return -1

def ConfirmMessage():
    printConfirmMessage()
    if g2d.mouse_clicked() or g2d.mouse_right_clicked():
        xm, ym = g2d.mouse_pos()
        if xm >= 177 and xm <= 224 and ym >= 396 and ym <= 429:
            return 1
        elif (xm >= 272 and xm <= 319 and ym >= 396 and ym <= 429) or (xm >= 185 and xm <= 312 and ym >= 277 and ym <= 332) :
            return 0 
        elif xm >= 134 and xm <= 353 and ym >= 83 and ym <= 183:
            return -1 #PLAY
        elif xm >= 188 and xm <= 313 and ym >= 202 and ym <= 258:
            return -4 #SETTINGS
        elif xm >= 28 and xm <= 90 and ym >= 56 and ym <= 120:
            return -5 #CREDITS
    return -3

def printConfirmMessage():
    g2d.draw_image("img/quit.png",(0,0),(X_CANVAS,Y_CANVAS))



def printSettings():
    global difficolta
    g2d.draw_image("img/settings.png",(0,0),(X_CANVAS,Y_CANVAS))
    if difficolta == 1:
        g2d.draw_image("img/puntoVerde.png",(356,139),(10,10))
    elif difficolta == 2:
        g2d.draw_image("img/puntoArancione.png",(377,139),(10,10))
    elif difficolta == 3:
        g2d.draw_image("img/puntoRosso.png",(398,139),(10,10))
        
    if skin == 1:
        g2d.draw_image("img/puntoAzzurro.png",(165,380),(10,10))
    elif skin == 2:
        g2d.draw_image("img/puntoAzzurro.png",(329,380),(10,10))
        
def settings():
    global difficolta, velocita_massima, skin
    printSettings()
    if g2d.mouse_clicked() or g2d.mouse_right_clicked():
        xm, ym = g2d.mouse_pos()
        if xm >= 77 and xm <= 120 and ym >= 69 and ym <= 96:
            return -2
        elif xm >= 351 and xm <= 366 and ym >= 134 and ym <= 149:
            difficolta = 1
            velocita_massima = 80
        elif xm >= 372 and xm <= 387 and ym >= 134 and ym <= 149:
            difficolta = 2
            velocita_massima = 90
        elif xm >= 393 and xm <= 408 and ym >= 134 and ym <= 149:
            difficolta = 3
            velocita_massima = 100
        elif xm >= 142 and xm <= 192 and ym >= 240 and ym <= 395:
            skin = 1
        elif xm >= 300 and xm <= 362 and ym >= 240 and ym <= 395:
            skin = 2
    return -4
    
    
def menuC():    
    printMenuC()
    if g2d.mouse_clicked() or g2d.mouse_right_clicked():
        xm, ym = g2d.mouse_pos()
        if xm >= 134 and xm <= 353 and ym >= 83 and ym <= 183:
            return -1 #PLAY
        elif xm >= 188 and xm <= 313 and ym >= 277 and ym <= 331:
            return -3 #QUIT
        elif xm >= 188 and xm <= 313 and ym >= 202 and ym <= 258:
            return -4 #SETTINGS
        elif xm >= 28 and xm <= 90 and ym >= 56 and ym <= 120:
            return -2 #NO CREDITS
    return -5
    
def menu():
    printMenu()
    if g2d.mouse_clicked() or g2d.mouse_right_clicked():
        xm, ym = g2d.mouse_pos()
        if xm >= 134 and xm <= 353 and ym >= 83 and ym <= 183:
            return -1 #PLAY
        elif xm >= 188 and xm <= 313 and ym >= 277 and ym <= 331:
            return -3 #QUIT
        elif xm >= 188 and xm <= 313 and ym >= 202 and ym <= 258:
            return -4 #SETTINGS
        elif xm >= 28 and xm <= 90 and ym >= 56 and ym <= 120:
            return -5 #CREDITS
    return -2

opt = -2
contOver = 0
contPause = 0

def tick():
    global opt,inizializzato, punti, contOver
    if opt == -2:    
        contOver = 0
        opt = menu()
    elif opt == -1:
        if not inizializzato:
            inizializzato = True
            pause = False
            inizializzaGioco()
        g2d.clear_canvas()
        opt = play()
    elif opt == -4:
            opt = settings()
    elif opt == -3:
        opt = ConfirmMessage()
        if opt == 1:
            g2d.close_canvas()
        elif opt == 0:
            opt = -2
    elif opt == -5:
        opt = menuC()
    elif opt == 1:
        g2d.clear_canvas()
        contOver+=1
        if contOver >= 80 or "Escape" in g2d.current_keys(): 
            opt = -2
            contOver = 0
        printGM(punti)

        

        
def main():
    g2d.init_canvas((X_CANVAS, Y_CANVAS))
    g2d.main_loop(tick)
main()