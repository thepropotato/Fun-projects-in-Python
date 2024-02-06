def doflames() :
    
    print("\nEnter the names")
    
    name1 = input("\nNee peru : ")
    name = name1
    
    while len(name1) == 0:
        print("Nenu maree antha edhava la kanapaduthunnana ? Peru cheppara munda")
        name1 = input("Peru cheppara pookay : ")
        
    name2 = input("Evaritho flames cheyali : ")
    
    while len(name2) == 0:
        print("Nenu maree antha edhava la kanapaduthunnana ? Peru cheppara munda")
        name2 = input("Crush peru cheppara pookay : ")
    
    name1 = name1.lower()
    name2 = name2.lower()
    
    length = len(name1) + len(name2)
    
    flames = "flames"
    
    for i in name1 :
        for j in name2 :
            if i == j :
                length = length - 2
    
    dif = length
    
    while dif > len(flames):
        if dif > 0 :
            dif = dif - len(flames)
            
    letter = flames[dif-1]
    
    print("")
    
    if length != 0:
        if letter == flames[0] :
            print("Meeru FRIENDS ra zumpka")
        elif letter == flames[1]:
            print("Ahhaaaa",name,"LOVE vachindhi ga. Enjaayyy pandagooowwwww")
        elif letter == flames[2]:
            print("AFFECTION vachindhi, inka themgey")
        elif letter == flames[3] :
            print("ok google !, play PELLI kala vachesindhe bala.mp3")
        elif letter == flames[4]:
            print("broooo, meeru edhuru padinappudu erra ga mande suryudu nallabadipothadu. ardham kaledha ? ENEMIES ra munda")
        elif letter == flames[5]:
            print("ayindha, baga ayindha. flamesooo flamesoo ani egirav. SISTER ni baga choosko inka")

    
doflames()

    