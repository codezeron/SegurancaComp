# Seguranca Computacional

Este repositório conta com os trabalhos desenvolvidos para a matéria de segurança computacional

## Trabalho 1

Utilize sua IDE e linguagem de programação de preferência para criar um código capaz de criptografar um texto inserido diretamente no código, um texto digitado no console, um texto lido de um arquivo (ex. um txt em seu disco) e um arquivo binário (ex. uma foto, pdf, etc). Utilize uma chave criptográfica digitada. Crie um menu simples para a escolha das opções.

Utilizar o algoritmo DES.

Requisito:
Instalar a biblioteca pycryptodome v3.18.0 ou acima

Para testar o trabalho:

1. inicie o arquivo na pasta cript_simetrica

2. inicie o código com `python3 cript.py`

3. insira uma senha/chave de 8 dígitos 

4. escolha a opção 1 para criptografar esse texto: "Texto exemplo para criptografar"

5. escolha a opção 2 para criptografar um texto que vai ser digitado por você

6. escolha a opção 3 para inserir o arquivo de texto, por exemplo "arquivo_teste.txt", no campo de texto e aperte ENTER

7. escolha a opção 4 para inserir o arquivo binário, por exemplo "nome_do _arquivo.png/.pdf", no campo de texto e aperte ENTER

8. escolha a opção 4 para descriptografar um arquivo inserindo o nome do arquivo

Os resultados esperados são a saída de criptografia na tela para os três primeiros botões e as imagens criptografadas e descriptografadas para o último botão.

