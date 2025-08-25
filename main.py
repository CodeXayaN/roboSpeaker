import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "q":
            command = 'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
                      '(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'bye bye friend\')"'
            os.system(command)
            break
        command = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
                  f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        os.system(command)

