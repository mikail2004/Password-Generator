import random
import eel

eel.init('web')
running = True

lowcap = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
highcap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            
@eel.expose
def button():
    n1 = random.randrange(1099, 2199)
    n2 = random.randrange(0, 21)
    w1 = random.choice(lowcap)
    w2 = random.choice(highcap)
    passWORD = (w1 + w1 + str(n1) + w1 + str(n2) + w2)
    print(passWORD)
    eel.printGreeting(passWORD)
    return passWORD

eel.start('index.html', size=(1000,500))
        
