from pynput import keyboard

def keyscan(tecla):
    tecla = str(tecla)
    print(tecla)

with keyboard.Listener(on_press=keyscan) as listener:
    listener.join()















