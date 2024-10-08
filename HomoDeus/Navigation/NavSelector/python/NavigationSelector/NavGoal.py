#!/usr/bin/env python3

from homodeus_library.homodeus_precomp import *
import time

class NavGoal :
    __navGoalID : int
    __name : str
    __posX : float
    __posY : float
    __posZ : float
    __objOri : float
    __creationTime : float
    __shouldStart : bool

    def __init__(self, objPosX : float, objPosY : float, objPosZ : float, objOri : float, name : str = "", shouldStart : bool = True) -> None :
        self.__posX = objPosX
        self.__posY = objPosY
        self.__posZ = objPosZ
        self.__objOri = objOri
        self.__shouldStart = shouldStart
        self.__name = name
        self.__creationTime = time.time()
        self.__navGoalID = getAndIncrementNavGoalCount()

    def __repr__(self):
        return self.__name + " : {" + \
                "PosX : " + str(self.__posX) + ", " + \
                "PosY : " + str(self.__posY) + ", " + \
                "PosZ : " + str(self.__posZ) + ", " + \
                "ObjOri : " + str(self.__objOri) + "}"

    def GetPos(self) -> Tuple[float, float, float] :
        return (self.__posX, self.__posY, self.__posZ)
        
    def GetPoint(self) -> Point :
        return Point(self.__posX, self.__posY, self.__posZ)
        
    def GetOriScalar(self) -> float :
        return self.__objOri

    def GetOri(self) -> Quaternion :
        return Quaternion(0, 0, sin(self.__objOri * 0.5), cos(self.__objOri * 0.5))

    def GetPose(self) -> Tuple[Point,Quaternion] :
        return (self.GetPoint(),self.GetOri())
    
    def GetCreationTime(self) -> float :
        return self.__creationTime
    
    def GetNavGoalExistenceTime(self) -> float :
        return time.time() - self.__creationTime

    def GetNavGoalID(self) -> int :
        return self.__navGoalID
    
    def GetName(self) -> str :
        return self.__name
    
    def BlockNavGoal(self) -> None :
        self.__shouldStart = False

    def UnblockNavGoal(self) -> None :
        self.__shouldStart = True

    def IsBlocked(self) -> bool :
        return not self.__shouldStart
    
    def SetID(self, id : int ) -> None :
        self.__navGoalID = id