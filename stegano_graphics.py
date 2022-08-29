import tkinter as tk

root= tk.Tk()            

canvas1 = tk.Canvas(root, width = 400, height = 10000,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='WELCOME TO STEGANOGRAPHY ')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='enter the message to be encrypted:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)
import random as r
def stegano():
 A=["Atharva","Absorb","Abiotic","Anand","Above","Buddha","Chacha","Data","Extrema"]
 B=["Buddha","Bomb","Benthic","Bend","Benzene","Lamb","Thumb","Vocab","Web","Curb"]
 C=["Chacha","Chub","Cyclic","cried","Cheque","Topic","Sonic","Workoholivc","Zinc","Specific"]
 D=["Data","Dumb","Dynamic","Dead","Duke","Squad","Mad","Trend","Yard","Weird"]
 E=["Extrema","Earbob","Erotic","Endead","Eagle","Quote","Xylene","Eagle","Wiggle","Vibe"]
 F=["Facula","Forb","Fabric","Friend","Free","Relief","Roof","Half","Puff","Thief"]
 G=["Gamma","Grab","Galectic","Grind","Genre","Voting","Using","Tag","Willing","Young"]
 H=["Honda","Herb","Havoc","Hired","Horse","Photograph","Vanish","Witch","Smooth","Growth"]
 I=["India","Intomb","Ironic","Island","Ignore","Illuminati","Agami","Bronchi","Chili","Deci","Emboli"]
 J=["Jambia","Jibb","Jurassic","Jammed","Jasmine","Jorj","Prithviraj","Hajj","Viraj","Swaraj"]
 K=["Koala","Kab","Karmic","Kid","Knee","Crook","Cook","Mark","Stark","Stock"]
 L=["Libra","Lamb","Lilac","Lied","Lion","Small","Seal","Dell","Drill","Sell"]
 M=["Mega","Mob","Mac","Med","Mole","Arm","Buxom","Conform","Decom","Exam"]
 N=["Ninja","Numb","Nostoc","Nod","Nine","Chain","Train","Brain","Ukrain","Ten"]
 O=["Orchestra","Overdub","Optic","Old","Ore","Virgo","Marco","Hello","Ammo","Who"]
 P=["Pizza","Pub","Plastic","Piked","Plate","Atrip","Zip","Trap","Xylocarp","Yep"]
 Q=["Quota","Quadratic","Quad","Quote","Quiff","Abraq","Bloaq","Saoq","Traq","Farooq"]
 R=["Rima","Rehab","Rhodic","Red","Race","Door","Car","Far","Roar","Tear"]
 S=["Sea","Sab","Specific","Squad","Square","Fuss","Zeros","Yes","Sandals","Vowels"]
 T=["Tata","Thumb","Topic","Trend","Technique","Theif","Craft","Dart","Cart","Smart","Cot"]
 U=["Ultra","Uncurb","Unrythmic","Unbaked","Use","Tapu","You","Zebu","Ragu","Vermoulu"]
 V=["Visa","Vocab","Volumetric","Valid","Vibe","Perv","Shiv","Maglev","halierov","Gaurav"]
 W=["Wakanda","Web","Workaholic","Weird","Wiggle","Grow","Draw","Slow","Flow","New"]
 X=["Xenophobia","Xenic","Xyloid","Xylene","Xeroxing","Relax","Epex","Flex","Box","Max"]
 Y=["Yoga","Yob","Yonic","Yard","Yodle","Appy","Boy","Chevvy","Dolby","Early"]
 Z=["Zebra","Zineb","Zinc","Zipped","Zone","Buzz","Fizz","Cuz","Ditz","Wiz"]
 symbol=["!","@","#","$","%","^","&","*","(",")","_","+","/"]
 
 x1 =str(entry1.get())
 x1=x1.lower()

    
   

 for i in x1:
    if (i==" "):
        print(r.choice(symbol),end=" ")
    elif (i=="."):
        print(",",end=" ")
    elif (i=="a"):
        print(r.choice(A),end=" ")
    elif (i=="b"):
        print(r.choice(B),end=" ")
    elif (i=="c"):
        print(r.choice(C),end=" ")
    elif (i=="d"):
        print(r.choice(D),end=" ")
    elif (i=="e"):
        print(r.choice(E),end=" ")
    elif (i=="f"):
        print(r.choice(F),end=" ")
    elif (i=="g"):
        print(r.choice(G),end=" ")
    elif (i=="h"):
        print(r.choice(H),end=" ")
    elif (i=="i"):
        print(r.choice(I),end=" ")
    elif (i=="j"):
        print(r.choice(J),end=" ")
    elif (i=="k"):
        print(r.choice(K),end=" ")
    elif (i=="l"):
        print(r.choice(L),end=" ")
    elif (i=="m"):
        print(r.choice(M),end=" ")
    elif (i=="n"):
        print(r.choice(N),end=" ")
    elif (i=="o"):
        print(r.choice(O),end=" ")
    elif (i=="p"):
        print(r.choice(P),end=" ")
    elif (i=="q"):
        print(r.choice(Q),end=" ")
    elif (i=="r"):
        print(r.choice(R),end=" ")
    elif (i=="s"):
        print(r.choice(S),end=" ")
    elif (i=="t"):
        print(r.choice(T),end=" ")
    elif (i=="u"):
        print(r.choice(U),end=" ")
    elif (i=="v"):
        print(r.choice(V),end=" ")
    elif (i=="w"):
        print(r.choice(W),end=" ")
    elif (i=="x"):
        print(r.choice(X),end=" ")
    elif (i=="y"):
        print(r.choice(Y),end=" ")
    elif (i=="z"):
        print(r.choice(Z),end=" ")

    
   
    
    
    label3 = tk.Label(root, text= 'the steganography of these messsage  ' + ' is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    
    label4 = tk.Label(root ,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='get the data', command=stegano, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
