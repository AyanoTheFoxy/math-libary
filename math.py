# basic operations with numbers floats
def Add(numb1: float, numb2: float) -> float:
    return numb1 + numb2
    
def Sub(numb1: float, numb2: float) -> float:
    return numb1 - numb2
    
def Mul(numb1: float, numb2: float) -> float:
    return numb1 * numb2
    
def Div(numb1: float, numb2: float) -> float:
    return numb1 / numb2

def Pot(base: float, exponent: float) -> float:
    return base ** exponent
    
def Percent(percent: float, numb: float) -> float:
    return round(percent % numb, 1)
    
# opetrations complex with nembers floats
def Root(rooting: float, index: float = 2) -> float:
    return rooting ** (1 / index)

def Log(log: float, base: float = 2) -> float:
    x = 0
    while base ** x < log:
        x += 0.1
        if base ** x >= log:
            return round(x, 2)
    
def Sqdeq(a: float, b: float, c: float) -> float:
    d = b ** 2 - 4 * a * c
    x1 = (-b - Root(d)) / (2 * a)
    x2 = (-b + Root(d)) / (2 * a)
    return x1, x2

# positions
def Cmfr(r: int) -> int:
    return round(2 * 3.14 * r, 0)
    
def Lerp(s0: int, s1: int, alph: int) -> int:
    if alph > 1:
        alph = 1
    return s0 + (s1 - s0) * alph

def Vect2(x: int = 0, y: int = 0) -> int:
        pos = [x, y]
        return pos

def Vect3(x: int = 0, y: int = 0, z: int = 0) -> int:
        pos = [x, y, z]
        return pos

class Area:   
    def Square(x: int, y: int, w: int, h: int) -> int:
        area = [x, y, w, h]
        return area
    
    def Triangle(x: int, y: int, w: int, h: int) -> int:
        w / 2
        h / 2
        x * 1.5
        y * 2
        area = [x, y, h, w]
        return 
    
    def Cricle(x: int, y: int, w: int, h : int) -> int:
        w / 1.25 
        h / 1.25
        x * 1.25
        y * 1.25
        area = [x, y, h, w]
        return area
    
# conversion
# pixels
class Pixels:
    def PtToPx(pt: float) -> float:
        px = pt * .75
        return px
    def EmToPx(em: float) -> float:
        px = em / 16
        return px
    def InToPx(In: float) -> float:
        px = In * 120
        return px
    def MmToaPx(mm: float) -> float:
        px = mm * 3.7795280352161
        return px
    
# time
class time:
    def HToM(hour: float) -> float:
        return hour * 60
        
    def HToS(hour: float) -> float:
        return hour * 3600
        
    def MToS(minute: float) -> float:
        return minute * 60
        
    def MToH(minute: float) -> float:
        return minute / 60
        
    def SToM(sec: float) -> float:
        return sec / 60
        
    def SToH(sec: float) -> float:
        return sec / 3600
        
# temp
class Temp:
    def CToK(c: float) -> float:
        return c + 273.15
    
    def CToF(c: float) -> float:
        return (c * 9 / 5) + 32

    def FToC(f: float) -> float:
        return (f - 32) * 5 / 9
    
    def FToK(f: float) -> float:
        return (f - 32) * 5 / 9 + 273.15
   
    def KToF(k: float) -> float:
        return (k - 273.15) * 9 / 5 + 32
    
    def KToC(k: float) -> float:
        return k - 273.15
    
