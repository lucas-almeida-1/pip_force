# pip_force.py

Este script Python automatiza a instalação de pacotes via pip, repetindo a tentativa em caso de falha de conexão. É útil para ambientes com internet instável, garantindo que a instalação só termina quando for bem-sucedida.

## Como funciona
- O script solicita ao usuário o nome do pacote a ser instalado.
- Tenta instalar o pacote usando `pip install`.
- Se ocorrer uma falha (por exemplo, perda de conexão), ele espera 0.5 segundos e tenta novamente.
- O processo se repete até a instalação ser concluída com sucesso.

## Como usar
1. Certifique-se de ter Python e pip instalados no sistema.
2. Salve o script como `pip_force.py`.
3. Execute o script no terminal:

```shell
python pip_force.py
```
ou de forma abreviada:
```shell
py pip_force.py
```

4. O script será executado e solicitará que você digite o nome do pacote desejado. Enquanto o script estiver sendo executado, ele se manterá tentando instalar até que seja concluído com sucesso ou interrompido pelo usuário.

## Exemplo de uso
```
Você quer instalar a lib requests...
Executou o código e retornará:
"Digite o nome do pacote a ser instalado:"
Você digitou "requests"
O script tenta instalar a biblioteca, qualquer erro ele entra num loop de tentativas
"Tentando instalar requests..."
Finalizada a instalação, você já pode executar seu script que requer a lib requests.
"requests instalado com sucesso!"
```

## Observações
- O tempo de espera entre as tentativas é de 0.5 segundos. Você pode editar esse valor para um tempo maior ou menor se desejar.
- Se o pip não estiver instalado ou não for encontrado, o script exibirá uma mensagem de erro e encerrará.

## Licença e contribuições
Uso livre (Agradeço de marcar meu usuário GitHub caso tenha te ajudado)  
Fique à vontade para contribuir com melhorias através de pull requests.
