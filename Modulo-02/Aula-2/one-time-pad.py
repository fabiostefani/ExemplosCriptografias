import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.']
def gerar_chave(n):
    global alphabet
    shifts = []
    for i in range(n):
        shifts.append(random.randint(0, len(alphabet)))
    return shifts

def shift(char, shift):
    global alphabet
    nova_posicao = (alphabet.index(char) + shift) % len(alphabet)
    return alphabet[nova_posicao]

def criptografar(mensagem, shifts):
    global alphabet
    length = len(mensagem)
    return str.join('', [shift(mensagem[i], shifts[i]) for i in range(length)])

def descriptogrfar(mensagem, shits):
    global alphabet    
    length = len(mensagem)
    return str.join('', [shift(mensagem[i], shits[i] * -1) for i in range(length)])

mensagem = "desenvolvedor.io"
chave = gerar_chave(len(mensagem))
print(chave)
print(shift('a',10))
cipher = criptografar(mensagem, chave)
print('cipher:', cipher)
plainText = descriptogrfar(cipher, chave)
print('Plain text:', plainText)