from email import message
import secrets
import binascii

def gerar_chave(n):
    bytearray = []
    aleatorio = secrets.SystemRandom()
    for i in range(n):
        bytearray.append(aleatorio.randint(0,255))
    return bytes(bytearray)

def xor(chave, mensagem):
    length = len(mensagem)
    return bytes([chave[i] ^ mensagem[i] for i in range(length)])

mensagem = "desenvolvedor.io"
mensagem = mensagem.encode()
chave = gerar_chave(len(mensagem))
cipher = xor(chave, mensagem)
print('Chave:', binascii.hexlify(chave).decode())
print('Cipher:',binascii.hexlify(cipher).decode())
print('Resultado:',xor(chave, cipher).decode())