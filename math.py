#operations
class operations:
    def root( r: float, i: float = 2, e: float = 1) -> float:
        return r ** (e / i)
    
    def log( l: float, b: float = 2) -> float:
        x = 0
        while b ** x < l:
            x += 0.1
            if b ** x >= l:
                return round( x, 2)
    
    def Sqdeq( a: float, b: float, c: float) -> float:
        d = b ** 2 - 4 * a * c
        x1 = (-b - operations.root(d)) / (2 * a)
        x2 = (-b + operations.root(d)) / (2 * a)
        return x1, x2

#positions
class pos:
    def vect2d( x: int = 0, y: int = 0) -> int:
        return pos = [ x, y]
    
    def vect3d( x: int = 0, y: int = 0) -> int:
        return pos = [ x, y]
    
    def lerp ( s0: int, s1: int, a: int = .5) -> int:
        if a > 1:
            a = 1
        return s0 + (s1 - s0) * a

class area:
    def square( x: int, y: int, w: int, h: int) -> int:
        return area = [ x, y, w, h]
    
    def triangle( x: int, y: int, w: int, h: int) -> int:
        return area = [ x * 1.5, y * 2, w / 1.5, h / 2]
    
    def cricle( x: int, y: int, w: int, h : int) -> int:
        return area = [ x * 1.25, y * 1.25, w / 1.25, h / 1.25]
    
    def cmfr(r: int) -> int:
        return 2 * 3.14159265358979323846 * r
    
#conversion
class conversions:
    #pixels
    class pixels:
        def ptToPx(pt: float) -> float:
        return pt * .75
    
        def emToPx(em: float) -> float:
            return em / 16
    
        def inToPx(In: float) -> float:
            return In * 120
    
        def mmToaPx(mm: float) -> float:
            return mm * 3.7795280352161
    
    #time
    class time:
        def mToM(h: float) -> float:
            return hour * 60
        
        def hToS(h: float) -> float:
            return h * 3600
        
        def mToS(m: float) -> float:
            return m * 60
        
        def mToH(m: float) -> float:
            return m / 60
        
        def sToM(s: float) -> float:
            return s / 60
        
        def sToH(s: float) -> float:
            return s / 3600
        
    #temp
    class Temp:
        def cToK(c: float) -> float:
            return c + 273.15
        
        def cToF(c: float) -> float:
            return (c * 9 / 5) + 32
        
        def fToC(f: float) -> float:
            return (f - 32) * 5 / 9
        
        def fToK(f: float) -> float:
            return (f - 32) * 5 / 9 + 273.15
       
        def kToF(k: float) -> float:
            return (k - 273.15) * 9 / 5 + 32
        
        def kToC(k: float) -> float:
            return k - 273.15
        
