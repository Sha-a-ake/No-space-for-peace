# Returns a blank map
def Create_Map(x,y):
    Map = []
    for i in range(y):
        Line = []
        for j in range(x):
            # Type,Occupied, Passable, Transparrant, Scouted 
            n = [1,0,True,False,False]
            Line.append(n)
        Map.append(Line)
    return(Map)
    
def Make_Level():
    print()
            
        
