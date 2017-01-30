# Returns a blank map
def Create_Map(x,y):
    Map = []
    for i in range(x):
        Line = []
        for j in range(y):
            # Type,Occupied, Passable, Transparrant, Scouted 
            n = [1,0,True,False,False]
            Line.append(n)
        Map.append(Line)
    return(Map)
    
def Make_Level():
    print()
            
        
