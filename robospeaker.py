import os

print('Welcome to RoboSpeaker! You type it, I speak it')

while True:
    a = input('Provide the text you want me to speak: ')
    if a == 'quit':
        break
    command = f'say {a}'
    os.system(command)