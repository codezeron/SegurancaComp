from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.fernet import Fernet


# Função para ler a chave pública ECDSA a partir de bytes
def carregar_chave_publica_ECDSA(public_pem_bytes):
    public_key_ecdsa = serialization.load_pem_public_key(public_pem_bytes, backend=default_backend())
    return public_key_ecdsa


# Verifique a assinatura ECDSA
def verificar_assinatura_ECDSA(public_key, mensagem, assinatura):
    mensagem_bytes = mensagem.encode('utf-8')
    try:
        public_key.verify(assinatura, mensagem_bytes, ec.ECDSA(hashes.SHA256()))
        return True
    except Exception:
        return False

#funcao de ler os dados do arquivo
def ler_dados(nome_arquivo):
    with open(nome_arquivo, 'rb') as arquivo_entrada:
        dados = arquivo_entrada.read()
    return dados




mensagem_claro_cifrada = ler_dados("mensagem.bin")
assinatura_cifrada = ler_dados("assinatura.bin")

# Pergunte ao usuário se deseja usar Fernet ou AES para descriptografar
usar_fernet = input("Deseja usar a chave Fernet para descriptografar? (S/N): ").strip().lower() == 's'

if usar_fernet:
    # Abra o arquivo com a chave Fernet pública
    chave_fernet = ler_dados("chave_fernet_publica.bin")
    fernet = Fernet(chave_fernet)
    # Decifre os dados com Fernet
    mensagem_decifrados = fernet.decrypt(mensagem_claro_cifrada)
    assinatura_decifrada = fernet.decrypt(assinatura_cifrada)
    
else:
    # Defina dados_decifrados como os dados cifrados originais (sem descriptografia)
    mensagem_decifrados = mensagem_claro_cifrada
    assinatura_decifrada = assinatura_cifrada


# Carregue a chave pública ECDSA
public_pem_bytes = ler_dados("chave_ec.bin")

# Carregue a chave pública ECDSA
public_key_ecdsa = carregar_chave_publica_ECDSA(public_pem_bytes)

# Converta a mensagem clara para texto
mensagem_claro = mensagem_decifrados.decode('utf-8')

verificacao = verificar_assinatura_ECDSA(public_key_ecdsa, mensagem_claro, assinatura_decifrada)

if verificacao:
    print("A assinatura é válida.")
    print("Mensagem decifrada:", mensagem_claro)
else:
    print("A verificação da assinatura falhou.")
