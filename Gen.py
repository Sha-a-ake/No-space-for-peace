# Returns a blank map
def Create_Map(x,y):
    Map = []
    for i in range(y):
        Line = []
        for j in range(x):
            # Type, Passable, Transparrant, Scouted 
            n = [1,False,False,False]
            Line.append(n)
        Map.append(Line)
    return(Map)
    
def Make_Level():
    print()
            
        
