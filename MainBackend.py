import Backend
import time
import cv2
import csv
import numpy as np
import os
from config import *

def FindPath(SP, EP):
    Detail = ''
    RoomFile = Room

    def MPNodeToCoord(NodeIndex):
        CoordList.append(DT.NodeToCoord(NodeList[NodeIndex]))

    def SavePath(Name, PathImg):
        cv2.imwrite(f'ToDrawMap/{Name}.jpg', PathImg)

    if (SP.upper() == EP.upper()):

        StartTime = time.time()

        PointCoord = DT.NodeToCoord(DT.NameToNode(SP.upper()))
        print(PointCoord)

        CoordList = [PointCoord]
        FlagImage = cv2.imread('Items/flag.png', -1)
        Drawing = Backend.Draw(GlobalImage.copy(), CoordList, (0,0,0), True, (0,0,0))
        Image = Drawing.AddFlag(Image, FlagImage, PointCoord[1], PointCoord[0], 0.045)
        
        cv2.imwrite('ToDrawMap/Path.jpg', Image)

        print('DONE')
        print('')

        print(f'--------------- {time.time() - StartTime} seconds ---------------')

        return Image
    
    
    if (f"{SP.upper()}_{EP.upper()}.csv" in os.listdir("cache")):
        StartTime = time.time()

        print("Found in cache")

        with open(f"cache/{SP.upper()}_{EP.upper()}.csv") as FileIn:
            csvReader = csv.reader(FileIn)
            CoordList = [[int(row[0]), int(row[1])] for row in csvReader]

        Ind = DT.GetIndex(RoomFile["Name"], EP.upper())

        if (Ind != -1):
            print("In Room file")
            if (type(RoomFile["Describe"][Ind]) == str or type(RoomFile["Describe"][Ind]) == chr):
                print("Have describe")
                Detail = RoomFile["Label"][Ind] + " - " + RoomFile["Describe"][Ind]
            else:
                print("No describe")
                Detail = RoomFile["Label"][Ind]
            print(Detail)
        else:
            print(EP.upper(), " Not in Room file")

        Drawing = Backend.Draw(GlobalImage.copy(), CoordList, LineColor, True, MarkColor)
        Image = Drawing.Path()

        SavePath("Path", Image)
            
        print('DONE IN CACHE')
        print('')

        print(f'--------------- {time.time() - StartTime} seconds ---------------')

        return Image, Detail

    StartTime = time.time()

    SN = DT.NameToNode(SP.upper())
    if (SN == -1):
        print(f"{SP} is not the right place name.")
        return -1

    EN = DT.NameToNode(EP.upper())
    if (EN == -1):
        print(f"{EP} is not the right place name.")
        return -1

    NodeList = Al.AStar(SN, EN)
    
    Ind = DT.GetIndex(RoomFile["Name"], EP.upper())

    if (Ind != -1):
        print("In Room file")
        if (type(RoomFile["Describe"][Ind]) == str or type(RoomFile["Describe"][Ind]) == chr):
            print("Have describe")
            Detail = RoomFile["Label"][Ind] + " - " + RoomFile["Describe"][Ind]
        else:
            print("No describe")
            Detail = RoomFile["Label"][Ind]
        print(Detail)
    else:
        print("Not in Room file")

    if (NodeList == -1):
        print("Some error occured, try again")
        return -1
 
    CoordList = [DT.NodeToCoord(NodeInList) for NodeInList in NodeList]
        
    Drawing = Backend.Draw(GlobalImage.copy(), CoordList, LineColor, True, MarkColor)
    Image = Drawing.Path()

    SavePath("Path",Image)

    with open(f"cache/{SP.upper()}_{EP.upper()}.csv", "w", newline="") as FileOut:
        csv.writer(FileOut).writerows(CoordList)
        
    print('DONE')
    print('')

    print(f'--------------- {time.time() - StartTime} seconds ---------------')

    return Image, Detail


def UploadGetLink(FileName, SP, EP):
    DB = Backend.Internet(FileName)
    QrImage = DB.Upload(SP, EP)

    QrImage.save("QrCode.jpg")

    return QrImage


#------ TEST AREA ------



# ---------- FIND PATH BY TYPING ------------

# if __name__ == '__main__':

# 000000



#------- FAIL DETECTION --------

# ProcessCount = 0
# Name = pd.read_csv("NameAndNodes.csv");
# for i in range(len(Name["Name"])):
#     SP = Name["Name"][i]
#     for j in range(i):
#         if (i == j): continue
#         EP = Name["Name"][j]
#         ProcessCount += 1
#         if ProcessCount <= 5:
#             mp1 = mp.Process(target = FindPath, args = (SP, EP))
#             mp1.start()
#         else:
#             mp1.join()
#             mp1 = mp.Process(target = FindPath, args = (SP, EP))
#             mp1.start()
#             ProcessCount = 0
#         # ReturnVal = FindPath(SP, EP)
        # if (ReturnVal == -1):
        #     print(f"Failed to find path from {SP} to {EP}")
# mp1.join()

#---------- NORMAL TEST -----------

# Signal = "y"

# while(Signal == 'y' or Signal == 'Y'):
#     SP = input("Start place: ")
#     EP = input("End place: ")

#     ReturnVal = FindPath(SP, EP)

#     try:
#         if (ReturnVal == -1):
#             print("Error occured, try again")
#             continue
#     except:
#         pass

#     Post = input("Upload image ? y, n \n")

#     if (Post == 'y' or Post == 'Y'):
#         UploadGetLink("ToDrawMap/Path.jpg" ,SP, EP)

#     Signal = input("Signal: y, n \n")

    #------- FAIL DETECTION --------

    # ProcessCount = 0
    # Name = pd.read_csv("NameAndNodes.csv");
    # for i in range(len(Name["Name"])):
    #     SP = Name["Name"][i]
    #     for j in range(i):
    #         if (i == j): continue
    #         EP = Name["Name"][j]
    #         ProcessCount += 1
    #         if ProcessCount <= 5:
    #             mp1 = mp.Process(target = FindPath, args = (SP, EP))
    #             mp1.start()
    #         else:
    #             mp1.join()
    #             mp1 = mp.Process(target = FindPath, args = (SP, EP))
    #             mp1.start()
    #             ProcessCount = 0
    #         # ReturnVal = FindPath(SP, EP)
            # if (ReturnVal == -1):
            #     print(f"Failed to find path from {SP} to {EP}")  
    # mp1.join()
