'''from Settings import *

def Vetor():
    mousePos = pygame.mouse.get_pos()
    vector = pygame.math.Vector2((mousePos[0] - STARTX, STARTY - mousePos[1]))
    if vector.x == 0 :
        return vector, 90
    if vector.y < 0 and vector.x < 0:
        return vector, 179
    if vector.y < 0 and vector.x > 0:
        return vector, 1
    angle = math.degrees(math.atan(vector.y / vector.x))
    if angle < 0:
        angle += 180
    #print(angle)
    return vector, angle'''