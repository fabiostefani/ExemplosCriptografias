import hashlib
from blake3 import blake3
from passlib.hash import argon2
from datetime import *

mensagem = b'desenvolvedorio'

print('============================ Blake3 ============================')
daqui20Segundos = datetime.now() + timedelta(seconds=20)
blake3Execucoes = 0
while datetime.now() < daqui20Segundos:
    blake3(mensagem).digest()
    blake3Execucoes += 1

print('Execuções Blake3 em 20 segundos:', blake3Execucoes) 

print('=================== MD5 ==============')
daqui20Segundos = datetime.now() + timedelta(seconds=20)
md5Execucoes = 0
while datetime.now() < daqui20Segundos:
    hashlib.md5(mensagem).digest()
    md5Execucoes += 1

print('Execuções MD5 em 20 segundos: ', md5Execucoes)    

print('=================== SHA-256 ==============')
daqui20Segundos = datetime.now() + timedelta(seconds=20)
sha256Execucoes = 0
while datetime.now() < daqui20Segundos:
    hashlib.sha256(mensagem).digest()
    sha256Execucoes += 1

print('Execuções SHA-256 em 20 segundos: ', sha256Execucoes)    

print('=================== Argon2 ==============')
daqui20Segundos = datetime.now() + timedelta(seconds=20)
argon2Execucoes = 0
while datetime.now() < daqui20Segundos:
    argon2.using(memory_cost=131072, rounds=6).hash(mensagem)
    argon2Execucoes += 1

print('Execuções Argon2 em 20 segundos: ', argon2Execucoes)    