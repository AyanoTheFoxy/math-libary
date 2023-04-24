print("I'm just starting, Hello World!")
import math

#math
log = math.Log(27, 3)
cmfr = math.Cmfr(20)
root = math.Root(100)
lerp = math.Lerp(10, 20, .5)

# player 2d
playerX = 0
playerY = 1
playerPos = math.Vect2(playerX, playerY)

# player 3s
player2X = 0
player2Y = 1
player2Z = 2
player2Pos = math.Vect3(player2X, player2Y, player2Z)

# graphics
px1 = math.Pixels.PtToPx(1)
px2 = math.Pixels.EmToPx(1)
px3 = math.Pixels.InToPx(1)

# blocks
block = math.Area.Square(1, 1, 32, 32)
blockSize = 1

print("--complex operations--")
print("log 27 with base 3 is " + str(log))
print("circumference of a cricle with 40 px of diamter is " + str(cmfr))
print("square root 100 is " + str(root))
print("lerp 10 + 20 is " + str(lerp))
print("--player pos (vect2)--")
print("pos x is " + str(playerPos[0])) # pos x
print("pos y is " + str(playerPos[1])) # pos y
print("--player pos (vect3)--")
print("pos x is " + str(player2Pos[0]))
print("pos y is " + str(player2Pos[1]))
print("pos z is " + str(player2Pos[2]))
print("--block area (area.square)--")
print("block x is " + str(block[0]))
print("block y is " + str(block[1]))
print("block w is " + str(block[2]))
print("block h is " + str(block[3]))
print("--pt to px--")
print("1 pt is " + str(px1) + "px") 
print("1 em is " + str(px2) + "px")
print("1 in is " + str(px3) + "px")