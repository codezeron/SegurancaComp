
## Trabalho 5
Criar um código capaz de gerar um par de chaves com o algoritmo DSA, assinar uma mensagem/arquivo e enviar por email para o destinatário. Ofereça a alternativa de mandar a mensagem/assinatura cifrada ou não (utilizar AES).
Criar outro código para decriptografia e verificação da assinatura para o arquivo recebido por email.
Teste seu código enviando o código de verificação para um colega e a mensagem/assinatura por email. O destinatário deverá conhecer a chave pública do emissor.

Para testar o trabalho, use os comandos abaixo:

assinatura
```bash
python3 sign.py
```
verificação
```bash
python3 verify.py
```



