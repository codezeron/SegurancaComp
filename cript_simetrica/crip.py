from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

#Função para criptografar dados usando DES
def encrypt_des(data, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)  # Cria um objeto DES com a chave e o modo ECB
    encrypted_data = cipher.encrypt(pad(data, DES.block_size))  # Criptografa os dados após preenchimento
    return encrypted_data

# Função para descriptografar dados usando DES
def decrypt_des(encrypted_data, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)  # Cria um objeto DES com a chave e o modo ECB
    decrypted_data = unpad(cipher.decrypt(encrypted_data), DES.block_size)  # Descriptografa e remove o preenchimento
    return decrypted_data.decode()  # Retorna os dados descriptografados como string


def main():
    key = input("Digite a chave criptográfica: ")  # Recebe a chave criptográfica do usuário de 8 caracteres (8bytes)

    while True:
        print("\nMenu:")
        print("1. Criptografar texto inserido no código")
        print("2. Criptografar texto digitado no console")
        print("3. Criptografar texto de um arquivo de texto")
        print("4. Criptografar arquivo binário")
        print("5. Descriptografar um arquivo")
        print("6. Sair")
        
        choice = input("Escolha uma opção: ")  # Recebe a escolha do usuário

        if choice == "1":
            plaintext = "Texto exemplo para criptografar"  # Texto de exemplo para criptografar
            encrypted_data = encrypt_des(plaintext.encode(), key)  # Chama a função de criptografia
            print("Texto criptografado:", encrypted_data)  # Exibe o texto criptografado

        elif choice == "2":
            plaintext = input("Digite o texto para criptografar: ")  # Recebe o texto a ser criptografado
            encrypted_data = encrypt_des(plaintext.encode(), key)  # Chama a função de criptografia
            print("Texto criptografado:", encrypted_data)  # Exibe o texto criptografado

        elif choice == "3":
            file_name = input("Digite o nome do arquivo de texto: ")  # Recebe o nome do arquivo de texto
            with open(file_name, "r") as file:
                plaintext = file.read()  # Lê o conteúdo do arquivo de texto
                encrypted_data = encrypt_des(plaintext.encode(), key)  # Chama a função de criptografia
                encrypted_file_name = file_name + ".enc"  # Gera o nome do arquivo criptografado
                with open(encrypted_file_name, "wb") as encrypted_file:
                    encrypted_file.write(encrypted_data)  # Salva os dados criptografados no arquivo
                print("Arquivo criptografado salvo como:", encrypted_file_name)  # Exibe o nome do arquivo criptografado

        elif choice == "5":
            encrypted_file_name = input("Digite o nome do arquivo criptografado: ")
            with open(encrypted_file_name, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()
                decrypted_data = decrypt_des(encrypted_data, key)
                decrypted_file_name = encrypted_file_name[:-4]  # Remove a extensão ".enc"
                with open(decrypted_file_name, "wb") as decrypted_file:
                    decrypted_file.write(decrypted_data)
                print("Arquivo descriptografado salvo como:", decrypted_file_name)
        elif choice == "6":
            break

if __name__ == "__main__":
    main()  # Chama a função principal ao executar o script
