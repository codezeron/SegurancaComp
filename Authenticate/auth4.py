from cryptography.fernet import Fernet
import tarfile
from io import BytesIO
import subprocess
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import  ec



# Solicite a mensagem de texto claro do usuário
mensagem_claro = input("Digite sua mensagem de texto claro: ").encode('utf-8')


# Gere uma chave de criptografia
chave = Fernet.generate_key()
fernet = Fernet(chave)


def gerar_par_de_chaves_EC():
    # Gerar par de chaves EC com openssl
    subprocess.run(["openssl", "ecparam", "-name", "secp256k1", "-genkey", "-noout", "-out", "chave_ec.pem"], check=True)
    subprocess.run(["openssl", "ec", "-in", "chave_ec.pem", "-pubout", "-out", "chave_ec_pub.pem"], check=True)

    # Carregar a chave privada EC gerada com OpenSSL
    with open("chave_ec.pem", "rb") as arquivo_chave_privada:
        chave_privada = serialization.load_pem_private_key(
            arquivo_chave_privada.read(),
            password=None,
            backend=default_backend()
        )

    # Carregar a chave pública EC gerada com OpenSSL
    with open("chave_ec_pub.pem", "rb") as arquivo_chave_publica:
        chave_publica = serialization.load_pem_public_key(
            arquivo_chave_publica.read(),
            backend=default_backend()
        )

    return chave_privada, chave_publica



def autenticar_EC(mensagem_bytes, chave_privada):
    # Assinar a mensagem com a chave privada EC
    
    assinatura = chave_privada.sign(
        mensagem_bytes,
        ec.ECDSA(hashes.SHA256())
    )

    return assinatura

def verificar_assinatura_EC(mensagem_bytes, assinatura, chave_publica):
    # Verificar a assinatura da mensagem usando a chave pública EC
    
    try:
        chave_publica.verify(
            assinatura,
            mensagem_bytes,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except Exception:
        return False
    
    
def autentication(chave_privada,fern_key):
    
    assinatura_ec = autenticar_EC(mensagem_claro, chave_privada)
    # Crie um objeto BytesIO para armazenar os dados criptografados
    dados_criptografados_io = BytesIO()
    dados_criptografados_io.write(fern_key.encrypt(mensagem_claro + assinatura_ec + len(assinatura_ec).to_bytes(1,byteorder='big')))

    # Crie um arquivo tar e adicione os dados criptografados a ele
    with tarfile.open('dados.tar', 'w') as tar:
        mensagem_info = tarfile.TarInfo("mensagem.txt")
        dados_criptografados_io.seek(0)  # Volte ao início do BytesIO
        mensagem_info.size = len(dados_criptografados_io.getvalue())
        tar.addfile(mensagem_info, fileobj=dados_criptografados_io)
        
    print("\nArquivo criptografado salvo como 'dados.tar'\n")
  


def verification(chave_publica,fern_key):
    # Abrir o arquivo tar criptografado
    with open('dados.tar', 'rb') as arquivo_tar:
        # Abrir o arquivo tar
        with tarfile.open(fileobj=arquivo_tar, mode='r') as tar:
            # Extrair o arquivo de texto criptografado
            arquivo_info = tar.getmember('mensagem.txt')
            with tar.extractfile(arquivo_info) as arquivo_criptografado:
                dados_criptografados = arquivo_criptografado.read()

        
        dados_decifrados = fern_key.decrypt(dados_criptografados)
        tam = int.from_bytes(dados_decifrados[-1:], byteorder='big') + 1
        
        # tirar o hash dos dados decifrados
        hash_extraido = dados_decifrados[-tam:-1]
        
        #tirar o texto claro dos dados decifrados
        texto_claro = dados_decifrados[:-tam]

        if verificar_assinatura_EC(texto_claro, hash_extraido,chave_publica):
            print("Mensagem autenticada com sucesso!")
            print("Mensagem de texto claro:", texto_claro.decode('utf-8'))
        else:
            print("A mensagem não pôde ser autenticada.")
        
            
            
chave_privada_ec, chave_publica_ec = gerar_par_de_chaves_EC()

autentication(chave_privada_ec,fernet)
verification(chave_publica_ec,fernet)