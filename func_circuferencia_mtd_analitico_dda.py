from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


x1, y1, x2, y2 = 0, 0, 0, 0

def funcao_circunferencia_dda():
    global x1, y1, x2, y2
    
    raio = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    delta_t = 0.0001
    t = 0
    
    glBegin(GL_POINTS)
    while t < 2:
        x = int(math.floor(raio * math.cos(t)))
        y = int(math.floor(raio * math.sin(t)))
        glVertex2f(x + x1, y + y1)
        glVertex2f(-x + x1, y + y1)
        glVertex2f(-x + x1, -y + y1)
        glVertex2f(x + x1, -y + y1)
        t += delta_t
    glEnd()
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    funcao_circunferencia_dda()

def main():
    global x1, y1, x2, y2
    
    x1 = int(input("Informe o valor de X1: "))
    y1 = int(input("Informe o valor de Y1: "))
    x2 = int(input("Informe o valor de X2: "))
    y2 = int(input("Informe o valor de Y2: "))
    
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Funcao Circunferencia - DDA")
    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-200, 200, -200, 200)
    
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
