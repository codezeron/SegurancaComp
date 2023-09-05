
## Trabalho 3

Gerar um par de chaves criptográficas RSA e EC utilizando o SSH Keygen, OpenSSL e também via código, na linguagem que preferirem.
Criar um código para carregar um par de chaves e realizar a criptografia e decriptografia de uma mensagem pequena.

Requisito:
Instalar a biblioteca cryptography 41.0.3 ou acima

Para testar o trabalho:

1. inicie o arquivo na pasta RSA_EC

2. inicie o código com `python3 rsa_ec.py`

3. Assim que começar o código, vai gerar as 4 chaves: privada e publica 
para RSA e EC 

Os resultados esperados são:
```bash
writing RSA key
read EC key
writing EC key
Mensagem original: Olá, mundo!

Ciphertext RSA: 860dd59ecd569de9dfdbd198fff5d190a781e5e1a50cfd705437fc820ce21db05c358cc5f401b62708b0a53eeedda213437d7e04bc849c24217ff45d9cc053205b19971dd2916416a41690a37dd601bb49e3bcff7b0112a5291261d4b3405191f246d8609fb907529321c474275e939aa6f4c02cc4bab8aa0ec176ae83faf3e3599721510e3b5bf0a9f43b4c1d50b95aa64751f8631fcce6443751f52b4b23c7f43d83d259191ab5b0f5ee6a50b0c6f3c99526b1be96eae5a767407fe1e6b40f739e9616cff540d60a114758dc9f9705908eb2b226be418e99ab65fff2747602f95c8cdf12ab435608534cbe6a4cd627e9000e231744d41e21a72eb5e82caa33

Mensagem descriptografada RSA: Olá, mundo!

Assinatura EC:  3046022100a00e584cc721dce84300ce1de6a2e2723898d1221e8d41bc62696bfa3d86be57022100e2de4266888270ee0759836f2d0c3cf0c7549f03215bd012709e3edcc6526fb3

Verificação de Assinatura EC: True
```

