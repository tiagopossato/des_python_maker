from Supervisor import Events, Event, handle_event
from time import sleep
# install getkey with: pip install getkey
from getkey import getkey

def btn_callback(event: Event):
    handle_event(Events['liga'])
    handle_event(Events['desliga'])

def liga_callback(event: Event):
    print('Ligando...')

def desliga_callback(event: Event):
    print('Desligando...')

# set default callback for example
Events['btn'].set_callback(btn_callback)
Events['liga'].set_callback(liga_callback)
Events['desliga'].set_callback(desliga_callback)

if __name__ == '__main__':
    # handle events for teste
    while True:
        print('Pressione "b" para ligar/desligar ou "q" para sair')
        # read one char from stdin
        key = getkey()
        if key == 'b':
            handle_event(Events['btn'])
        if key == 'q':
            break
