from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# 1. Criando o chão do nosso mundo (para o jogador não cair no infinito)
chao = Entity(
    model='plane',
    scale=(30, 1, 30),        # Um chão bem grande
    color=color.green.tint(-.2), # Verde grama escuro
    texture='white_cube',     # Textura quadriculada
    texture_scale=(30, 30),
    collider='box'            # Isso faz o chão ser sólido!
)

# 2. Criando uma "Fábrica" de Blocos Interativos
class Bloco(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            texture='white_cube',
            color=color.orange,
            highlight_color=color.lime, # O bloco brilha verde quando o mouse passa por cima!
            collider='box'
        )

    # 3. A mágica da interação: O que acontece quando clicamos?
    def input(self, key):
        if self.hovered: # Se o mouse estiver apontando para este bloco
            
            # Botão esquerdo quebra o bloco
            if key == 'left mouse down':
                destroy(self)
                
            # Botão direito constrói um bloco novo colado nele
            if key == 'right mouse down':
                novo_bloco = Bloco(position=self.position + mouse.normal)

# 4. Construindo uma plataforma de blocos iniciais para a criança brincar
for z in range(5):
    for x in range(5):
        Bloco(position=(x, 1, z))

# 5. Colocando o jogador no mundo
jogador = FirstPersonController()


app.run()