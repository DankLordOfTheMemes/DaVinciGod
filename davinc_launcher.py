## A FAIRE ##
#petit bug quand on clique sur l'arbre des competences: de temps en temps ca marche mal



#equilibrer les variations de populations SI TU Y ARRIVE (self.viePop *= 0.9xx par exemple, il faut juste varier le coef) j'ai pas testé la periode 3 qui risque de partir en couille

      




# IMPORT #
from threading import Thread
import os
import pygame
import math
from pygame.locals import *
import time
import random
import os


chemin = os.getcwd()
print(chemin) 

pygame.init()
gameDisplay = pygame.display.set_mode((1280,720))
pygame.display.set_caption("DA VINCI GOD")
ico = pygame.image.load('data/png/favicon.png').convert_alpha()
pygame.display.set_icon(ico)
# ASSEMBLAGE #

epoque = 0
#global menu_vie
menu_vie = False

#global menu_creation_vie
menu_creation_vie = False
#global gif_set
gif_set = 0
vie_lock = True


class Animation(Thread): #anime gif
    
    
    def __init__(self, cheminDossier, posx, posy):    
        Thread.__init__(self)
        self.n = 1
        self.cheminDossier = cheminDossier
        self.posx = posx
        self.posy = posy
        
        while (1):
            try:
                self.chemin = self.cheminDossier + str(self.n) + ".gif"
                test = pygame.image.load(self.chemin)
                self.n = self.n + 1
            except:
                print(self.n)
                break
                
    def run(self):
      global nom_fin,conso_fin,rejet_fin
      while (menu_creation_vie == True):
        
        i= 0
        for i in range(0,self.n):
                if (menu_creation_vie != True):
                  break
              #•  print(self.posx, "      frame n° ", i)
                self.chemin = self.cheminDossier + str(i) + ".gif"
                #test = image.load(self.chemin)
                gameDisplay.blit(pygame.image.load(self.chemin), ((self.posx,self.posy)))
                
                gameDisplay.blit(creation_info,(0,0))

                
                time.sleep(0.04)

# CLASS #

lock_pop = 0
chrono_stop = False

class alea_events(Thread):

  def __init__(self):
    Thread.__init__(self)
    self.event = 0
    self.hap_2 = 0
  
  def run(self):
    global dev_alea, meteor_1, chrono_stop

    def event():
      global dev_alea, meteor_1, chrono_stop
      event_space = ['Meteore','Trou noir']


      time.sleep(20)


      self.hap_2 = random.randint(0,500)
      
      if self.hap_2 > 495 :
        return event_space[1]
      if self.hap_2 < 220 :
        meteor_1 = Meteor(look_meteor,0.1,1,0,0)
        return event_space[0]
      else :
        return 0
   
    time.sleep(30)
    print("events on the way")
    
    while 1 :
      if chrono_stop == False :
        self.event = event()
        print("event : ", self.event, self.hap_2)
      else :
        print("event.pause 10s")
        time.sleep(10)


class alea_events_pop(Thread):
    def __init__(self):
      Thread.__init__(self)
      self.event_pop = 0
      self.hap = 0
    
    def run(self):
        global dev_alea, chrono_stop, lock_pop
        
        def eventpop():
            global dev_alea, chrono_stop, lock_pop
            event_alea = ['Aire glaciere','Rechauffement climatique','Guerre','Famine','Maladie']
            time.sleep(30)
            
            
            
            self.hap = random.randint(0,100)
            
            if dev_alea == "eau" :
                if self.hap < 3 :
                  return event_alea[0]
                if self.hap < 5 :
                    return event_alea[3]
                if self.hap < 10 :
                    return event_alea[1] 
                
            
            if dev_alea == "terre" :
                if self.hap < 3 :
                  return event_alea[1]
                if self.hap < 5 :
                    return event_alea[3]
                if self.hap < 10 :
                    return event_alea[0]
                
            
            if dev_alea == "peuple" :
                if self.hap < 5 :
                    return event_alea[2]
                if self.hap < 15 :
                    return event_alea[3]
                if self.hap < 25 :
                  return event_alea[4]

            if dev_alea == "guerre":
                if self.hap < 5 :
                    return event_alea[3]
                if self.hap < 15 :
                    return event_alea[2]
                if self.hap < 25:
                  return event_alea[1]
                
            
            if dev_alea == "" :
                return 0

        while 1 :
          
          if chrono_stop == False :
            self.event_pop = eventpop()
            print("event_pop : ", self.event_pop, self.hap)
            time.sleep(10)
            self.event_pop = ''
            lock_pop = 0
            
          else :
            print("event_pop.pause 10s")
            time.sleep(10)

class chrono(Thread):
  def __init__(self):
      Thread.__init__(self)

      self.minute = 6

      self.sc = 0
  def run(self):
      global points, chrono_stop, planete_choice
      i = 0
      while 1 :
        if chrono_stop == True :
            self.sc = self.sc
            self.minute = self.minute
        else :

            time.sleep(1)
            self.sc += 1
              
            
              
            if (self.sc % 2 == 0):
              points +=1
              
              
            i += 1

            if i == 25 :
              if planete_choice != 0 :
                points += 1
              i = 0

class Hitboxes:
    def __init__(self,taille_x,taille_y,place_x,place_y,opacite,point):
      self.rect = pygame.Rect((place_x, place_y), (taille_x, taille_y))
      self.surf = pygame.Surface(self.rect.size)
      self.surf.fill((255,0,255))
      self.surf.set_alpha(opacite)
      self.point = point

    def remove(self):
      self.rect = pygame.Rect((0,0), (0, 0))
      
      
class Especes():  #################################################### REMPLACER COMPLETEMENT L'ANCIENNE CLASSE PAR CELLE-CI (si elle existe dans ta version je sais plus)

  global planete_choice, epoque

  
  def __init__(self):
        
        
        
        self.vieNom = "Espece libre"
        self.vieCons = ""
        self.vieRej = ""
        self.viePop = 0
        self.vieConsTaux = 0
        self.vieRejTaux = 0
        self.vieCoefVie = 0
        
  def especesTick(self):
      
      #['Dioxygene', 'CO2', 'Souffre', 'Dihydrogene']
      
      if (self.viePop >= 1):
        if (self.vieCons == 'Dioxygene' and planete_choice.dioxygene > 15):
          if (epoque == 1):
            self.viePop *=1.0005
            print(planete_choice.dioxygene)
          elif (epoque == 2):
            self.viePop *=1.005
          elif (epoque == 3):
            self.viePop *= 1.02
            
          planete_choice.dioxygene *= 1-(self.viePop / 1000000000)
            
            
            
        elif (self.vieCons == 'Dioxygene' and planete_choice.dioxygene <= 15 and planete_choice.dioxygene > 10):
            self.viePop *=0.990
            planete_choice.dioxygene *= 0.99999
        
        
        
        
        elif (self.vieCons == 'CO2' and planete_choice.CO2 > 10):
          if (epoque == 1):
            self.viePop *=1.0005
          elif (epoque == 2):
            self.viePop *=1.005
          elif (epoque == 3):
            self.viePop *= 1.02
          
        
          planete_choice.CO2 *= 1-(self.viePop / 1000000000)
          
          
          
        elif (self.vieCons == 'CO2' and planete_choice.CO2<= 10 and planete_choice.CO2 > 5):
          self.viePop *=0.990
          planete_choice.CO2 *= 0.99999
          
          
          
          
          
        
        elif (self.vieCons == 'Souffre' and planete_choice.Souffre > 15):
          if (epoque == 1):
            self.viePop *=1.0005
          elif (epoque == 2):
            self.viePop *=1.005
          elif (epoque == 3):
            self.viePop *= 1.02
          planete_choice.Souffre *= 1-(self.viePop / 1000000000)
          
          
          
        elif (self.vieCons == 'Dioxygene' and planete_choice.Souffre <= 15 and planete_choice.Souffre > 10):
          self.viePop *=0.990
          planete_choice.Souffre *= 0.99999
        
        
        
        
        
        
        elif (self.vieCons == 'Dihydrogene' and planete_choice.dihydrogene > 15):
          if (epoque == 1):
            self.viePop *=1.0005
          elif (epoque == 2):
            self.viePop *=1.005
          elif (epoque == 3):
            self.viePop *= 1.02
          planete_choice.dihydrogene *= 1-(self.viePop / 1000000000)
          
          
        elif (self.vieCons == 'Dihydrogene' and planete_choice.dihydrogene<= 15 and planete_choice.dihydrogene > 10):
          self.viePop *=0.990
          planete_choice.dihydrogene *= 0.99999


        elif (self.vieCons == 'Azote' and planete_choice.Azote > 15):
          if (epoque == 1):
            self.viePop *=1.0005
          elif (epoque == 2):
            self.viePop *=1.005
          elif (epoque == 3):
            self.viePop *= 1.02
          planete_choice.Azote *= 1-(self.viePop / 1000000000)
          
          
        elif (self.vieCons == 'Azote' and planete_choice.Azote<= 15 and planete_choice.Azote > 10):
          self.viePop *=0.990
          planete_choice.Azote *= 0.99999          
      
        
        else:
          self.viePop = 0
        
        if (self.vieRej == 'dioxygene'):
          if (planete_choice.dioxygene != 0):
            planete_choice.dioxygene *= 1.0001
          else:
            planete_choice.dioxygene += 0.1
            
        elif (self.vieRej == 'CO2'):
          if (planete_choice.CO2 != 0):
            planete_choice.CO2 *= 1.0001
          else:
            planete_choice.CO2 += 0.1
            
        elif (self.vieRej == 'Souffre'):
          if (planete_choice.Souffre != 0):
            planete_choice.Souffre *= 1.0001
          else:
            planete_choice.Souffre += 0.1
          
        elif (self.vieRej == 'Dihydrogene'):
          if (planete_choice.dihydrogene != 0):
            planete_choice.dihydrogene *= 1.0001
          else:
            planete_choice.dihydrogene += 0.1
        
        elif (self.vieRej == 'Azote'):
          if (planete_choice.Azote != 0):
            planete_choice.Azote *= 1.0001
          else:
            planete_choice.Azote += 0.1   
        
        
        
        
        
      else:
        self.viePop = 0
     # print(str(planete_choice.dioxygene))
     
      #planete_choice.Azote = 100 - planete_choice.dioxygene - planete_choice.dihydrogene
      

class Planete:
    def __init__(self,nom,rayon,periode,envergure,look, type,  hasard):
        self.nom = nom
        self.rayon = rayon
        self.periode = periode
        self.envergure = envergure
        self.omega = (2*math.pi) / self.periode
        self.i = 0
        self.look = look
        self.look_z = pygame.transform.rotozoom(look,0,self.envergure)
        self.type = type
        
        self.dioxygene = 0
        self.CO2 = 0
        self.Azote = 0
        self.Souffre = 0
        self.dihydrogene = 0
        self.eau = 'non'
        self.atmosphere = 'ngton'
        self.temperature = 16
        text_type = ['Tellurique', 'Gazeux', 'Magmatique', 'Chaotique']

        
        
        if (self.type == 'Tellurique'):                                #####################################################REMPLACER LES ACIEN RANDOM.RANDINT PAR LES NOUVEAUX
          self.dioxygene = random.randint(10,45)
          self.CO2 = random.randint(0,45)
          self.Souffre = 0
          self.dihydrogene = 0
          if (self.rayon == 100):
            self.eau = "Gaz"
          elif (self.rayon == 200):
            self.eau = "Liquide"
          elif (self.rayon == 300):
            self.eau = "Solide"
            
            
        elif (self.type == 'Gazeux'):
          self.dioxygene = random.randint(0,4)
          self.CO2 = random.randint(0,2)
          self.Souffre = 0
          self.dihydrogene = random.randint(80,94)
          self.eau = "NON"
          
        elif (self.type == 'Magmatique'):
          self.dioxygene = random.randint(0,20)
          self.CO2 = random.randint(0,30)
          self.Souffre = random.randint(0,40)
          self.dihydrogene = 0
          self.eau = "Gaz"
        
        elif self.type == 'Chaotique':
          self.dioxygene = random.randint(0,2)
          self.CO2 = random.randint(0,2)
          self.Souffre = random.randint(10,80)
          self.dihydrogene = random.randint(0,3)
          self.atmosphere = 'non'
          self.eau = 'Gaz'
          
        if (self.envergure == 0.1 and self.type != 'Gazeux'):
          if (random.randint(0,2) == 2):
            self.atmosphere = 'oui'
          else:
            self.atmosphere = 'non'
        elif (self.envergure == 0.2 and self.type != 'Gazeux'):
          if (random.randint(0,10) >= 2):
            self.atmosphere = 'oui'
            
        else:
          self.atmosphere = 'oui'
          
        if (self.rayon == 100):
          self.temperature = random.randint(0,600)
        elif (self.rayon == 200):
          self.temperature = random.randint(-50,50)
        elif (self.rayon == 300):
          self.temperature = random.randint(-600,0)
          
        self.Azote = 100 - self.dioxygene - self.CO2 - self.Souffre - self.dihydrogene
        
        
        
        
        
        
        self.rect = pygame.Rect((0, 0), (0, 0))                  
        #self.surf = pygame.Surface(self.rect.size)
        #self.surf = pygame.Surface(self.rect.size)
        
        self.hasard = hasard

    def tourner(self) :
        
        """self.surf = pygame.Surface(self.rect.size)
        self.surf.fill((255,0,255))
        self.surf.set_alpha(50)"""

        
        self.x = self.rayon*math.cos(self.omega*self.i)
        self.x2 = int(self.x)+630
        self.y = self.rayon*math.sin(self.omega*self.i)
        self.y2 = int(self.y)+340
        self.i = self.i + 1
        
        if self.envergure == 0.1 :
            self.rect = pygame.Rect((self.x2, self.y2), (25, 25))
        
        if self.envergure == 0.2 :
            self.rect = pygame.Rect((self.x2, self.y2), (50, 50))

        if self.envergure == 0.3 :
            self.rect = pygame.Rect((self.x2, self.y2), (77, 77))
    
    def ecologie(self): # planete_choice.ecologie()
      global total_vie

      if total_vie < 10000 :
        
        if self.type == 'Tellurique' :
          if self.dioxygene < 60 :
            self.dioxygene += random.randint(0,1)/10000
          if self.CO2 < 40 :
            self.CO2 += random.randint(0,1)/10000
          if self.Souffre < 5 :  
            self.Souffre += random.randint(0,1)/10000
          if self.dioxygene < 10 :  
            self.dihydrogene += random.randint(0,1)/10000
        
        if self.type == 'Gazeux':
          if self.dioxygene < 20 :
            self.dioxygene += random.randint(0,1)/10000
          if self.CO2 < 30 :
            self.CO2 += random.randint(0,1)/10000
          if self.Souffre < 5 :  
            self.Souffre += random.randint(0,1)/10000
          if self.dioxygene < 70 :  
            self.dihydrogene += random.randint(0,1)/10000

        if self.type == 'Magmatique':
          if self.dioxygene < 20 :
            self.dioxygene += random.randint(0,1)/10000
          if self.CO2 < 20 :
            self.CO2 += random.randint(0,1)/10000
          if self.Souffre < 35 :  
            self.Souffre += random.randint(0,1)/10000
          if self.dioxygene < 10 :  
            self.dihydrogene += random.randint(0,1)/10000

        if self.type == 'Chaotique':
          if self.dioxygene < 15 :
            self.dioxygene += random.randint(0,1)/10000
          if self.CO2 < 10 :
            self.CO2 += random.randint(0,1)/10000
          if self.Souffre < 45 :  
            self.Souffre += random.randint(0,1)/10000
          if self.dioxygene < 10 :  
            self.dihydrogene += random.randint(0,1)/10000
    
    def dessiner(self):
        #pygame.draw.circle(gameDisplay,(self.couleur),((self.x2, self.y2)), self.envergure)
        #gameDisplay.blit(self.surf,self)
        gameDisplay.blit(self.look_z,(self.x2, self.y2))
        #gameDisplay.blit(self.surf,(self.x2, self.y2))

class Meteor:
  
  def __init__(self,look,envergure,vitesse,x,y):
    self.envergure = envergure
    self.look = pygame.transform.rotozoom(look,random.randint(1,180),self.envergure)
    self.vitesse = vitesse
    self.x = random.randint(0,1280)
    self.y = y - 10
    self.x2 = x
    self.y2 = y
    self.i = x
    self.ratio = 1
    self.rect = pygame.Rect((0, 0), (0, 0)) 
    if self.x >= 640 :
      self.ratio = -1
    else :
      self.ratio = 1
    self.gone = False
  def going_in(self):
    
    self.x2 = self.x + (self.i*self.ratio)
    self.y2 = self.y + self.i
    self.i  = self.i + self.vitesse
    self.rect = pygame.Rect((self.x2, self.y2), (50, 50)) #20 20
    
    if self.x2 > 1280 or self.y2 > 720 :
      self.gone = True 
  
  def dessiner(self):
    gameDisplay.blit(self.look,(self.x2, self.y2))


# VARIABLE #

pop_ag = pygame.image.load('data/png/pop_glace.png').convert_alpha()
pop_rc = pygame.image.load('data/png/pop_chaud.png').convert_alpha()
pop_gu = pygame.image.load('data/png/pop_guerre.png').convert_alpha()
pop_fa = pygame.image.load('data/png/pop_miam.png').convert_alpha()
pop_ma = pygame.image.load('data/png/pop_virus.png').convert_alpha() 

#Variable skiiltreea
skill_tree_champi = False
skill_tree_2a = pygame.image.load('data/jpg/arbre2a.jpg').convert_alpha()
skill_tree_2b = pygame.image.load('data/jpg/arbre2b.jpg').convert_alpha()
lock2a = pygame.image.load('data/png/lock2a.png').convert_alpha()
lock2b = pygame.image.load('data/png/lock2b.png').convert_alpha()

fin_tree = pygame.image.load("data/jpg/avantfin.jpg").convert_alpha()
ge = False
# VARIABLE D'ECRAN DE JEU
gif_vie = []
gif_vie.append(Animation("data/gif_vie/tmp-",0, 0))
creation_info = pygame.image.load('data/png/creation.png').convert_alpha()

vie_background = pygame.image.load("data/jpg/especesMenu.jpg").convert_alpha()



look_1 = pygame.image.load('data/png/look1.png').convert_alpha()
look_2 = pygame.image.load('data/png/look2.png').convert_alpha()
look_3 = pygame.image.load('data/png/look3.png').convert_alpha()
look_4 = pygame.image.load('data/png/look4.png').convert_alpha()
look_5 = pygame.image.load('data/png/look5.png').convert_alpha()
look_6 = pygame.image.load('data/png/look6.png').convert_alpha()
look_7 = pygame.image.load('data/png/look7.png').convert_alpha()
look_8 = pygame.image.load('data/png/look8.png').convert_alpha()
look_9 = pygame.image.load('data/png/look9.png').convert_alpha()
look_10 = pygame.image.load('data/png/look10.png').convert_alpha()
look_11 = pygame.image.load('data/png/look11.png').convert_alpha()
look_12 = pygame.image.load('data/png/look12.png').convert_alpha()
look_13 = pygame.image.load('data/png/look13.png').convert_alpha()


look_meteor = pygame.image.load('data/png/meteor.png').convert_alpha()


"""Terre = Planete('Terre',149, 365.25,0.2,look_1)
Mars = Planete('Mars',227, 286.98,0.2,look_2)
Wuut = Planete(195,206,7,(15,30,70))
Jupiter = Planete(80,800,12,(150,50,15))"""

clock = pygame.time.Clock()

gameover = pygame.image.load("data/jpg/gameover.jpg").convert_alpha()

alerte_valide = pygame.image.load("data/png/alerte_skill.png").convert_alpha()
alerte_non_viable = pygame.image.load("data/png/alerte_before_tree.png").convert_alpha()

alerte_same = pygame.image.load("data/png/alertesame.png").convert_alpha()
alerte_done = pygame.image.load("data/png/alertenom.png").convert_alpha()
alerte_crea = pygame.image.load("data/png/alertecrea.png").convert_alpha()
alerte_not  = pygame.image.load("data/png/alerte_not.png").convert_alpha()

alerte_log = pygame.image.load("data/png/alertelog.png").convert_alpha()
alerte_log_rect = alerte_log.get_rect()
alerte_log_surface = pygame.Surface((alerte_log_rect.width, alerte_log_rect.height), pygame.SRCALPHA)
alerte_log_surface.fill((0, 0, 0, 0))
alerte_log_surface.blit(alerte_log, alerte_log_rect)

top_bar = pygame.image.load("data/png/menu_top.png").convert_alpha()
top_bar_rect = top_bar.get_rect()
top_bar_surface = pygame.Surface((top_bar_rect.width, top_bar_rect.height), pygame.SRCALPHA)
top_bar_surface.fill((0, 0, 0, 0))
top_bar_surface.blit(top_bar, top_bar_rect)

menu = pygame.image.load("data/png/menu.png").convert_alpha()
menu_rect = menu.get_rect()
menu_surface = pygame.Surface((menu_rect.width, menu_rect.height), pygame.SRCALPHA)
menu_surface.fill((0, 0, 0, 0))
menu_surface.blit(menu, menu_rect)

background = pygame.image.load("data/jpg/background.jpg").convert_alpha()
background_rect = background.get_rect()
background_surface = pygame.Surface((background_rect.width, background_rect.height), pygame.SRCALPHA)
background_surface.fill((0, 0, 0, 0))
background_surface.blit(background, background_rect)

soleil = pygame.image.load('data/png/soleil.png').convert_alpha()
soleil_rect = soleil.get_rect()
soleil_surface = pygame.Surface((soleil_rect.width, soleil_rect.height), pygame.SRCALPHA)
soleil_surface.fill((0, 0, 0, 0))
soleil_surface.blit(soleil, soleil_rect)

gameExit = False
planete_stat = False
psc = 0


#VARIABLE DES OPTIONS
bg_option = pygame.image.load('data/jpg/bg_option.jpg').convert_alpha()

# CREDIT
bg_credit = pygame.image.load('data/jpg/creditbg.jpg').convert_alpha()

# VARIABLE DE CONSTRUCTION DE PLANETE 

font=pygame.font.Font(None, 50)
font2=pygame.font.Font(None,30)
font3= pygame.font.Font(None,70)
font4=pygame.font.Font(None,22)
i = 0

text_nom = ''
text_taille = ['Petit', 'Moyen', 'Grand']
text_type = ['Tellurique', 'Gazeux', 'Magmatique', 'Chaotique']
text_masse = 1000

text_fin_nom = font.render(str(text_nom),1,(255,255,255))
text_fin_taille = font.render(str(text_taille[0]),1,(255,255,255))
text_fin_type = font.render(str(text_type[0]),1,(255,255,255))
text_fin_masse = font.render(str(text_masse),1,(255,255,255))

label_conseil = font.render('',1,(255,255,255))

bg = pygame.image.load('data/jpg/parfait.jpg').convert_alpha()

look_check = [look_1,look_2,look_3,look_4,look_5,look_6,look_7,look_8,look_9,look_10,look_11,look_12,look_13]
i_look = 0

overcrea = False
alerte_nom = False
alerte_check = False
alerte_same_name = False

non_viable = False
tree_viable = False
planete_choice = 0
planete_selec = False
alerte_not_point = False

chapeaux = False

balise_taille = 0
balise_type = 0
positive = True
continuer = 1
ecrire_nom = False

#VARIABLE DU JEUX
timer = chrono()
eve = alea_events()
eve_pop = alea_events_pop()
espece1 = Especes()
espece2 = Especes()
espece3 = Especes()
total_vie = int(espece1.viePop + espece2.viePop + espece3.viePop)
#VARIABLE ECRAN TITRE

logo = pygame.image.load('data/png/logo.png').convert_alpha()
ecrant = pygame.image.load('data/jpg/ecran.jpg')
selc = pygame.image.load('data/png/selection_menu.png').convert_alpha()
#jouer = Hitboxes(431,92,437,125,0,0)
#option = Hitboxes(431,92,467,125,100,0)

# VARIABLES Musiques
#pygame.mixer.music.load('data/mp3/credits.mp3')
pygame.mixer.music.load('data/mp3/mainmusic.mp3')

# VARIABLES SKILLTREE
nb_skill = 0
points = 0                  # A remettre à zéro
last_skill =""
dev_alea = ""

ok = pygame.image.load('data/png/ok.png').convert_alpha()
skill_tree_1 = pygame.image.load('data/jpg/arbre1.jpg').convert_alpha()

#Variable chapo
background_chapo = pygame.image.load('data/jpg/background_chapo.jpg').convert_alpha()
chapo_1 = pygame.image.load('data/png/chapo_1.png').convert_alpha()
chapo_2 = pygame.image.load('data/png/chapo_2.png').convert_alpha()
chapo_3 = pygame.image.load('data/png/chapo_3.png').convert_alpha()
button_parier = pygame.image.load('data/png/button_parier.png').convert_alpha()
star = pygame.image.load('data/png/star.png').convert_alpha()
pari = "None"
choixpo = "None"
porte_chance = 0

# VAriableroulettee
a_color = 8
bg_roulette = pygame.image.load('data/jpg/bg_roulette.jpg').convert_alpha()
dotmark = pygame.image.load('data/png/dotmark.png').convert_alpha()
rules = pygame.image.load('data/jpg/rules.jpg').convert_alpha()
d_arrow = pygame.image.load('data/png/darrow.png').convert_alpha()
dot = True
ruler = False 
diable = False
# MAIN #
menu = True
# VARIABLE CINEMA2
bg2 = pygame.image.load('data/jpg/partie2.jpg')
a_cine = 0
last_cine = "down"
cinematique = False
suite = ""
#TESST#
#Zone de creation de planetes : self,nom,rayon,periode,envergure,look // Terre = Planete(149, 365.25,0.2,look_1)
def definir(text_nom,text_taille,text_masse,text_type,look,hasard) :
  
  plan1_hasard = hasard
  plan1_nom = str(text_nom)
  plan1_look = look
  plan1_type = str(text_type) #text_type = ['Tellurique', 'Gazeux', 'Magmatique', 'Chaotique']
  plan1_envergure = 0.3
  plan1_masse = int(text_masse)

  if plan1_type == 'Tellurique' :
    plan1_hasard = 2 - random.randint(0,2)
  
  if plan1_type == 'Magmatique':
    plan1_hasard = 0 + random.randint(0,2)

  if plan1_type == 'Gazeux' :
    if plan1_hasard < 2 :
      plan1_hasard += random.randint(0,2)
    if plan1_hasard > 2 :
      plan1_hasard -= random.randint(0,2)

  
  if text_taille == 'Petit':
    plan1_envergure = 0.1
    plan1_hasard += 1
    
  elif text_taille == 'Moyen' :
    plan1_envergure = 0.2
    
  elif text_taille == 'Grand' :
    plan1_envergure == 0.3
    plan1_hasard -= 1
    
  if 1000 <= plan1_masse <= 1500 :
    plan1_hasard += 1 + random.randint(0,2)
  if 2000 <= plan1_masse <= 2200 :
    plan1_hasard -= 1 + random.randint(0,2)
  if 3100 <= plan1_masse <= 3700 :
    plan1_hasard += 2 - random.randint(0,2)
  if 4900 <= plan1_masse <= 6000 :
    plan1_hasard += 1 + random.randint(0,2)
  if 7200 <= plan1_masse <= 8300 :
    plan1_hasard -= 2 - random.randint(0,2)

  if plan1_masse == 10000 :
    plan1_hasard += 2 + random.randint(0,2)

  if plan1_nom == 'DATAGRAVE' :
    plan1_hasard = 2
  #print(text_taille)
  plan1_periode = (plan1_envergure*10000)     #RAJOUTER DU RANDOM
  plan1_rayon = (plan1_envergure*1000) 
  
  
  return Planete(plan1_nom,plan1_rayon,plan1_periode,plan1_envergure,plan1_look,plan1_type,plan1_hasard) # Rajouter le type dans la classe planete

label_viable = font.render('',1,(10,255,10))
label_stats = font2.render('',1,(255,255,255))
label_skill = font2.render('',1,(255,255,255))
#---ZONE LOG---
creation = 0                    

plan_log1 = definir(text_nom,text_taille[balise_taille],text_masse,text_type[balise_type],look_check[i_look],0)
plan_log2 = definir(text_nom,text_taille[balise_taille],text_masse,text_type[balise_type],look_check[i_look],0)
plan_log3 = definir(text_nom,text_taille[balise_taille],text_masse,text_type[balise_type],look_check[i_look],0)
plan_log4 = definir(text_nom,text_taille[balise_taille],text_masse,text_type[balise_type],look_check[i_look],0)
plan_log5 = definir(text_nom,text_taille[balise_taille],text_masse,text_type[balise_type],look_check[i_look],0)

#---END ZONE---
meteor_1 = Meteor(look_meteor,0.1,1,0,0) #(self,look,envergure,vitesse,x,y)

#evenement.start()
list_nom_hasard = ["Kobolds","Coyote","Toatse","Mosaoul","Raceav","Fonzee","Vlotkey","Fleanea","Grupeo","Donamel","Arachish","Cooperine","Kaacron"]
nom_vie = list_nom_hasard[random.randint(0,12)]
conso = 'Souffre'
rejet = 'Dihydrogene'
nom_fin = font.render('',1,(255,255,255))
conso_fin = font.render(conso,1,(255,255,255))
rejet_fin = font.render(rejet,1,(255,255,255))
secure = pygame.image.load('data/png/black.png').convert_alpha()
#End Game
terminer = pygame.image.load('data/png/terminer.png').convert_alpha()
ending = pygame.image.load('data/jpg/ending.jpg').convert_alpha()

def tuto():
  global chrono_stop
  image_tuto = pygame.image.load('data/jpg/tutoriel.jpg').convert_alpha()
  tuto_balise = True
  chrono_stop = True
  a = 0
  i = 0
  last = 'stop'
  while tuto_balise :
    for event in pygame.event.get():
      #print(event)
      if event.type == pygame.MOUSEBUTTONUP :
        if event.button == 4 :
          last = 'up'
          if a < 0 :
            a += 15
        
        if event.button == 5 :
          last = 'down'
          if a > -2160 :  
            a -= 15

        if event.button == 2 :
          last = 'stop'
        
        if a < -2080 :
          if event.button == 1 :
            if hitbox_suivant.rect.collidepoint(event.pos):
              tuto_balise = False
      
      if event.type == pygame.QUIT:                                                        
        pygame.quit()
        quit()


    if last == 'stop' :
      a += 0
    
    if last == 'down' :
      if a > -2160 :
        a -= 0.3
    if last == 'up' :
      if a < 0 :
        a += 0.3
    
    if a < -2080 :
      hitbox_suivant = Hitboxes(180,55,565,600,100,0)
    
    
    gameDisplay.blit(image_tuto,(0,a))
    pygame.display.update()

def main_menu() :  
  global menu, chrono_stop
  hitbox_bg = Hitboxes(1000,1000,0,0,0,0)
  hitbox_jouer = Hitboxes(431,92,437,125,0,0)
  hitbox_option = Hitboxes(431,92,437,248,0,0)
  hitbox_quitter = Hitboxes(431,92,437,501,100,0)
  hitbox_credit = Hitboxes(431,92,437,376,100,0)
  a = 0
  b = 0
  flaire = False
  while menu :
    chrono_stop = True
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            #evenement.join()
        if hitbox_bg.rect.collidepoint(pygame.mouse.get_pos()) :
          flaire = False
        if hitbox_jouer.rect.collidepoint(pygame.mouse.get_pos()) :
          a, b = 0, 0
          flaire = True
        if hitbox_option.rect.collidepoint(pygame.mouse.get_pos()) :
          a, b = 0, 123
          flaire = True          
        if hitbox_credit.rect.collidepoint(pygame.mouse.get_pos()) :
          a, b = 0, 251
          flaire = True 
        if hitbox_quitter.rect.collidepoint(pygame.mouse.get_pos()) :
          a, b = 0, 376
          flaire = True
        
        if event.type == pygame.MOUSEBUTTONUP :
          if event.button == 1 :  
            if hitbox_jouer.rect.collidepoint(event.pos):
              menu = False
              hitbox_jouer.remove()
              hitbox_option.remove()
              hitbox_credit.remove()
              print("jeu")
              creationPlanete = True
              while creationPlanete :
                creation_pla()
            if hitbox_option.rect.collidepoint(event.pos) :
              menu = False
              hitbox_jouer.remove()
              hitbox_option.remove()
              hitbox_credit.remove()
              print("options")
              m_option = True
              while m_option :
                m_options()
            if hitbox_credit.rect.collidepoint(event.pos):
              menu = False
              hitbox_jouer.remove()
              hitbox_option.remove()
              hitbox_credit.remove()
              print("Credits")
              m_credit = True
              
              while m_credit == True :
                m_credits()
                
            if hitbox_quitter.rect.collidepoint(event.pos):
              pygame.quit()
              quit()
              
    gameDisplay.blit(ecrant,(0,0))
    
    if flaire == True :
      gameDisplay.blit(selc,(a,b))

    #gameDisplay.blit(hitbox_credit.surf,hitbox_credit)
    pygame.display.update()

def m_options():
  global menu, m_options
  hitbox_fullscreen = Hitboxes(431,92,425,125,100,0)
  hitbox_retour = Hitboxes(431,92,425,505,100,0)
  hitbox_sound_off = Hitboxes(140,140,465,305,110,0)
  hitbox_sound_on = Hitboxes(140,140,690,305,110,0)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
    if event.type == pygame.MOUSEBUTTONUP :
      if event.button == 1 :  
        if hitbox_fullscreen.rect.collidepoint(event.pos):
          size = (1280, 720)
          pygame.display.set_caption("FULLSCREEN")
          return pygame.display.set_mode((size) , pygame.FULLSCREEN)
        
        if hitbox_retour.rect.collidepoint(event.pos):          
          m_option = False
          menu = True
          print("retour") 
          main_menu()
          

        if hitbox_sound_off.rect.collidepoint(event.pos):
          pygame.mixer.music.pause()
        if hitbox_sound_on.rect.collidepoint(event.pos):
          pygame.mixer.music.unpause()

  
  gameDisplay.blit(bg_option,(0,0))
  #gameDisplay.blit(hitbox_sound_on.surf,hitbox_sound_on)
  pygame.display.update()

def m_credits():
  global menu, verrou

  for event in pygame.event.get():
    if event.type == pygame.KEYUP :
      if event.key == 27 :
        menu = True
        while menu:
          main_menu()
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

  
  gameDisplay.fill(0)
  gameDisplay.blit(bg_credit,(0,0))
  pygame.display.update()

def creation_pla() :
    global menu, creation, creationPlanete ,text_fin_nom, text_fin_taille, text_fin_taille, text_fin_type, text_fin_masse, label_conseil, i_look, ecrire_nom, i, text_nom, balise_taille, text_masse, balise_type
    global alerte_check, alerte_nom, alerte_same_name, overcrea, switch_box, chrono_stop, psc
    global plan_log1, plan_log2, plan_log3, plan_log4, plan_log5, suite, planete_choice, nb_skill, last_skill, planete_selec
    chrono_stop = True
    
    hitbox_nom = Hitboxes(350,80,850,130,0,0)
    hitbox_taille_plus = Hitboxes(20,20,1172,252,100,0)
    hitbox_type_plus = Hitboxes(20,20,1172,452,100,0)
    hitbox_masse_plus = Hitboxes(15,15,1174,348,100,0)
    hitbox_masse_moins = Hitboxes(15,15,1174,365,100,0)        # METTRE TOUT CA EN GLOBAL POUR LE PROBLEME DES HITBOXES
    hitbox_sauver = Hitboxes(195,60,883,572,100,0)
    hitbox_visuel_plus = Hitboxes(50,50,285,360,100,0)        
    hitbox_visuel_moin = Hitboxes(50,50,40,360,100,0)
    hitbox_placer = Hitboxes(197,68,68,568,100,0)
    hitbox_carte = Hitboxes(122,38,100,655,100,0)
    
    psc = 0

    for event in pygame.event.get():
        #print(event)

        if event.type == QUIT:
            pygame.quit()
            quit()

        
        
        if event.type == pygame.MOUSEBUTTONUP:
          if event.button == 1 :
            
            if hitbox_sauver.rect.collidepoint(event.pos):
                
                #gameDisplay.fill(0)
                #gameDisplay.blit(font.render('Nom : ' + text_nom + " / Taille :" + text_taille[balise_taille] + " / Masse :" + str(text_masse) + " / Type :" + text_type[balise_type] ,1,(255,255,255)),(0,0))
                #gameDisplay.blit(look_check[i_look],(150,50))
                
                """hitbox_nom.remove()
                hitbox_sauver.remove()
                hitbox_masse_plus.remove()
                hitbox_masse_moins.remove()
                hitbox_taille_plus.remove()
                hitbox_type_plus.remove()"""
                
                creationPlanete = False
                menu = True
                main_menu()

                #positive = False
                pygame.display.update()
            
            if hitbox_placer.rect.collidepoint(event.pos):
              if text_nom != "" :  
                
                if  creation != 5 :
                  
                  
                  print("ALERTE LOG")
                  pygame.display.flip()
                
                  if creation == 0 :
                    log1_1, log1_2, log1_3, log1_4, log1_5 = text_nom, text_taille[balise_taille], text_masse, text_type[balise_type], look_check[i_look]
                    plan_log1 = definir(log1_1, log1_2, log1_3, log1_4, log1_5,random.randint(0,2))#random.randint(0,2))  # CHEATTTTTEERER CHEATTERTET CHETRETTATTR H
                    
                    alerte_check = True
                    creation += 1
                  
                  elif creation == 1 :
                    log2_1, log2_2, log2_3, log2_4, log2_5 = text_nom, text_taille[balise_taille], text_masse, text_type[balise_type], look_check[i_look]
                    plan_log2 = definir(log2_1, log2_2, log2_3, log2_4, log2_5,random.randint(0,2))
                    
                    if plan_log1.nom == plan_log2.nom  :
                      alerte_same_name = True
                    
                    else :
                      alerte_check = True
                      creation += 1
                  
                  elif creation == 2 :
                    log3_1, log3_2, log3_3, log3_4, log3_5 = text_nom, text_taille[balise_taille], text_masse, text_type[balise_type], look_check[i_look]
                    plan_log3 = definir(log3_1, log3_2, log3_3, log3_4, log3_5,random.randint(0,2))
                    
                    if plan_log3.nom == plan_log1.nom or plan_log3.nom == plan_log2.nom  :
                      alerte_same_name = True
                    
                    else :
                      alerte_check = True
                      creation += 1
                  
                  elif creation == 3 :
                    log4_1, log4_2, log4_3, log4_4, log4_5 = text_nom, text_taille[balise_taille], text_masse, text_type[balise_type], look_check[i_look]
                    plan_log4 = definir(log4_1, log4_2, log4_3, log4_4, log4_5,random.randint(0,2))
                    
                    if plan_log4.nom == plan_log1.nom or plan_log4.nom == plan_log2.nom or plan_log4.nom == plan_log3.nom :
                      alerte_same_name = True
                    
                    else :
                      alerte_check = True
                      creation += 1
                  
                  elif creation == 4 :
                    log5_1, log5_2, log5_3, log5_4, log5_5 = text_nom, text_taille[balise_taille], text_masse, text_type[balise_type], look_check[i_look]
                    plan_log5 = definir(log5_1, log5_2, log5_3, log5_4, log5_5,random.randint(0,2))
                    
                    if plan_log5.nom == plan_log1.nom or plan_log5.nom == plan_log2.nom or plan_log5.nom == plan_log3.nom or plan_log5.nom == plan_log4.nom:
                      alerte_same_name = True
                    
                    else :
                      alerte_check = True
                      creation += 1  
                else :
                  overcrea = True
                  print("OVERCREA")
              
              else :
                alerte_nom = True

            if hitbox_carte.rect.collidepoint(event.pos):
              creationPlanete = False
              jouer_carte = True
              while jouer_carte :
                jouer()
              
              print("carte")
            
            if hitbox_visuel_plus.rect.collidepoint(event.pos) :
              if i_look < 12 :
                i_look += 1
              else :
                i_look = 0
            
            if hitbox_visuel_moin.rect.collidepoint(event.pos) :
              if i_look > 0 :
                i_look -= 1
              else :
                i_look = 12                
              #pygame.display.update()

            if hitbox_nom.rect.collidepoint(event.pos) :
              #print("ok")
              label_conseil = font.render('Choisir le nom de la planéte.',1,(255,255,255))
              ecrire_nom = True


            if hitbox_masse_plus.rect.collidepoint(event.pos) :
              label_conseil = font.render('La masse est en puissance de 24 Kg.',1,(255,255,255))
              if text_masse >= 1000 and text_masse <= 9900 :
                text_masse += 100
                text_fin_masse = font.render(str(str(text_masse)),1,(255,255,255))
                pygame.display.update()
            
            if hitbox_masse_moins.rect.collidepoint(event.pos):
              label_conseil = font.render('La masse est en puissance de 24 Kg.',1,(255,255,255))
              if text_masse >= 1100 :
                text_masse -= 100
                text_fin_masse = font.render(str(text_masse),1,(255,255,255))
                pygame.display.update()               

            if hitbox_taille_plus.rect.collidepoint(event.pos) :
              label_conseil = font.render('''Modifier l'envergure de la planéte.''',1,(255,255,255))
              
              if balise_taille < 2 :
                balise_taille += 1
                text_fin_taille = font.render(str(text_taille[balise_taille]),1,(255,255,255))
                pygame.display.update()
              
              else :                        
                balise_taille  = 0 
                
                text_fin_taille = font.render(str(text_taille[balise_taille]),1,(255,255,255))
                pygame.display.update()
              print(text_taille[balise_taille])
              
            
            if hitbox_type_plus.rect.collidepoint(event.pos) :
              label_conseil = font.render('Le type de la planéte est très important.',1,(255,255,255))
              if balise_type < 3 :
                balise_type += 1
                text_fin_type = font.render(str(text_type[balise_type]),1,(255,255,255))
                pygame.display.update()
              else :
                balise_type = 0
                text_fin_type = font.render(str(text_type[balise_type]),1,(255,255,255))
                pygame.display.update() 


        if ecrire_nom == True :
          
          if event.type == pygame.MOUSEBUTTONUP :
            if hitbox_nom.rect.collidepoint(event.pos) == False :
              ecrire_nom = False

          if event.type == KEYDOWN :
            
            if event.key != 8 and event.key != 13 and i < 9 :
              if event.unicode != '' :  
                i += 1
                print(i)
                text_nom += (str(event.unicode))
                text_fin_nom = font.render(str(text_nom),1,(255,255,255))
                #gameDisplay.blit(bg,(0,0))
                pygame.display.update()

            if event.key == 13 :
              ecrire_nom = False
            

            if event.key == 8 :
              text_nom = text_nom[:-1]
              if i > 0 :
                i -= 1
              print(i)
              text_fin_nom = font.render(str(text_nom),1,(255,255,255))
              #gameDisplay.blit(bg,(0,0))
              pygame.display.update()



    if positive :
        gameDisplay.blit(bg,(0,0))
        gameDisplay.blit(text_fin_nom, (870, 160))
        gameDisplay.blit(text_fin_taille, (870,255))
        gameDisplay.blit(text_fin_type,(870,450))
        gameDisplay.blit(text_fin_masse,(870,350))
        gameDisplay.blit(label_conseil,(550,0))
        #gameDisplay.blit(hitbox_placer.surf, hitbox_placer)
        gameDisplay.blit(look_check[i_look],(60,50))
    
    if alerte_check :
      
      hitbox_alerte = Hitboxes(120,50,585,472,100,0)
      gameDisplay.blit(alerte_log_surface,(0,0))
      #gameDisplay.blit(hitbox_alerte.surf, hitbox_alerte)
      
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
          if event.button == 1 :
            if hitbox_alerte.rect.collidepoint(event.pos) == False :
              print("u want...")
            else :
              alerte_check = False

    if alerte_nom :
      
      hitbox_alerte_nom = Hitboxes(120,50,585,472,100,0)
      gameDisplay.blit(alerte_done,(0,0))
      #gameDisplay.blit(hitbox_alerte.surf, hitbox_alerte)
      
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
          if event.button == 1 :
            if hitbox_alerte_nom.rect.collidepoint(event.pos) == False :
              print("sum...")
            else :
              alerte_nom = False

    if alerte_same_name :
      
      hitbox_alerte_same = Hitboxes(120,50,585,472,100,0)
      gameDisplay.blit(alerte_same,(0,0))
      #gameDisplay.blit(hitbox_alerte.surf, hitbox_alerte)
      
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
          if event.button == 1 :
            if hitbox_alerte_same.rect.collidepoint(event.pos) == False :
              print("fuk ?")
            else :
              alerte_same_name = False

    if overcrea :

      hitbox_alerte_overcrea_ok = Hitboxes(120,50,585,472,100,0)
      hitbox_destroy = Hitboxes(120,50,405,470,100,0)
      hitbox_destroy_last = Hitboxes(120,50,765,472,100,0)
      gameDisplay.blit(alerte_crea,(0,0))
      #gameDisplay.blit(hitbox_sauver.surf, hitbox_sauver)
      #gameDisplay.blit(hitbox_destroy_last.surf, hitbox_destroy_last)
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
          if event.button == 1 :
            if hitbox_alerte_overcrea_ok.rect.collidepoint(event.pos) :
              overcrea = False
            if hitbox_destroy.rect.collidepoint(event.pos) :
              creation = 0
              overcrea = False
              planete_choice = 0
              last_skill = ""
              nb_skill = 0
              suite = ""
              planete_selec = False
            
            if hitbox_destroy_last.rect.collidepoint(event.pos) :
              if plan_log5.hasard == 2 :
                overcrea = False
                last_skill = ""
                nb_skill = 0
                suite = ""
                planete_selec = False
              creation -= 1
              overcrea = False


    pygame.display.update()
    
def vie():
  
  global menu_vie, menu_creation_vie, jouer_carte
  
  while (menu_vie == True):
    hitbox_carte = Hitboxes(133,46,1130,675,100,0)               
    hitbox_creer = Hitboxes(175,40,1090,10,100,0)
    hitbox_epdm1 = Hitboxes(265,34,727,85,100,0)
    hitbox_epdm2 = Hitboxes(265,34,727,337,100,0)
    hitbox_epdm3 = Hitboxes(265,34,727,594,100,0)

    
    
    label1_vieNom = font.render(espece1.vieNom,1,(255,255,255))
    label1_vieCons = font.render(espece1.vieCons,1,(255,255,255))
    label1_vieRej = font.render(espece1.vieRej,1,(255,255,255))
    label1_viePop = font.render(str(int(espece1.viePop)),1,(255,255,255))
    
    
    label2_vieNom = font.render(espece2.vieNom,1,(255,255,255))
    label2_vieCons = font.render(espece2.vieCons,1,(255,255,255))
    label2_vieRej = font.render(espece2.vieRej,1,(255,255,255))
    label2_viePop = font.render(str(int(espece2.viePop)),1,(255,255,255))
    
    label3_vieNom = font.render(espece3.vieNom,1,(255,255,255))
    label3_vieCons = font.render(espece3.vieCons,1,(255,255,255))
    label3_vieRej = font.render(espece3.vieRej,1,(255,255,255))
    label3_viePop = font.render(str(int(espece3.viePop)),1,(255,255,255))
    
    
  
  
    gameDisplay.blit(vie_background,(0,0))
    gameDisplay.blit(label1_vieNom,(365,25))
    gameDisplay.blit(label1_viePop,(365,67))
    gameDisplay.blit(label1_vieCons,(365,100))
    gameDisplay.blit(label1_vieRej,(365,140))
    
    gameDisplay.blit(label2_vieNom,(365,277))
    gameDisplay.blit(label2_viePop,(365,319))
    gameDisplay.blit(label2_vieCons,(365,352))
    gameDisplay.blit(label2_vieRej,(365,391))
    
    gameDisplay.blit(label3_vieNom,(365,531))
    gameDisplay.blit(label3_viePop,(365,573))
    gameDisplay.blit(label3_vieCons,(365,606))
    gameDisplay.blit(label3_vieRej,(365,646))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
          evenement.join()
      

        elif event.type == pygame.MOUSEBUTTONUP:
            print("COORDONNES: " + str(event.pos[0]) + "   " + str(event.pos[1]))
            if event.button == 1 :                        #   6 à remplacer par 1 à cause du pavé du pc portable /!\
              if hitbox_carte.rect.collidepoint(event.pos):
                menu_vie = False
                jouer_carte = True
                print("ok la vie")
                while jouer_carte :
                    jouer()
              elif hitbox_creer.rect.collidepoint(event.pos):
                if (espece1.viePop == 0 or espece2.viePop == 0 or espece3.viePop == 0):
                  menu_vie = False
                  menu_creation_vie = True
                  print("on va creer chef")
                  while menu_creation_vie :
                      creer_vie()
              
              elif hitbox_epdm1.rect.collidepoint(event.pos):
                espece1.viePop = espece1.viePop - (espece1.viePop * random.uniform(0.2,0.6))
              elif hitbox_epdm2.rect.collidepoint(event.pos):
                espece2.viePop = espece2.viePop - (espece2.viePop * random.uniform(0.2,0.6))
              elif hitbox_epdm3.rect.collidepoint(event.pos):
                espece3.viePop = espece3.viePop - (espece3.viePop * random.uniform(0.2,0.6))
    
    #gameDisplay.blit(hitbox_epdm1.surf,hitbox_epdm1)
    #gameDisplay.blit(hitbox_creer.surf,hitbox_creer)
    pygame.display.update()
                           
def creer_vie():
  global gif_set, nom_fin, conso_fin, rejet_fin, nom_vie,conso,rejet, menu_creation_vie, menu_vie,vie_lock, list_nom_hasard, nom_vie
  
  """xnom = list_nom_hasard[random.randint(0,12)]
  nom_vie = xnom"""
  

  try:
    gif_vie[gif_set].start()
  except:
    gif_vie.append(Animation("data/gif_vie/tmp-",0, 0))
    gif_set += 1
    gif_vie[gif_set].start()
  

  select = 0
  selectBouton = 0
  i = 0
  atome_type = ['Dioxygene', 'CO2', 'Souffre', 'Dihydrogene','Azote']
  
  
  while (menu_creation_vie == True):
    
        hitbox_nom = Hitboxes(215,34,600,266,100,0)
        hitbox_conso = Hitboxes(25,25,827,320,100,0)
        hitbox_rejet = Hitboxes(25,25,832,375,100,0)
        #hitbox_valider = Hitboxes(191,53,580,515,100,0)
        
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
              evenement.join()
          

            elif event.type == pygame.MOUSEBUTTONUP:
                print("COORDONNES: " + str(event.pos[0]) + "   " + str(event.pos[1]))
                if event.button == 1 :                        #   6 à remplacer par 1 à cause du pavé du pc portable /!\
                
                
                  if hitbox_nom.rect.collidepoint(event.pos):
                    print("nom")
                    select = 0
                    
                    
                  elif hitbox_conso.rect.collidepoint(event.pos):
                    print("conso")
                    select = 1
                    if selectBouton < 4 :
                      selectBouton += 1
                    else:
                      selectBouton = 0
                    conso = str(atome_type[selectBouton])
                    conso_fin = font.render(conso ,1,(255,255,255))
                      
                      
                  elif hitbox_rejet.rect.collidepoint(event.pos):
                    print("rejet")
                    select = 2
                    if selectBouton < 4 :
                      selectBouton += 1
                    else:
                      selectBouton = 0
                    rejet = str(atome_type[selectBouton])
                    rejet_fin = font.render(rejet ,1,(255,255,255))
                    
                    
      
                    
                    
                    
                    
            elif (event.type == KEYDOWN):
              if event.key == K_TAB:
                print("tab") 
                select = select + 1
              if (select >= 3):
                select = 0
              else:
                
                if event.key != 8 and event.key != 13 and i < 9 and select == 0 :
                  if event.unicode != '' :  
                    i += 1
                    nom_vie += (str(event.unicode))
                    nom_fin = font.render(str(nom_vie) + " ",1,(255,255,255))
                    #gameDisplay.blit(bg,(0,0))
                    pygame.display.update()


      
                if event.key == 8 :
                  nom_vie = nom_vie[:-1]
                  if i > 0 :
                    i -= 1
                  nom_fin = font.render(str(nom_vie) + " ",1,(255,255,255))
                  #gameDisplay.blit(bg,(0,0))
                  pygame.display.update()
                if event.key == 13 :
                  
                  
                  if (espece1.viePop == 0):
                  
                    espece1.vieNom = nom_vie
                    espece1.vieCons = conso
                    espece1.vieRej = rejet
                    espece1.viePop = 1000
                    print(espece1.vieNom)
                    print(espece1.vieCons)
                    print(espece1.vieRej)
                    print(espece1.viePop)
                    vie_lock = False
                    menu_creation_vie = False
                    menu_vie = True
                    
                  elif (espece2.viePop == 0):
                    espece2.vieNom = nom_vie
                    espece2.vieCons = conso
                    espece2.vieRej = rejet
                    espece2.viePop = 1000
                    print(espece2.vieNom)
                    print(espece2.vieCons)
                    print(espece2.vieRej)
                    print(espece2.viePop)
                    menu_creation_vie = False
                    menu_vie = True
                  
                  elif (espece3.viePop == 0):
                    espece3.vieNom = nom_vie
                    espece3.vieCons = conso
                    espece3.vieRej = rejet
                    espece3.viePop = 1000
                    print(espece3.vieNom)
                    print(espece3.vieCons)
                    print(espece3.vieRej)
                    print(espece3.viePop)
                    menu_creation_vie = False
                    menu_vie = True



        gameDisplay.blit(secure,(0,0))
        gameDisplay.blit(nom_fin,(602,270))
        gameDisplay.blit(conso_fin,(602,318))
        gameDisplay.blit(rejet_fin,(602,368))


        pygame.display.update()
                
    

              
  gif_vie[gif_set].join()
    
  
  
  
  pygame.display.update()
  while menu_vie :  
    vie()
    
def jouer():
  global jouer_carte, menu, chapeaux, creationPlanete ,text_fin_nom, text_fin_taille, text_fin_taille, text_fin_type, text_fin_masse, label_conseil, i_look, ecrire_nom, i, text_nom, balise_taille, text_masse, balise_type
  global planete_stat, psc, plan_log1, plan_log2, plan_log3, plan_log4, plan_log5, creation, points, chrono_stop, skill_tree_champi
  global label_viable, label_stats, label_skill, non_viable, tree_viable, planete_choice, planete_selec, last_skill, nb_skill, meteor_1
  global label_temperature, label_eau, label_atmosphere, label_dioxygene,label_CO2,label_Souffre, label_Azote, label_dihydrogene
  global menu_vie,vie_lock, epoque, lock_pop, total_vie, suite
  
  total_vie = int(espece1.viePop + espece2.viePop + espece3.viePop)
   
  if int(timer.sc) >= 420 : # VAPE NATION BLAZE IT
    while 1 :
      game_over() 
  
  if espece1.vieNom != 'Espece libre':
    planete_choice.ecologie()

  list_log = [plan_log1.rect, plan_log2.rect, plan_log3.rect, plan_log4.rect, plan_log5.rect]
  list_log_nom = [plan_log1.nom, plan_log2.nom, plan_log3.nom, plan_log4.nom, plan_log5.nom]
  x = meteor_1.rect.collidelist(list_log)
  chrono_stop = False
  #Terre.tourner()
  #Mars.tourner()
  #Wuut.tourner()
  #Jupiter.tourner()
  #if eve.event != 0 :
  #print("event = ", eve.event)
  if eve.event == 'Meteore' :
    if meteor_1.gone != True :
      meteor_1.going_in()

      if x > -1 :
        print("hit :", list_log_nom[x])
        meteor_1.gone = True
        if planete_choice != 0 :
          if list_log_nom[x] == planete_choice.nom :
            nb_skill = 0
            last_skill = ''
            label_skill = font2.render("Meteor",1,(255,0,0))
            espece1.viePop = espece1.viePop - (espece1.viePop * random.uniform(0.8,0.9))
            espece2.viePop = espece2.viePop - (espece2.viePop * random.uniform(0.8,0.9))
            espece3.viePop = espece3.viePop - (espece3.viePop * random.uniform(0.8,0.9))

  
  if creation >= 1 :
    plan_log1.tourner()
  if creation >= 2 :
    plan_log2.tourner()
  if creation >= 3 :
    plan_log3.tourner()
  if creation >= 4 :
    plan_log4.tourner()
  if creation >= 5:
    plan_log5.tourner()
    
    
    
  if vie_lock == False: #sert à faire apparaitre les stats de vies seulement quand on en créé pour la première fois
    espece1.especesTick()
    espece2.especesTick()
    espece3.especesTick()
    

  #hitbox_anti_bug = Hitboxes(2000,700,0,100,100,0)
  hitbox_menu_crea = Hitboxes(245,82,1034,639,100,0)
  hitbox_skill_tree = Hitboxes(395,82,380,639,100,0)
  hitbox_diable = Hitboxes(130,82,907,639,100,0)
  hitbox_jeu_chap = Hitboxes(130,82,777,639,100,0)
  hitbox_creer_vie = Hitboxes(183,37,783,27,100,0)

  for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
        evenement.join()
      

      elif event.type == pygame.MOUSEBUTTONUP:     
            if event.button == 1 :                        #   6 à remplacer par 1 à cause du pavé du pc portable /!\
              
              if meteor_1.gone != True :
                  if meteor_1.rect.collidepoint(event.pos):
                    if points >= 3 :
                      points -= 3
                      meteor_1.gone = True
              
              if hitbox_diable.rect.collidepoint(event.pos) :
                jouer_carte = False
                diable = True
                while diable :
                  roulette()
              
              if hitbox_jeu_chap.rect.collidepoint(event.pos) :
                
                jouer_carte = False
                chapeaux = True
                while chapeaux :
                  chapeau()
              

              elif hitbox_menu_crea.rect.collidepoint(event.pos):
                planete_stat = False
                jouer_carte = False
                creationPlanete = True
                while creationPlanete :
                  creation_pla()
              
              elif hitbox_skill_tree.rect.collidepoint(event.pos):
                
                if last_skill == 'Union' or last_skill == "Science":
                  jouer_carte = False
                  ge = True
                  while ge :
                    good_end()
                
                if suite == "champi" :
                    jouer_carte = False
                    skill_tree_champi = True
                    while skill_tree_champi :
                        skill_tree_a()
                
                if suite == "homme":
                    jouer_carte = False
                    skill_tree_champi = True
                    while skill_tree_champi :
                        skill_tree_b()

                if suite == "":
                    if planete_selec == True :
                      jouer_carte = False
                      skill_tree = True
                      while skill_tree :
                        skill_tree_menu() 
                
                    else :
                      try :  
                        if psc.hasard != 2 :
                          non_viable = True
                        
                        else :
                          tree_viable = True
                      except :
                        pass
                   
              



              if plan_log1.rect.collidepoint(event.pos):
                  
                  planete_stat = True
                  psc = plan_log1

                  

              elif plan_log2.rect.collidepoint(event.pos):
                
                  planete_stat = True
                  psc = plan_log2

                  
              
              elif plan_log3.rect.collidepoint(event.pos):
                 
                  planete_stat = True
                  psc = plan_log3
                  
                  

              elif plan_log4.rect.collidepoint(event.pos):
                 
                  planete_stat = True
                  psc = plan_log4

                  

              elif plan_log5.rect.collidepoint(event.pos):
                 
                  planete_stat = True
                  psc = plan_log5

                  
              if planete_stat :
                
                if hitbox_creer_vie.rect.collidepoint(event.pos):
                    if epoque >= 1 and psc == planete_choice :  
                      print("OK")
                      planete_stat = False
                      jouer_carte = False
                      menu_vie = True
                      while(menu_vie == True):
                        vie()
                    else :
                      print("déso pas des os")

              try :
                if psc.rect.collidepoint(event.pos) == False :
                    planete_stat = False
                    
              except :
                print("Erreur évitée")
                pass
  try :
    if psc.hasard == 2 :  
      label_viable = font.render('VIABLE',1,(10,255,10))
    else :
      label_viable = font2.render('NON-VIABLE',1,(255,10,10))
    
    
    label_stats = font2.render(str(psc.nom),1,(255,255,255))
    if psc == planete_choice :
      label_stats = font2.render(str(psc.nom)+" - Arbre",1,(255,55,25))
      if last_skill != "" :
        label_skill = font2.render("Dev: "+str(last_skill),1,(123,213,231))
  except :
    pass
    
    
  if (psc == plan_log1):
      
    label_eau = font2.render("eau: " + plan_log1.eau,1,(255,255,255))
    label_temperature = font2.render("temperature ambiante : " + str(plan_log1.temperature) + "°C",1,(255,255,255))
    label_distance = font2.render("distance du soleil: " + str(plan_log1.rayon),1,(255,255,255))
    label_atmosphere = font2.render("atmosphere: " + plan_log1.atmosphere ,1,(255,255,255))
    label_dioxygene = font2.render("Taux O²: " + str(int(plan_log1.dioxygene)) + "%",1,(255,255,255))
    label_CO2 = font2.render("Taux CO²: " + str(int(plan_log1.CO2)) + "%",1,(255,255,255))
    label_Souffre = font2.render("Taux Souffre: " + str(int(plan_log1.Souffre)) + "%",1,(255,255,255))
    label_Azote = font2.render("Taux Azote: " + str(int(plan_log1.Azote)) + "%",1,(255,255,255))
    label_dihydrogene = font2.render("Taux H²: " + str(int(plan_log1.dihydrogene)) + "%",1,(255,255,255))
    
  elif (psc == plan_log2):
    label_eau = font2.render("eau: " + plan_log2.eau,1,(255,255,255))
    label_temperature = font2.render("temperature ambiante : " + str(plan_log2.temperature) + "°C",1,(255,255,255))
    label_distance = font2.render("distance du soleil: " + str(plan_log2.rayon),1,(255,255,255))
    label_atmosphere = font2.render("atmosphere: " + plan_log2.atmosphere ,1,(255,255,255))
    label_dioxygene = font2.render("Taux O²: " + str(int(plan_log2.dioxygene)) + "%",1,(255,255,255))
    label_CO2 = font2.render("Taux CO²: " + str(int(plan_log2.CO2)) + "%",1,(255,255,255))
    label_Souffre = font2.render("Taux Souffre: " + str(int(plan_log2.Souffre)) + "%",1,(255,255,255))
    label_Azote = font2.render("Taux Azote: " + str(int(plan_log2.Azote)) + "%",1,(255,255,255))
    label_dihydrogene = font2.render("Taux H²: " + str(int(plan_log2.dihydrogene)) + "%",1,(255,255,255))
  
  elif (psc == plan_log3):
    label_eau = font2.render("eau: " + plan_log3.eau,1,(255,255,255))
    label_temperature = font2.render("temperature ambiante : " + str(plan_log3.temperature) + "°C",1,(255,255,255))
    label_distance = font2.render("distance du soleil: " + str(plan_log3.rayon),1,(255,255,255))
    label_atmosphere = font2.render("atmosphere: " + plan_log3.atmosphere ,1,(255,255,255))
    label_dioxygene = font2.render("Taux O²: " + str(int(plan_log3.dioxygene)) + "%",1,(255,255,255))
    label_CO2 = font2.render("Taux CO²: " + str(int(plan_log3.CO2)) + "%",1,(255,255,255))
    label_Souffre = font2.render("Taux Souffre: " + str(int(plan_log3.Souffre)) + "%",1,(255,255,255))
    label_Azote = font2.render("Taux Azote: " + str(int(plan_log3.Azote)) + "%",1,(255,255,255))
    label_dihydrogene = font2.render("Taux H²: " + str(int(plan_log3.dihydrogene)) + "%",1,(255,255,255))
  
  elif (psc == plan_log4):
    label_eau = font2.render("eau: " + plan_log4.eau,1,(255,255,255))
    label_temperature = font2.render("temperature ambiante : " + str(plan_log4.temperature) + "°C",1,(255,255,255))
    label_distance = font2.render("distance du soleil: " + str(plan_log4.rayon),1,(255,255,255))
    label_atmosphere = font2.render("atmosphere: " + plan_log4.atmosphere ,1,(255,255,255))
    label_dioxygene = font2.render("Taux O²: " + str(int(plan_log4.dioxygene)) + "%",1,(255,255,255))
    label_CO2 = font2.render("Taux CO²: " + str(int(plan_log4.CO2)) + "%",1,(255,255,255))
    label_Souffre = font2.render("Taux Souffre: " + str(int(plan_log4.Souffre)) + "%",1,(255,255,255))
    label_Azote = font2.render("Taux Azote: " + str(int(plan_log4.Azote)) + "%",1,(255,255,255))
    label_dihydrogene = font2.render("Taux H²: " + str(int(plan_log4.dihydrogene)) + "%",1,(255,255,255))
    
  elif (psc == plan_log5):
    label_eau = font2.render("eau: " + plan_log5.eau,1,(255,255,255))
    label_temperature = font2.render("temperature ambiante : " + str(plan_log5.temperature) + "°C",1,(255,255,255))
    label_distance = font2.render("distance du soleil: " + str(plan_log5.rayon),1,(255,255,255))
    label_atmosphere = font2.render("atmosphere: " + plan_log5.atmosphere ,1,(255,255,255))
    label_dioxygene = font2.render("Taux O²: " + str(int(plan_log5.dioxygene)) + "%",1,(255,255,255))
    label_CO2 = font2.render("Taux CO²: " + str(int(plan_log5.CO2)) + "%",1,(255,255,255))
    label_Souffre = font2.render("Taux Souffre: " + str(int(plan_log5.Souffre)) + "%",1,(255,255,255))
    label_Azote = font2.render("Taux Azote: " + str(int(plan_log5.Azote)) + "%",1,(255,255,255))
    label_dihydrogene = font2.render("Taux H²: " + str(int(plan_log5.dihydrogene)) + "%",1,(255,255,255))  
  
  if (psc == planete_choice and vie_lock == False):
    label_espece1 = font2.render(espece1.vieNom + ": " + str(int(espece1.viePop)),1,(255,255,255))
    label_espece2 = font2.render(espece2.vieNom + ": " + str(int(espece2.viePop)),1,(255,255,255))
    label_espece3 = font2.render(espece3.vieNom + ": " + str(int(espece3.viePop)),1,(255,255,255))
    
  
  #gameDisplay.fill(0)
  
  gameDisplay.blit(background_surface,(0,0))

  #Terre.dessiner()
  #Mars.dessiner()
  #Wuut.dessiner()
  #Jupiter.dessiner()
  
  if eve.event == 'Meteore' :
    if meteor_1.gone != True :
      meteor_1.dessiner()
  

  #print("x :", meteor_1.x2, "y :", meteor_1.y2)
  if creation >= 1 :
    plan_log1.dessiner()
  if creation >= 2 :
    plan_log2.dessiner()
  if creation >= 3 :
    plan_log3.dessiner()
  if creation >= 4 :
    plan_log4.dessiner()
  if creation >= 5:
    plan_log5.dessiner()

  gameDisplay.blit(soleil_surface,(510,235))
  
  if planete_stat :
    gameDisplay.blit(top_bar_surface,(0,0))
    
    if psc.hasard != 2 :
      gameDisplay.blit(font4.render("cette planète n'est pas viable",1,(255,100,100)),(770,58))
    
    if psc.hasard == 2 and planete_choice == 0 :
      gameDisplay.blit(font4.render("union à l'arbre de compétence obligatoire",1,(255,100,100)),(725,58))

    if psc.hasard == 2 and planete_choice != 0 and psc!=planete_choice :
      gameDisplay.blit(font4.render("vous pouvez créer la vie ailleur",1,(255,100,100)),(772,58))
    
    if suite == "" and planete_choice == psc:
      gameDisplay.blit(font4.render("vous n'avez pas la compétence requise",1,(255,100,100)),(735,58))


    """for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1 :
            if hitbox_creer_vie.rect.collidepoint(event.pos):
              print("OKOKOKOKOKOKOKOKOKOKOKOK")
              jouer_carte = False
              menu_vie = True
              while(menu_vie == True):
                vie()"""
    
    try:
      
      gameDisplay.blit(label_temperature,(0,0))
      gameDisplay.blit(label_eau,(0,20))
      gameDisplay.blit(label_atmosphere,(0,37))
      gameDisplay.blit(label_dioxygene,(0,57))
      gameDisplay.blit(label_CO2,(0,75))
      gameDisplay.blit(label_Souffre,(300,0))
      gameDisplay.blit(label_Azote,(300,20))
      gameDisplay.blit(label_dihydrogene,(300,40))
      
      if (psc == planete_choice and vie_lock == False):          ##############################################################ICI AJOUT DES STATS DE VIE (prend effet des la premiere creation de vie)
        gameDisplay.blit(label_espece1,(550,0))
        gameDisplay.blit(label_espece2,(550,20))
        gameDisplay.blit(label_espece3,(550,37))
    except:
      print("ERREUR BLINT PLANETE DESCRIPTION")
  
  #print(planete_stat)
  gameDisplay.blit(menu_surface,(0,0))
  if psc != 0 :
      gameDisplay.blit(label_viable,(180,600))
      gameDisplay.blit(label_stats,(180,640))
  
  r = 255
  v = int(255-(0.425*timer.sc))
  b = int(255-(0.425*timer.sc))

  try:
    gameDisplay.blit((font3.render(str(timer.sc)+"M",1,(r,v,b))),(1100,15))
  except:
    print("erreur couleur")
  gameDisplay.blit((font2.render('points :' + str(points),1,(255,255,255))),(1100,60))
  
  
  
  gameDisplay.blit((font2.render('points :' + str(points),1,(255,255,255))),(1100,60))
  """gameDisplay.blit(hitbox_diable.surf, hitbox_diable)"""
  
  if psc == planete_choice :
    if psc != 0 : 
      gameDisplay.blit(label_skill,(180,670))
  
  #event_alea = ['Aire glaciere','Rechauffement climatique','Guerre','Famine','Maladie']
  if espece1.viePop != 0 or espece2.viePop != 0 or espece3.viePop != 0 :
    if eve_pop.event_pop == 'Aire glaciere' :
      gameDisplay.blit(pop_ag,(0,0))
      if lock_pop == 0 :
        
        espece1.viePop = espece1.viePop - (espece1.viePop * random.uniform(0.45,0.80))
        espece2.viePop = espece2.viePop - (espece2.viePop * random.uniform(0.45,0.80))
        espece3.viePop = espece3.viePop - (espece3.viePop * random.uniform(0.45,0.80))
        
        planete_choice.temperature -= 100
        
        lock_pop = 1

    if eve_pop.event_pop == 'Rechauffement climatique' :
      gameDisplay.blit(pop_rc,(0,0))
      if lock_pop == 0 :
        espece1.viePop = espece1.viePop - (espece1.viePop * random.uniform(0.2,0.4))
        espece2.viePop = espece2.viePop - (espece2.viePop * random.uniform(0.2,0.4))
        espece3.viePop = espece3.viePop - (espece3.viePop * random.uniform(0.2,0.4))
        
        planete_choice.temperature += 100    
        
        lock_pop = 1

    if eve_pop.event_pop == 'Guerre':
      gameDisplay.blit(pop_gu,(0,0))
      if lock_pop == 0 :
        espece1.viePop = espece1.viePop - (espece1.viePop * random.uniform(0.05,0.85))
        espece2.viePop = espece2.viePop - (espece2.viePop * random.uniform(0.05,0.85))
        espece3.viePop = espece3.viePop - (espece3.viePop * random.uniform(0.05,0.85))
        lock_pop = 1

    if eve_pop.event_pop == 'Famine' :
      gameDisplay.blit(pop_fa,(0,0))
      if lock_pop == 0 :
        espece1.viePop = espece1.viePop - (espece1.viePop * random.uniform(0.3,0.7))
        espece2.viePop = espece2.viePop - (espece2.viePop * random.uniform(0.3,0.7))
        espece3.viePop = espece3.viePop - (espece3.viePop * random.uniform(0.3,0.7))
        lock_pop = 1

    if eve_pop.event_pop == 'Maladie' :    
      gameDisplay.blit(pop_ma,(0,0))
      if lock_pop == 0 :
        espece1.viePop = espece1.viePop - (espece1.viePop * random.uniform(0.2,0.9))
        espece2.viePop = espece2.viePop - (espece2.viePop * random.uniform(0.2,0.9))
        espece3.viePop = espece3.viePop - (espece3.viePop * random.uniform(0.2,0.9))
        lock_pop = 1

  if last_skill == 'Union' or last_skill == "Science" :
    if total_vie > 100000000 :
      hitbox_terminer = Hitboxes(217,40,975,350,100,0)
      gameDisplay.blit(terminer,(0,0))
      #gameDisplay.blit(hitbox_terminer.surf,hitbox_terminer)
      
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
          if event.button == 1 :
            if hitbox_terminer.rect.collidepoint(event.pos) :
              suite = "Fin"
              jouer_carte = False
              ge = True
              while ge :
                good_end()
  
  if non_viable :
    hitbox_nv_ok = Hitboxes(120,50,585,472,100,0)
    gameDisplay.blit(alerte_non_viable,(0,0))
    gameDisplay.blit(pygame.transform.rotozoom(psc.look,0,0.35),(535,255))
    #gameDisplay.blit(hitbox_nv_ok.surf,hitbox_nv_ok)
    gameDisplay.blit(font3.render(str(psc.nom),1,(255,255,255)),(630,275))

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1 :
          if hitbox_nv_ok.rect.collidepoint(event.pos) :
            non_viable = False

  if tree_viable  :
    hitbox_v_ok = Hitboxes(120,50,705,463,100,0)
    hitbox_v_v = Hitboxes(120,50,463,463,100,0)
    gameDisplay.blit(alerte_valide,(0,0))
    gameDisplay.blit(pygame.transform.rotozoom(psc.look,0,0.35),(535,365))
    #gameDisplay.blit(hitbox_v_v.surf,hitbox_v_v)
    gameDisplay.blit((font3.render(str(psc.nom),1,(255,255,255))),(630,385))

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1 :
          if hitbox_v_ok.rect.collidepoint(event.pos) :
            tree_viable = False
          
          elif hitbox_v_v.rect.collidepoint(event.pos) :
            planete_choice = psc
            tree_viable = False
            planete_selec = True
            jouer_carte = False
            skill_tree = True
            while skill_tree :
              skill_tree_menu()


  try:
      gameDisplay.blit(pygame.transform.rotozoom(psc.look,0,0.5),(20,590))
      #gameDisplay.blit(hitbox_anti_bug.surf, hitbox_anti_bug)
  except :
      #print("Erreur esquivée")
      pass
  #gameDisplay.blit(hitbox_skill_tree.surf, hitbox_skill_tree)
  pygame.display.update()
  clock.tick(60)
  pygame.display.set_caption("fps: " + str(clock.get_fps()))

def skill_tree_menu() :
  
  global points, nb_skill, alerte_not_point, last_skill, dev_alea, cinematique, suite 
  global jouer_carte, menu, creationPlanete, planete_choice, chrono_stop, epoque ######################################################################################## ajout epoque
  chrono_stop = True

  def skill_point(hitbox,complexx):
    global points, nb_skill, alerte_not_point, epoque
    
    if hitbox.rect.collidepoint(event.pos):
      if points >= hitbox.point :
        #hitbox.surf.fill((0, 255, 0))
        if complexx == False :
          nb_skill += 1
        if complexx == True :
          nb_skill += 0.5
        points -= hitbox.point

      elif points < hitbox.point :
        alerte_not_point = True
  

  hitbox_retour = Hitboxes(170,50,1080,645,100,0)
  
  hitbox_1 = Hitboxes(142,140,565,550,30,5)
  hitbox_2 = Hitboxes(142,145,565,380,30,5)
  hitbox_3D = Hitboxes(142,145,730,380,30,5)
  hitbox_3G = Hitboxes(142,145,398,380,30,5)
  hitbox_4D = Hitboxes(142,145,900,380,30,5)
  hitbox_4G = Hitboxes(145,147,217,385,30,5)
  hitbox_5D = Hitboxes(145,135,900,210,30,5)
  hitbox_5G = Hitboxes(145,145,220,210,30,5)

  for event in pygame.event.get():
          
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
        evenement.join()
      
      elif event.type == pygame.MOUSEBUTTONUP:    
          if event.type == 6 :                        #   6 à remplacer par 1 à cause du pavé du pc portable /!\
              #print(last_skill, "nb_skill :", nb_skill)
              if (nb_skill > 3 and epoque == 0)  :                     #au cas où que je joueurs irait trop vite
                epoque = 1 
              
              
              if nb_skill == 0 :
                skill_point(hitbox_1,False)
                last_skill = ""
              if nb_skill == 1 :
                skill_point(hitbox_2,False)
                last_skill = "ADN"
              if nb_skill == 2 :
                skill_point(hitbox_3D,False)
                skill_point(hitbox_3G,True)
                last_skill = "Bactérie"
              if nb_skill == 2.5 :
                skill_point(hitbox_4G,False)
                dev_alea = 'terre'
                last_skill = 'Herbe'
              if nb_skill == 3 :
                skill_point(hitbox_4D,False)
                dev_alea = 'eau'
                last_skill = 'Organisme'
              if nb_skill == 3.5 :
                skill_point(hitbox_5G,False)
                last_skill = 'Fungus'
              if nb_skill == 4 :
                skill_point(hitbox_5D,False)
                last_skill = 'Algues'
              if nb_skill == 4.5 :
                last_skill = 'Créature fonge'
                suite = 'champi'
              if nb_skill == 5 :
                last_skill = 'Monstre marin'
                suite="homme"

              if hitbox_retour.rect.collidepoint(event.pos):
                
                if last_skill == 'Créature fonge' or last_skill == 'Monstre marin' :
                    skill_tree = False
                    cinematique = True
                    while cinematique :
                        cinema2()
                else :
                    skill_tree = False
                    jouer_carte = True
                    
                    while jouer_carte :
                      jouer()

  gameDisplay.blit(skill_tree_1,(0,0))
  gameDisplay.blit((font3.render(str(points),1,(255,255,255))),(626,5))
  gameDisplay.blit(pygame.transform.rotozoom(planete_choice.look,0,0.6),(560,190))
  #gameDisplay.blit(hitbox_retour.surf, hitbox_retour)

  if nb_skill >= 1 :
    gameDisplay.blit(ok, hitbox_1)
  if nb_skill >= 2 :
    gameDisplay.blit(ok, hitbox_2)
  
  if type(nb_skill) == int :  
    if nb_skill >= 3 :
      gameDisplay.blit(ok, hitbox_3D)
    if nb_skill >= 4 :
      gameDisplay.blit(ok, hitbox_4D)
    if nb_skill >= 5:
      gameDisplay.blit(ok, hitbox_5D)
  
  if type(nb_skill) == float :
    if nb_skill >= 2 :
      gameDisplay.blit(ok, hitbox_3G)
    if nb_skill >= 3 :
      gameDisplay.blit(ok, hitbox_4G)
    if nb_skill >= 4 :
      gameDisplay.blit(ok, hitbox_5G)


  """gameDisplay.blit(hitbox_1.surf, hitbox_1)
  gameDisplay.blit(hitbox_2.surf, hitbox_2)
  gameDisplay.blit(hitbox_3D.surf, hitbox_3D)
  gameDisplay.blit(hitbox_3G.surf, hitbox_3G)
  gameDisplay.blit(hitbox_4D.surf, hitbox_4D)
  gameDisplay.blit(hitbox_4G.surf, hitbox_4G)
  gameDisplay.blit(hitbox_5D.surf, hitbox_5D)
  gameDisplay.blit(hitbox_5G.surf, hitbox_5G)"""

  if alerte_not_point :
    hitbox_ok = Hitboxes(120,50,585,472,100,0)
    gameDisplay.blit(alerte_not,(0,0))
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1 :
          if hitbox_ok.rect.collidepoint(event.pos) :
            alerte_not_point = False

  pygame.display.update()

def chapeau():
  global menu, chrono_stop
  global points, pari, choixpo, porte_chance, alerte_not_point # au retour mettre choixpo = "none"

  hitbox_chapo1 = Hitboxes(160,300,300,195,100,0)
  hitbox_chapo2 = Hitboxes(160,300,570,195,100,0)
  hitbox_chapo3 = Hitboxes(160,300,870,195,100,0)
  hitbox_pari1 = Hitboxes(50,50,440,123,100,5)
  hitbox_pari2 = Hitboxes(50,50,620,123,100,10)
  hitbox_pari3 = Hitboxes(50,50,805,123,100,15)
  hitbox_retour = Hitboxes(170,50,1100,665,100,0)
  
  chrono_stop = True
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
    if event.type == pygame.MOUSEBUTTONUP :
      if event.button == 1 :
        
        if hitbox_retour.rect.collidepoint(event.pos):
          jouer_carte = True
          chapeaux = False
          while jouer_carte :
            jouer()

        if hitbox_chapo1.rect.collidepoint(event.pos):
          choixpo = 1
          porte_chance = random.randint(1,3)
        if hitbox_chapo2.rect.collidepoint(event.pos):
          choixpo = 2
          porte_chance = random.randint(1,3)
        if hitbox_chapo3.rect.collidepoint(event.pos):
          choixpo = 3
          porte_chance = random.randint(1,3)
        
        if hitbox_pari1.rect.collidepoint(event.pos):
          pari = 5
         
        if hitbox_pari2.rect.collidepoint(event.pos):
          pari = 10
          
        if hitbox_pari3.rect.collidepoint(event.pos):
          pari = 15
          
  
  gameDisplay.blit(background_chapo,(0,0))
  """gameDisplay.blit(hitbox_retour.surf,hitbox_retour)"""
  if choixpo == 1 :
    gameDisplay.blit(chapo_1,(0,0))
  if choixpo == 2 :
    gameDisplay.blit(chapo_2,(0,0))
  if choixpo == 3 :
    gameDisplay.blit(chapo_3,(0,0))
  if pari == 5 :
    gameDisplay.blit(star,(0,0))
  if pari == 10 :
    gameDisplay.blit(star,(175,0))
  if pari == 15 :
    gameDisplay.blit(star,(367,0))  

  if choixpo != "None" and pari != "None" :
    # ajouter hitbox_parier ici plus le collidepoint
    hitbox_parier = Hitboxes(245,53,520,590,100,0)
    gameDisplay.blit(button_parier,(0,0))
    #gameDisplay.blit(hitbox_parier.surf,hitbox_parier)
   
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP :
        if hitbox_parier.rect.collidepoint(event.pos):
          if pari > points :
            pari = "None"
            choixpo = "None"
            alerte_not_point = True
          if choixpo == porte_chance :
            try :
              points += pari
            except :
              print("points:", points, "pari :",pari,"-", type(pari))
            print("win, pari =",pari, "porte_chance :",porte_chance, "choix :", choixpo)
            choixpo = "None"
            pari = "None"
            porte_chance = "None"
          if choixpo != porte_chance :
            try :
              points -= pari
            except :
              print("points:", points, "pari :",pari,"-", type(pari))
            print("looser, pari =",pari, "porte_chance :",porte_chance, "choix :", choixpo)
            choixpo = "None"
            porte_chance = "None"
            pari = "None"
        else :
          print("block")
  if alerte_not_point :        # FAIRE DU PHOTOSHOP MODIFIER MESSAGE
    
    hitbox_ok = Hitboxes(120,50,585,472,100,0)
    gameDisplay.blit(alerte_not,(0,0))
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1 :
          if hitbox_ok.rect.collidepoint(event.pos) :
            alerte_not_point = False
            pari = "None"
            choixpo = "None"
          else :
            print("block")
  pygame.display.update()

def cinema2():
    global chrono_stop, menu, jouer_carte, skill_tree, a_cine, last_cine, nb_skill,vie_lock, epoque
    nb_skill = 0
    epoque = 2
    for event in pygame.event.get():
      #print(event) 
      
      
      #print(vie_lock)
      
      if event.type == pygame.MOUSEBUTTONUP :
        if event.button == 4 :
          last_cine = 'up'
          if a_cine < 0 :
            a_cine += 15
        
        if event.button == 5 :
          last_cine = 'down'
          if a_cine > -2900 :  
            a_cine -= 15

        if event.button == 2 :
          last_cine = 'stop'
        

      
      if event.type == pygame.QUIT:                                                        
        pygame.quit()
        quit()
   
    if a_cine < -2800 :
      cinematique = False
      jouer_carte = True
      while jouer_carte :
        jouer()

    if last_cine == 'stop' :
      a_cine += 0
    
    if last_cine == 'down' :
      if a_cine > -2900 :
        a_cine -= 1
    if last_cine == 'up' :
      if a_cine < 0 :
        a_cine += 1
    
    """if a_cine < -2080 :
      hitbox_suivant = Hitboxes(180,55,565,600,100,0)"""
    
    
    gameDisplay.blit(bg2,(0,a_cine))
    pygame.display.update()

def skill_tree_a():
    global points, nb_skill, alerte_not_point, last_skill, dev_alea, suite, ge
    global jouer_carte, menu, creationPlanete, planete_choice, chrono_stop, skill_tree_champi
    
    chrono_stop = True
    hitbox_retour = Hitboxes(170,50,1080,645,100,0)
    
    hitbox_1a = Hitboxes(125,125,25,190,100,10)
    hitbox_2a = Hitboxes(125,125,173,338,100,10)
    hitbox_3a = Hitboxes(125,125,320,192,100,10)
    hitbox_4a = Hitboxes(125,125,468,336,100,10)
    hitbox_5a = Hitboxes(125,125,615,190,100,10)
    hitbox_6a = Hitboxes(125,125,763,337,100,10)
    hitbox_7a = Hitboxes(125,125,910,193,100,10)
    
    def skill_point(hitbox):
        global points, nb_skill, alerte_not_point

        if hitbox.rect.collidepoint(event.pos):
          if points >= hitbox.point :
            #hitbox.surf.fill((0, 255, 0))

            nb_skill += 1

            points -= hitbox.point

          elif points < hitbox.point :
            alerte_not_point = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        
        if event.type == pygame.MOUSEBUTTONUP :
            if event.button == 1 :
                if hitbox_retour.rect.collidepoint(event.pos):
                 if last_skill == 'Union':
                   skill_tree = False
                   ge = True
                   while ge :
                    good_end()

                 skill_tree = False
                 jouer_carte = True
                 
                 while jouer_carte :
                   jouer()

                if nb_skill == 0 :
                    skill_point(hitbox_1a)
                if nb_skill == 1 :
                  if espece1.vieNom != 'Espece libre' : 
                    skill_point(hitbox_2a)
                    last_skill = "Boletus"
                    dev_alea = "peuple"
                if nb_skill == 2 :
                    skill_point(hitbox_3a)
                    last_skill = "Bolectius"
                if nb_skill == 3 :
                    skill_point(hitbox_4a)
                    last_skill = "Apocynae"
                    dev_alea = "guerre"
                if nb_skill == 4 :
                    skill_point(hitbox_5a)
                    last_skill = "Lignos"
                if nb_skill == 5 :
                    skill_point(hitbox_6a)
                    last_skill = "Golem"
                if nb_skill == 6 :
                    skill_point(hitbox_7a)
                    last_skill = "Titan"
                    epoque = 3
                if nb_skill == 7 :
                    last_skill = "Union"
    
    gameDisplay.blit(skill_tree_2a,(0,0))
    gameDisplay.blit((font3.render("Points: " + str(points),1,(255,150,150))),(530,665))
    
    if espece1.vieNom == 'Espece libre' :
      gameDisplay.blit(font4.render("Vous devez avoir une espéce crée.",1,(255,100,100)),(130,470))
    

    """gameDisplay.blit(hitbox_3a.surf,hitbox_6a)
    gameDisplay.blit(hitbox_3a.surf,hitbox_7a) """  
    
    if nb_skill >= 1 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_1a)
    if nb_skill >= 2 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_2a)
    if nb_skill >= 3 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_3a)
    if nb_skill >= 4 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_4a)    
    if nb_skill >= 5 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_5a) 
    if nb_skill >= 6 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_6a) 
    if nb_skill >= 7 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_7a)     
    
    if nb_skill < 7 :
        gameDisplay.blit(lock2a,(0,0))
    
    if alerte_not_point :
        hitbox_ok = Hitboxes(120,50,585,472,100,0)
        gameDisplay.blit(alerte_not,(0,0))
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 :
              if hitbox_ok.rect.collidepoint(event.pos) :
                alerte_not_point = False
    
    pygame.display.update() #case 2 : label il faut une espéce (self.vieNom = 'Espece libre')

def skill_tree_b():
    global points, nb_skill, alerte_not_point, last_skill, dev_alea, suite, ge
    global jouer_carte, menu, creationPlanete, planete_choice, chrono_stop, skill_tree_champi, epoque
    chrono_stop = True
    hitbox_retour = Hitboxes(170,50,1080,645,100,0)
    
    hitbox_1b = Hitboxes(125,125,25,190,100,10)
    hitbox_2b = Hitboxes(125,125,173,338,100,10)
    hitbox_3b = Hitboxes(125,125,320,192,100,10)
    hitbox_4b = Hitboxes(125,125,468,336,100,10)
    hitbox_5b = Hitboxes(125,125,615,190,100,10)
    hitbox_6b = Hitboxes(125,125,763,337,100,10)
    hitbox_7b = Hitboxes(125,125,910,193,100,10)
    
    def skill_point(hitbox):
        global points, nb_skill, alerte_not_point

        if hitbox.rect.collidepoint(event.pos):
          if points >= hitbox.point :
            #hitbox.surf.fill((0, 255, 0))

            nb_skill += 1

            points -= hitbox.point

          elif points < hitbox.point :
            alerte_not_point = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        
        if event.type == pygame.MOUSEBUTTONUP :
            if event.button == 1 :
                if hitbox_retour.rect.collidepoint(event.pos):
                 if last_skill == 'Science':
                   skill_tree = False
                   ge = True
                   while ge :
                    good_end()
                 
                 skill_tree = False
                 jouer_carte = True
                 
                 while jouer_carte :
                   jouer()

                if nb_skill == 0 :
                    skill_point(hitbox_1b)
                if nb_skill == 1 :
                  if espece1.vieNom != 'Espece libre' :
                    skill_point(hitbox_2b)
                    last_skill = "Salamandre"
                    dev_alea = "peuple"
                
                if nb_skill == 2 :
                    skill_point(hitbox_3b)
                    last_skill = "Jurasique"
                if nb_skill == 3 :
                    skill_point(hitbox_4b)
                    last_skill = "Lucy"
                    dev_alea = "guerre"
                if nb_skill == 4 :
                    skill_point(hitbox_5b)
                    last_skill = "Feu"
                if nb_skill == 5 :
                    skill_point(hitbox_6b)
                    last_skill = "Histoire"
                if nb_skill == 6 :
                    skill_point(hitbox_7b)
                    last_skill = "Deus Vult"
                    epoque = 3
                if nb_skill == 7 :
                    last_skill = "Science"
    
    gameDisplay.blit(skill_tree_2b,(0,0))
    gameDisplay.blit((font3.render("Points: " + str(points),1,(255,150,150))),(530,665))
    
    if espece1.vieNom == 'Espece libre' :
      gameDisplay.blit(font4.render("Vous devez avoir une espéce crée.",1,(255,100,100)),(130,470))

    """gameDisplay.blit(hitbox_3a.surf,hitbox_6a)
    gameDisplay.blit(hitbox_3a.surf,hitbox_7a) """  
    
    if nb_skill >= 1 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_1b)
    if nb_skill >= 2 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_2b)
    if nb_skill >= 3 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_3b)
    if nb_skill >= 4 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_4b)    
    if nb_skill >= 5 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_5b) 
    if nb_skill >= 6 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_6b) 
    if nb_skill >= 7 :
        gameDisplay.blit(pygame.transform.rotozoom(ok,0,0.85), hitbox_7b)     
    
    if nb_skill < 7 :
        gameDisplay.blit(lock2b,(0,0))
    
    if alerte_not_point :
        hitbox_ok = Hitboxes(120,50,585,472,100,0)
        gameDisplay.blit(alerte_not,(0,0))
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 :
              if hitbox_ok.rect.collidepoint(event.pos) :
                alerte_not_point = False
    
    pygame.display.update() #case 2 : label il faut une espéce (espece1.vieNom = 'Espece libre')

def roulette():
  global menu, a_color, dot, ruler, points, nb_skill, suite, diable, last_skill
  
  hitbox_info = Hitboxes(45,52,10,10,100,0)
  hitbox_retour = Hitboxes(170,50,1100,665,100,0)
  
  noir = (0,0,0)
  rouge = (255,0,0)
  vert = (0,255,0)
  bleu = (0,0,255)
  jaune = (255,255,0)
  cyan = (0,255,255)
  magenta = (255,0,255)
  blanc = (255,255,255)
  lg = (75,75,75)
  
  couleur_list = [blanc,noir,rouge,vert,bleu,jaune,cyan,magenta,lg]
  couleur_list_name = ["blanc","noir","rouge","vert","bleu","jaune","cyan","magenta","lg"]
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP :
      if event.button == 1 :
        
        if hitbox_retour.rect.collidepoint(event.pos):
          jouer_carte = True
          diable = False
          while jouer_carte :
            jouer()
    
    if hitbox_info.rect.collidepoint(pygame.mouse.get_pos()):
        ruler = True
    if hitbox_info.rect.collidepoint(pygame.mouse.get_pos()) == False :
        ruler = False   
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
    if event.type == pygame.KEYDOWN :
      if event.key == 274 :
        a_color = random.randint(0,7)
        print(couleur_list_name[a_color])
        
        if couleur_list_name[a_color] == 'noir' :
          if (points-5) <= 0 : 
            points -= 5
        if couleur_list_name[a_color] == 'rouge' :
          if planete_choice != 0:
            if last_skill == 'Boletus' or last_skill == 'Salamendre':
              print("déso mec")
            else :
              nb_skill += 1
        if couleur_list_name[a_color] == 'vert' :
          points = 10
        if couleur_list_name[a_color] == 'bleu' :
          if timer.sc <= 5 :
            timer.minute += 1
        if couleur_list_name[a_color] == 'jaune' :
          points += 3
        if couleur_list_name[a_color] == 'cyan' :
          if last_skill == 'Union' or last_skill == 'Science':
            if last_skill == 'Union':
              last_skill = 'Titan'
            if last_skill == 'Science' :
              last_skill = 'Deus Vult'
            nb_skill -= 1
          if planete_choice != 0 and nb_skill > 3 :
            nb_skill -= 1
        if couleur_list_name[a_color] == 'magenta' :
          if timer.sc >= 60 :
            timer.sc -= 60
            
        dot = False

    if event.type == pygame.KEYUP :
      if event.key == 274 :  
        dot = True
        a_color = 8
  
  gameDisplay.fill(0)
  gameDisplay.blit(bg_roulette,(0,0))
  pygame.draw.circle(gameDisplay, (couleur_list[a_color]), (630, 389), 227, 0)
  #gameDisplay.blit(hitbox_info.surf,hitbox_info)
  
  if dot :
    gameDisplay.blit(dotmark,(0,0))
  
  if dot == False :
    gameDisplay.blit(d_arrow,(0,0))
  
  if ruler :
    gameDisplay.blit(rules,(pygame.mouse.get_pos()))
  
  pygame.display.update()

def game_over():
  global menu

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

  
  gameDisplay.fill(0)
  gameDisplay.blit(gameover,(0,0))
  pygame.display.update()

def good_end() :
  global menu, jouer_carte,ge, suite
  
  if suite == 'Fin':
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    gameDisplay.blit(ending,(0,0))
    #gameDisplay.blit(hitbox_retour.surf,hitbox_retour)
    pygame.display.update()
  
  else:
    hitbox_retour = Hitboxes(395,85,425,545,100,0)
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.MOUSEBUTTONUP :
          if event.button == 1 :
              if hitbox_retour.rect.collidepoint(event.pos):

               ge = False
               jouer_carte = True
               
               while jouer_carte :
                 jouer()

    gameDisplay.blit(fin_tree,(0,0))
    #gameDisplay.blit(hitbox_retour.surf,hitbox_retour)
    pygame.display.update()

#Mettre tutoriel avant le menu

pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play()




tuto()
eve.start()
eve_pop.start()
timer.start()
main_menu()
eve.join()
eve_pop.join()
timer.join()

"""pygame.quit()
quit()"""
