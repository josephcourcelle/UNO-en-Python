
from random import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
liste_cartes = []
pioche = []
couleur = 0
periode = "pioche"
flag2=0
n=0
liste_totale = []
tas = []
liste_joueurs=[]
flag5= 0
playtimes=0
realplaytimes=0
flag7=0
p2=0
p4=0
sens=1
couleurs_fr=["jaune","vert","rouge","bleu","noir"]
couleurs_en=["yellow","green","red","blue","black"]
mots_titre = ["Super","UNO","Flash","2000"]
x=32









#fenetre entre 2 joueurs#
def fen_attente (ID):
    fen_att = Tk()
    texte = ("Passez le Pc à " + liste_totale[ID][0][0])
    label_nom = Label(fen_att , text = texte , font = "impact 48").grid(row = 0 , pady = 40 , padx = 40)
    bout_fermer = Button(fen_att , text = "OK !" , font = "impact 36" , command = fen_att.destroy).grid(row = 1, padx = 20)
    fen_att.mainloop()
def contre_possible(ID , carte):
    if ((apioche == False )and ((tas [0][0]=="plus 4") or (tas [0][0] == "plus 2"))) and (action_secondaire[0] != "pioche"):
        if liste_totale[ID][1][carte][0] == tas[0][0] :
            return "normal"
        else : return "disabled"
    else : return "normal"
def liste_jouable (ID):
    global liste_totale
    a=0
    liste = []
    for i in range (0 , len(liste_totale[ID][1])-1):
        if placement_possible(ID , i):
            liste.append(i)
    return liste
def nom_random ():
    global ma_var
    global select_nom
    liste_prenoms = ["Jean-" , "Pierre-" , "Etienne-" , "Claude-" ]
    liste_noms = ["Jean" , "Pierre" , "Lorenzo", "Oumar", "Denis", "Etienne" , "Claude" , "xavier" ,"Edward","batou","Triki" , "Jeanjean"]
    c = randint (0,1)
    a = randint(0,len(liste_prenoms)-1)
    b= randint(0,len(liste_noms)-1)
    while a == b :
        b= randint(0,len(liste_noms)-1)
    if c == 0:
        ma_var.set(liste_prenoms[a]+liste_noms[b])
    else : ma_var.set(liste_noms[b])
    return (liste_prenoms[a]+liste_noms[b])
################
#fenetre de jeu#
def aficher(ID):
    global fenetre
    global apioche
    fenetre=Tk()
    nom_graph = Label(fenetre, text=(liste_totale[ID_jeu][0]), font = "arial 20 bold").pack()
    #on change les couleurs et les lettres pour une lecture plus agréable
    frame_tas = LabelFrame(fenetre, text="Le tas", padx=10, pady=10)
    boutontas=Button(frame_tas, text=(mot_adapt(tas[0][0])),bg=language_adapt(tas[0][1]),fg=fg_adapter(tas[0][1]), borderwidth=1,font= "arial 20 bold")
    frame_paquet = LabelFrame(fenetre, text="Votre main", padx=10, pady=10)
    
    for ligne in range(1):
        for colonne in range(len(liste_totale[ID][1])):
            boutas = Button(frame_paquet,command = lambda colonne=colonne:clic(colonne),  state = contre_possible(ID_jeu , colonne), text=(mot_adapt(liste_totale[ID][1][colonne][0])),bg=language_adapt(liste_totale[ID][1][colonne][1]),fg=fg_adapter(liste_totale[ID][1][colonne][1]), borderwidth=1,font= "arial 20 bold").grid(row=ligne, column=colonne)
        if apioche == False :
            bou_pioche = Button(frame_paquet, text="Piocher" , font = "arial 20 bold" , command = graph_piocher).grid(row=ligne, column=colonne+1)
        else :
            bou_fin = Button(frame_paquet, text="Terminer le tour" , font = "arial 20 bold" , command = graph_piocher).grid(row=ligne, column=colonne+1)
    boutontas.pack()
    frame_tas.pack()
    frame_paquet.pack(padx=20,pady=20)
    fenetre.mainloop()
    

def graph_fin_tour():
    global ajoué
    ajoué = True
    fenetre.quit
    fenetre.destroy
def clic (ID):
    if not jouer(ID_jeu,ID):
        texte = "on joue pas un " + str(liste_totale[ID_jeu][1][ID][0]) + " " + str(liste_totale[ID_jeu][1][ID][1]) + " sur un " + str(tas[0][0]) + " "+ str(tas [0][1]) + " !"
        showerror('Hé ta cru quoi ?', texte )
        print("pas possible !")
    else :
        fenetre.quit()
        fenetre.destroy()
def graph_piocher():
    global p2
    global p4
    global apioche
    global ajoué
    global action_secondaire
    if apioche == True :
        ajoué = True
        action_secondaire = ["pioche" , "pioche"]
        fenetre.quit()
        fenetre.destroy()
    elif p2 != 0:
        action_secondaire = ["pioche" , "pioche"]
        piocher(ID_jeu,2*p2)
        p2=0
        apioche = True
        fenetre.quit()
        fenetre.destroy()
    elif p4 != 0:
        action_secondaire = ["pioche" , "pioche"]
        piocher(ID_jeu,4*p4)
        p4=0
        apioche = True
        fenetre.quit()
        fenetre.destroy()
    else :
        apioche = True
        piocher(ID_jeu,1)
        fenetre.quit()
        fenetre.destroy()


def voir_tas ():
    print ("un" , tas[0][0] , tas[0][1] , "est sur le haut du tas")
    return tas[0]

def placement_possible(ID_joueur,ID_carte):
    return (tas[0][0]==liste_totale[ID_joueur][1][ID_carte][0]) or (tas[0][1]==liste_totale[ID_joueur][1][ID_carte][1]) or (liste_totale[ID_joueur][1][ID_carte][1]=="noir")

def clean (b):
    a = 0
    while a<b :
        print (" ")
        a+=1
def piocher (ID , n):
    flag3 = 0
    while flag3 < n :
        liste_totale[ID][1].append(pioche[0])
        del pioche[0]
        flag3+=1
def language_adapt (couleur):
    return couleurs_en[couleurs_fr.index(couleur)]
def fg_adapter (couleur):
    if couleur == "jaune" :
        return "black"
    else :
        return "white"
def mot_adapt (mot):
    if (mot=="passe ton tour"): return "Ø"
    elif (mot=="jk"): return "J"
    elif (mot=="change de sens"): return "⇔"
    elif (mot=="plus 2"): return "+2"
    elif (mot=="plus 4"): return "+4"
    else : return mot
    
def couleur_dominante(ID):
    global dico
    dico = {"vert":0 , "rouge":0 , "bleu":0 , "jaune":0}
    for i in liste_totale[ID][1] :
        if i[1] != "noir" :
            dico[i[1]]+=1
    a = ["noir" , 0]
    for i in couleurs_fr :
        if i != "noir":
            if dico[i] >= a[1]:
                a=[i,dico[i]]
    return a[0]
def voir_main (ID):
    useless = input ("appuyez pour voir vos cartes")
    flag4 = 0
    while flag4<len(liste_totale[ID][1]) :
        print (flag4 ,"-->", liste_totale[ID][1][flag4][0], liste_totale[ID][1][flag4][1])
        flag4 +=1
def jouer (ID_joueur , ID_carte) :
    global ajoué
    global action_secondaire
    if placement_possible(ID_joueur,ID_carte) :
        if (liste_totale[ID_joueur][1][ID_carte][1])=="noir":
            if liste_totale[ID_joueur][2][0]==0 :
                flag9=input("choisissez une couleur")
            else:
                flag9 = couleur_dominante(ID_joueur)
            if not flag9 in liste_couleurs :
                return False
            else:
                action_secondaire=(liste_totale[ID_joueur][1][ID_carte])
                tas.insert (0,(liste_totale[ID_joueur][1][ID_carte]))
                tas[0][1]=flag9
                del (liste_totale[ID_joueur][1][ID_carte])
                ajoué = True
                return True
        else:
            action_secondaire=(liste_totale[ID_joueur][1][ID_carte])
            tas.insert (0,(liste_totale[ID_joueur][1][ID_carte]))
            del (liste_totale[ID_joueur][1][ID_carte])
            ajoué = True
        return True
    else :
        print ("placement impossible")
        return False
def periscope ():
    flag6 = 0
    while flag6<len(liste_totale) :
        print (str(liste_totale[flag6][0][0])+"-->"+ str(len(liste_totale[flag6][1])))
        flag6+=1

def recup_n_joueurs ():
    global n_joueurs
    n_joueurs = int(s.get())
    root.destroy()
def recup_nom (n):
    global nompartiel
    global mode
    mode = n
    nompartiel = str(entr.get())
    select_nom.destroy()


                        ###################################
                        # On lance le brassage des cartes #
                        ###################################
liste_couleurs = ["bleu","rouge","vert","jaune"]
while couleur!=4 :
    #le 0 n'est présent qu'une fois par couleur, on va l'insérer
    liste_cartes.append ([0,liste_couleurs[(couleur)]])
    rounde = 0
    #beaucoup de cartes sont présentes en 2 exemplaires, je vais donc doubler ma methode de rajout
    while rounde <2 :
        numero = 1
        while numero <10 :
            liste_cartes.append ([(numero) , liste_couleurs[(couleur)]])
            numero=numero+1
        #on va rajouter les cartes semi spéciales (1 par round donc 2)
        #d'abord les cartes +2 nomées p2
        liste_cartes.append (["plus 2" , liste_couleurs[(couleur)]])
        #puis les passe tour nomées "pt"
        liste_cartes.append (["passe ton tour" , liste_couleurs[(couleur)]])
        #enfin les change de sens nomées "cs"
        liste_cartes.append (["change de sens" , liste_couleurs[(couleur)]])
        rounde+=1
    #les cartes +4 et couleurs sont présente à raison de 4 chaqu'une, soit un par couleur
    #on va rajouter 4 cartes +4 nomées "p4"
    liste_cartes.append (["plus 4" , "noir"])
    #puis les jokers només "jk"
    liste_cartes.append (["jk" , "noir"])
    couleur+=1
while len(liste_cartes)>1 :
    flag=randint(1 , (len(liste_cartes)-1))
    pioche.append(liste_cartes[flag])
    del liste_cartes[flag]
                        ###############################
                        # On fait piocher les joueurs #
                        ###############################

root = Tk()
for colonne in range (4):
    label_bvn=Label(root , text=mots_titre[colonne] , font = "Barbatrick 48" , fg = couleurs_en[colonne] , bg=couleurs_en[(colonne+1)%4]).grid(sticky = "nesw" , row=1, column=colonne,ipadx=40, padx=0, pady = 0)
label_choix=Label(root , text="combien de joueurs ?" , font = "Barbatrick 48" , fg = couleurs_en[colonne] , bg="yellow").grid(row=2, column=0, padx=0, pady = 0 , columnspan=3 , ipadx=40)
s = Spinbox(root , from_=2 , to=9, fg="yellow", bg = "green" , font = "Barbatrick 48",width="5")
s.grid(row=2, column=3,ipadx=0)
jouer_bouton = Button(root, text="jouer !" , command = recup_n_joueurs , font = "Barbatrick 128" , width = 8 ,fg="red" , bg="blue").grid(row=3, column=0 , columnspan=4 , pady=0, sticky = "nesw" )
root.mainloop()
flag5= 0
while n_joueurs>flag5 :
    nompartiel = ""
    flag5+=1
    while nompartiel == "":
         select_nom = Tk()
         texte1="joueur " + str(flag5) + " : "
         ma_var = StringVar()
         ma_var.set("")
         lab = Label(select_nom , text = texte1 , font = "impact 48").grid(column = 0, row=0 , rowspan = 2)
         entr = Entry(select_nom,textvariable= ma_var, font = "impact 36",width=20)
         entr.grid(column = 1,row=0 , rowspan = 2)
         vals = ['player', 'ia_random']
         etiqs = ['Joueur', 'IA Imprévisible']
         varGr = StringVar()
         varGr.set(vals[1])
         for i in range(2):
             b = Button(select_nom, text=etiqs[i], command = lambda i=i:recup_nom(i))
             b.grid(column = 2 , row = (i) , sticky='nesw')
         bouton_valider = Button(select_nom,text="valider" , command = recup_nom)
         bouton_valider.grid(column=0,row=2,columnspan=2 ,sticky='nesw')
         bonton_random = Button(select_nom , text = "Nom au hasard" , command = nom_random).grid(row = 2 , column = 2 , sticky='nesw')
         select_nom.mainloop()
         if nompartiel != "": 
            liste_totale.append([[nompartiel],[],[mode]])
        
tas.append(pioche[0])
del pioche[0]
while flag7<len(liste_totale):
    piocher(flag7,7)
    flag7+=1
periode = 0


                        ###########################
                        # On commence le playtime #
                        ###########################
while periode <= 1000:
    ID_jeu=playtimes%len(liste_totale)
    voir_main(ID_jeu)
    apioche = False
    ajoué=False
    aposé=False
    if liste_totale[ID_jeu][2][0]==0:
        fen_attente (ID_jeu)
        while ajoué == False:
            aficher(ID_jeu)
        #gestion des plus 2
        if (action_secondaire[0]=="plus 2"):
            p2+=1
        #gestion des plus 4
        if (action_secondaire[0]=="plus 4"):
            p4+=1
        if (action_secondaire[0]=="change de sens"):
            sens=sens*(-1)
        if (action_secondaire[0]=="passe ton tour"):
            playtimes+=sens
    else :
        if len(liste_jouable (ID_jeu)) == 0 :
            piocher(ID_jeu , 1)
        else :
            jouer(ID_jeu , liste_jouable(ID_jeu)[0])
        if (action_secondaire[0]=="plus 2"):
            p2+=1
        #gestion des plus 4
        if (action_secondaire[0]=="plus 4"):
            p4+=1
        if (action_secondaire[0]=="change de sens"):
            sens=sens*(-1)
        if (action_secondaire[0]=="passe ton tour"):
            playtimes+=sens
    if len(pioche)==0 :
        while len(tas)>=2:
            pioche.append(tas.pop(1))
            shuffle (pioche)
    if aposé == False : print ("pioché")
    else : print(action_secondaire)
    playtimes+=sens
    realplaytimes+=1
    periode +=1
