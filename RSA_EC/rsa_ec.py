import subprocess
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import  ec, padding
from cryptography.hazmat.backends import default_backend


def gerar_par_de_chaves_RSA():
    # Gerar par de chaves RSA com openssl
    subprocess.run(["openssl", "genpkey", "-algorithm", "RSA", "-out", "chave_rsa.pem"], check=True)
    subprocess.run(["openssl", "rsa", "-in", "chave_rsa.pem", "-outform", "PEM", "-pubout", "-out", "chave_rsa_pub.pem"], check=True)

    # Carregar chave privada RSA com cryptography
    with open("chave_rsa.pem", "rb") as arquivo_chave_privada:
        chave_privada = serialization.load_pem_private_key(
            arquivo_chave_privada.read(),
            password=None,
            backend=default_backend()
        )

    # Carregar chave pública RSA com cryptography
    with open("chave_rsa_pub.pem", "rb") as arquivo_chave_publica:
        chave_publica = serialization.load_pem_public_key(
            arquivo_chave_publica.read(),
            backend=default_backend()
        )

    return chave_privada, chave_publica

def criptografar_RSA(mensagem, chave_publica):
    # Criptografar mensagem com chave pública RSA
    mensagem_bytes = mensagem.encode("utf-8")
    ciphertext = chave_publica.encrypt(
        mensagem_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return ciphertext

def descriptografar_RSA(ciphertext, chave_privada):
    # Descriptografar mensagem com chave privada RSA
    mensagem_bytes = chave_privada.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    mensagem = mensagem_bytes.decode("utf-8")

    return mensagem

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



def autenticar_EC(mensagem, chave_privada):
    # Assinar a mensagem com a chave privada EC
    mensagem_bytes = mensagem.encode("utf-8")
    assinatura = chave_privada.sign(
        mensagem_bytes,
        ec.ECDSA(hashes.SHA256())
    )

    return assinatura

def verificar_assinatura_EC(mensagem, assinatura, chave_publica):
    # Verificar a assinatura da mensagem usando a chave pública EC
    mensagem_bytes = mensagem.encode("utf-8")
    try:
        chave_publica.verify(
            assinatura,
            mensagem_bytes,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except Exception:
        return False


#Exemplo de uso
chave_privada_rsa, chave_publica_rsa = gerar_par_de_chaves_RSA()
chave_privada_ec, chave_publica_ec = gerar_par_de_chaves_EC()

mensagem_original = "Olá, mundo!"

# Criptografia e descriptografia usando RSA
ciphertext_rsa = criptografar_RSA(mensagem_original, chave_publica_rsa)
mensagem_descriptografada_rsa = descriptografar_RSA(ciphertext_rsa, chave_privada_rsa)

# Autenticação usando EC
assinatura_ec = autenticar_EC(mensagem_original, chave_privada_ec)
verificacao_ec = verificar_assinatura_EC(mensagem_original, assinatura_ec, chave_publica_ec)

print("Mensagem original:", mensagem_original)
print("\nCiphertext RSA:", ciphertext_rsa.hex())
print("\nMensagem descriptografada RSA:", mensagem_descriptografada_rsa)
print("\nAssinatura EC: ", assinatura_ec.hex())
print("\nVerificação de Assinatura EC:", verificacao_ec)
