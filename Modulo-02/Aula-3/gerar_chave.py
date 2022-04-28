import os
import secrets
from base64 import b64encode

aleatorio = os.urandom(128)
print('string criptograficamente seguro: ', b64encode(aleatorio).decode('utf-8'))

aleatorio = secrets.SystemRandom()
print('numero criptograficamente seguro: ',  aleatorio.randint(0,100))