import hashlib
mensagem = 'desenvolvedor.io'
result = hashlib.md5(mensagem.encode())
print('Mensagem:', mensagem)
print('Hash value:', result.hexdigest())