import Config as C



def Create_Map(x,y):
    
    C.TileMap = []
    C.WalkMap = []
    C.IdMap = []
    for i in range(x):
        Line = []
        TileLine = []
        PathLine = []
        IdLine = []
        for j in range(y):
            
            """
            Type status:
            
            0 == Floor
            
            11 == Horizontal Wall Top
            12 == Horizontal Wall Bottom
            21 == Vertical Wall Left
            22 == Vertical Wall Right
            
            31 == Top Left Corner
            32 == Top Right Corner
            41 == Bottom Left Corner
            42 == Bottom Right Corner
            
            51 == Special Vertical Wall Left
            52 == Special Vertical Wall Right
            61 == Special Horizontal Wall Top
            62 == Special Horizontal Wall Bottom
            
            """

            '''
            WalkMap = 0 == пустой тайл
            WalkMap = 1 == занятый тайл 
            WalkMap = 2 == стена
            '''
                
            TileLine.append(0)
            PathLine.append(0)
            IdLine.append(0)
        C.TileMap.append(TileLine)
        C.WalkMap.append(PathLine)
        C.IdMap.append(IdLine)

    for i in range(x):
        for j in range(y):
            if i == x-1 or j == 0 or j == y-1 or i == 0:
                C.TileMap[i][j] = 21
                C.WalkMap[i][j] = 2
                C.IdMap[i][j] = 2
                
                
