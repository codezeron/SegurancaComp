
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

iv_8 = get_random_bytes(8)
iv_16 = get_random_bytes(16)


def encrypt_aes(data, key, mode):
    global cipher
    if mode == AES.MODE_ECB:
        cipher = AES.new(key, mode)
    elif mode in (AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB):
        cipher = AES.new(key, mode, iv=iv_16)
    elif mode == AES.MODE_CTR:
        cipher = AES.new(key, mode, initial_value=iv_8)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    return encrypted_data


def decrypt_aes(encrypted_data, key, mode):
    global cipher
    if mode == AES.MODE_ECB:
        cipher = AES.new(key, mode)
    elif mode in (AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB):
        cipher = AES.new(key, mode, iv=iv_16)
    elif mode == AES.MODE_CTR:
        cipher = AES.new(key, mode, initial_value=iv_8, nonce=cipher.nonce)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    return decrypted_data


def main():
    key_length = int(input("Escolha o tamanho da chave (128 ou 256): "))
    if key_length not in (128, 256):
        print("Tamanho de chave inválido.")
        return
       
    global key
    key = get_random_bytes(key_length // 8)  # Chave em bytes

    data = b"Texto para criptografar e descriptografar"

    modes = [
            AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CFB,
            AES.MODE_OFB, AES.MODE_CTR
            ]
    mode_names = ["ECB", "CBC", "CFB", "OFB", "CTR"]

    for mode, mode_name in zip(modes, mode_names):
        encrypted_data = encrypt_aes(data, key, mode)
        decrypted_data = decrypt_aes(encrypted_data, key, mode)

        print(f"Modo: {mode_name}")
        print("Texto original:", data)
        print("Texto criptografado:", encrypted_data)
        print("Texto descriptografado:", decrypted_data)
        print()


if __name__ == "__main__":
    main()
