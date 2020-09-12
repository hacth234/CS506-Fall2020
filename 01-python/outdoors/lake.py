
def draw_lake(area = 25):
    A = area
    
    width = area**(1/2)
    width = (int) ((width * 2) // 2)
    height = width
    extraArea = area - (width**2) 
    
    for h in range(height + 1):
        stringRowLake = ""
        if (h == 0):
            for w in range(width):
                stringRowLake += " ------------ "
            print(stringRowLake)
        elif (h == 1):
            for w in range(width):
                if (w == 0):
                    stringRowLake += "(  . ~This    "
                elif (w == width - 1):
                    stringRowLake += "  . ~      ~ )"
                else:
                    stringRowLake += "  . ~     ~   "
            print(stringRowLake)
        elif (h == 2):
            for w in range(width):
                if (w == 0):
                    stringRowLake += "(     is  ~   "
                elif (w == width - 1):
                    stringRowLake += "     ~   ~   )"
                else:
                    stringRowLake += "     ~   ~    "
            print(stringRowLake)
        elif (h == 3):
            for w in range(width):
                if (w == 0):
                    stringRowLake += "(  ~   a   .  "
                elif (w == width - 1):
                    stringRowLake += "   ~       . )"
                else:
                    stringRowLake += "   ~       .  "
            print(stringRowLake)
        elif (h == 4):
            for w in range(width):
                if (w == 0):
                    stringRowLake += "(  .  Lake ~  "
                elif (w == width - 1):
                    stringRowLake += "   .       ~ )"
                else:
                    stringRowLake += "   .       ~  "
            print(stringRowLake)
        else:
            print("(", end = "")
            for w in range(width):
                if (h % 2 == 0):
                    stringRowLake += "  ~    ~   ~ "
                else:
                    stringRowLake += " ~   .    ~  "
            print(stringRowLake)
            print(")", end = "")
    print("(", end = "")
    while (extraArea > 0):
        if (height + 1 % 2 == 0):
            print("   ~ ", end = "")
        else:
            print("   ~ ", end = "")
        
        extraArea -= 1
    print(")", end = "")    
    print()
    
    
    print("                  [ No Phishing   ] ")
    print("                  [   Allowed     ] ")
    print("                          |          ")
    print("                          |          ")
    
    return