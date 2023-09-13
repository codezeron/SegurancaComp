import hashlib
import tarfile
from io import BytesIO

from cryptography.fernet import Fernet

# arrumar o codigo

# Solicite a mensagem de texto claro do usuário
mensagem_claro = input("Digite sua mensagem de texto claro: ").encode('utf-8')

# Crie o hash da mensagem com o sal
mensagem_hash = hashlib.sha256(mensagem_claro).digest()

# Gere uma chave de criptografia
chave = Fernet.generate_key()
fernet = Fernet(chave)


def autentication():

    # Crie um objeto BytesIO para armazenar os dados criptografados
    dados_criptografados_io = BytesIO()
    dados_criptografados_io.write(
        fernet.encrypt(mensagem_hash) + mensagem_claro)

    # Crie um arquivo tar e adicione os dados criptografados a ele
    with tarfile.open('dados.tar', 'w') as tar:
        mensagem_info = tarfile.TarInfo("mensagem.txt")
        dados_criptografados_io.seek(0)  # Volte ao início do BytesIO
        mensagem_info.size = len(dados_criptografados_io.getvalue())
        tar.addfile(mensagem_info, fileobj=dados_criptografados_io)

    print("\nArquivo criptografado salvo como 'dados.tar'\n")


def verification():
    # Abrir o arquivo tar criptografado
    with open('dados.tar', 'rb') as arquivo_tar:
        # Abrir o arquivo tar
        with tarfile.open(fileobj=arquivo_tar, mode='r') as tar:
            # Extrair o arquivo de texto criptografado
            arquivo_info = tar.getmember('mensagem.txt')
            with tar.extractfile(arquivo_info) as arquivo_criptografado:
                dados_criptografados = arquivo_criptografado.read()

        # Descriptografar a mensagem criptografada
        hash_extraido_cript = dados_criptografados[:-len(mensagem_claro)]
        
        hash_extraido = fernet.decrypt(hash_extraido_cript)

        texto_claro = dados_criptografados[-len(mensagem_claro):]
        # Extrair o hash

        # Calcular o hash da mensagem de texto claro e verificar a autenticidade
        hasher = hashlib.sha256()
        hasher.update(texto_claro)
        mensagem_hash_calculado = hasher.digest()

        if hash_extraido == mensagem_hash_calculado:
            print("Mensagem autenticada com sucesso!")
            print("Mensagem de texto claro:", texto_claro.decode('utf-8'))
        else:
            print("A mensagem não pôde ser autenticada.")


autentication()
verification()
