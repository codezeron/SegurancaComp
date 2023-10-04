
## Trabalho 6
Criar um certificado digital auto-assinado com o OpenSSL, seguindo os passos 1, 2 e 3 do tutorial:
[X.509 authentication in spring security](https://www.baeldung.com/x-509-authentication-in-spring-security)
Do passo 4 em diante, trata-se de um exemplo de utilização desse certificado num servidor web, o que é bastante interessante conhecer e recomendado que tentem fazê-lo, mas não será obrigatório para essa atividade.
Alternativamente, podem se basear nesse outro tutorial, que utiliza curva elíptica:
[exemplo do certificado no servidor web](https://blog.devolutions.net/2020/07/tutorial-how-to-generate-secure-self-signed-server-and-client-certificates-with-openssl/)

Para testar o trabalho, use os comandos abaixo:

Gerar as chaves open ssl
```bash
./gen_openssl_keys.sh 
```

Gerar a autenticação server-side
```bash
./keystore.sh  
```

Imprimir o certificado
```bash
./show_certificate.sh 
```

Gerar o arquivo pkcs12 
```bash
 ./gen_pkcs12.sh   
```

gera um repositódio de chaves e importa o localhost.p12
```bash
./import_keystore.sh 
```
