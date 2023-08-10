"""
Arquivo principal do projeto. 
É substituído pelo maker.py na hora de converter o supervisor.
"""
from Supervisor import Events, Event, trigger_event
from time import sleep
# install getkey with: pip install getkey
from getkey import getkey

def btn_action(event: Event):
    trigger_event(Events['liga'])
    trigger_event(Events['desliga'])

def liga_action(event: Event):
    print('Ligando...')

def desliga_action(event: Event):
    print('Desligando...')

# set default action for example
Events['btn'].set_action(btn_action)
Events['liga'].set_action(liga_action)
Events['desliga'].set_action(desliga_action)

if __name__ == '__main__':
    # handle events for teste
    while True:
        print('Pressione "b" para ligar/desligar ou "q" para sair')
        # read one char from stdin
        key = getkey()
        if key == 'b':
            trigger_event(Events['btn'])
        if key == 'q':
            break
