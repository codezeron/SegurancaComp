from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.fernet import Fernet

# Função para gerar um par de chaves ECDSA
def gerar_par_de_chaves_ECDSA():
    private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

# Função para assinar uma mensagem com a chave privada ECDSA
def assinar_mensagem_ECDSA(private_key, mensagem):
    mensagem_bytes = mensagem.encode('utf-8')
    assinatura = private_key.sign(
        mensagem_bytes,
        ec.ECDSA(hashes.SHA256())
    )
    return assinatura

# Função para salvar os dados em um arquivo
def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'wb') as arquivo_saida:
        arquivo_saida.write(dados)


# Digite a mensagem de texto claro
mensagem_claro = input("Digite sua mensagem de texto claro: ")

# Gere o par de chaves ECDSA
private_key, public_key = gerar_par_de_chaves_ECDSA()

# Assine a mensagem com a chave privada ECDSA
assinatura = assinar_mensagem_ECDSA(private_key, mensagem_claro)

# Pergunte ao usuário se deseja usar Fernet para criptografar e salvar os dados
usar_fernet = input("Deseja usar Fernet para criptografar os dados? (S/N): ").strip().lower() == 's'

# salvar a chave publica do ECDSA
chave_pub_ec= public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
)
salvar_dados("chave_ec.bin", chave_pub_ec)


if usar_fernet:
    # Gere uma chave Fernet
    chave_fernet = Fernet.generate_key()
    fernet = Fernet(chave_fernet)

    # Salve a chave Fernet pública em um arquivo binário
    nome_arquivo_chave_fernet = "chave_fernet_publica.bin"
    salvar_dados(nome_arquivo_chave_fernet,chave_fernet)
    salvar_dados("mensagem.bin",fernet.encrypt(mensagem_claro.encode('utf-8')))
    salvar_dados("assinatura.bin",fernet.encrypt(assinatura))
    
    print("Dados criptografados salvos como 'dados_mensagem_assinatura.bin'.")
    print(f"Chave Fernet pública salva como '{nome_arquivo_chave_fernet}'.")
    print("chave pública ECDSA salva em chave_en.bin")

else:
   
    salvar_dados("mensagem.bin",mensagem_claro.encode('utf-8'))
    salvar_dados("assinatura.bin",assinatura)

    print("Mensagem clara, assinatura salvas como 'dados_mensagem_assinatura.bin'.")
    print("chave pública ECDSA salva em chave_en.bin")


