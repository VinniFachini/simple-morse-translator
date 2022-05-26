secret = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "?": "..--..", " ": "/", ",": "--..--", "Ç": "-.-.."}

translated = []


print('+' + "-" * 100 + '+')
print('| Aperte 1 para traduzir de ASCII para Morse')
print('| Aperte 2 para traduzir de Morse para ASCII')
choice = int(input('| Digite sua opção: '))


def ascii_to_morse(phrase):
    for i in phrase:
        for key, value in enumerate(secret):
            if i == value:
                translated.append(secret[i])
    return " ".join(translated)


def morse_to_ascii(phrase):
    for i in phrase.split(' '):
        for key, value in secret.items():
            if i == secret[key]:
                translated.append(key)
    return "".join(translated)


if choice == 1:
    print('| Selecionado: ASCII para Morse')
    to_translate = input('| Digite a mensagem para traduzir: ').upper()
    print(f'| Mensagem Traduzida: {ascii_to_morse(to_translate)}')
    print('+' + '-' * 100 + '+')
elif choice == 2:
    print('| Selecionado: Morse para ASCII')
    to_translate = input('| Digite a mensagem para traduzir: ').upper()
    print(f'| Mensagem Traduzida: {morse_to_ascii(to_translate).capitalize()}')
    print('+' + '-' * 100 + '+')
