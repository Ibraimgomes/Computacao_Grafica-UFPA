from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 300
window_width = 300
window_title = "Renderizar ponto com OpenGL"

points = [
    [-0.3, 0.2],
    [0, 0.4],
    [0.3, 0.2],
    [0.3, 0],
    [-0.3, 0],
    [-0.3, 0.2],
    [0.6, 0.2],
    [0.6, 0.05],
    [0.3, 0],
    [0.3, 0.2],
    [0.6, 0.2],
    [0.35, 0.35],
    [0, 0.4],

]

def init():
    glClearColor(0, 0, 0, 1)  # Define a cor de fundo como preto
    glPointSize(5)  # Define o tamanho do ponto

def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpa o buffer
    glLoadIdentity()  # Reseta a matriz

    glBegin(GL_LINE_LOOP)  # Desenha um loop de linhas
    glColor3f(1, 1, 1)  # Define a cor como branca1
    for v in points:  # Adiciona os pontos do loop
        glVertex2fv(v)
    glEnd()

    glFlush()  # Garante que tudo será renderizado

def main():
    glutInit()  # Inicializa o GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Configura o modo de display
    glutInitWindowSize(window_width, window_height)  # Define o tamanho da janela
    glutCreateWindow(window_title.encode("utf-8"))  # Cria a janela com o título
    init()  # Configurações iniciais
    glutDisplayFunc(render)  # Define a função de renderização
    glutMainLoop()  # Inicia o loop principal

if __name__ == "__main__":
    main()
