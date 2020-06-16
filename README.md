# Bubble shooter

Projeto final - Design de software - 2020.1 - Turma C

**MEMBROS**  
Isabella Corrêa Fuhrken e Guilherme Caproni de Faria

**Linguagem utilizada**  
Python

**Link do vídeo da apresentação do jogo:**  
https://www.youtube.com/watch?v=wR5XtVTv5xc

**Descrição do projeto**  
Desenvolvimento do um jogo de computador Bubble Shooter em Python 3 utilizando recursos da biblioteca PyGame.  
O jogo consiste em mirar e atirar a bolha principal no grid de bolhas. As bolhas que tiverem as mesmas cores irão explodir. Cada uma que for retirada acarreta em um aumento de 500 pontos. O objetivo do jogo é atingir 20000 pontos. Caso a bolha atirada ultrapasse a linha limite, o jogo se encerra.

**Instalação do PyGame**  
**Windows e Linux**  
Abra o seu terminal (Linux) ou Anaconda Prompt (Windows) e digite:  
pip install pygame  
**Mac OSX**  
Se você não tiver o Homebrew instalado, instale-o  
seguindo as instruções disponíveis neste link : https://brew.sh/  
Abra o terminal e digite:  
brew install sdl2 sdl2_gfx sdl2_image sdl2_mixer sdl2_net sdl2_ttf  
brew install Caskroom/cask/xquartz  
git clone -b 1.9.6 --single-branch https://github.com/pygame/pygame.git  
cd pygame  
python setup.py -config -auto -sdl2  
python setup.py install  
cd ..  
rm -rf pygame  
Para mais detalhes e outras opções de instalação no Mac, consulte a documentação:   
https://www.pygame.org/wiki/MacCompile

**Como executar o programa**. 
Execute o arquivo Main.py
