import hashlib
mensagem = 'desenvolvedor.io'
result = hashlib.sha256(mensagem.encode())
print('Mensagem:', mensagem)
print('Hash value:', result.hexdigest())
print('Digest value:', result.digest_size)
print('Block size:', result.block_size)