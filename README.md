# Criptografia Assimétrica de Arquivos com Interface Gráfica

Este é um software em Python com interface gráfica que permite criptografar e descriptografar arquivos usando um sistema de criptografia assimétrica (RSA). Cada vez que o usuário deseja criptografar um arquivo, ele pode gerar um par de chaves RSA (pública e privada) diretamente na interface. A chave pública é usada para criptografia, e a chave privada é necessária para descriptografar o arquivo.

## Funcionalidades

- **Geração de Chaves RSA**: O software gera um novo par de chaves RSA (pública e privada) a cada vez que o botão "Gerar Novas Chaves" é clicado.
- **Criptografia de Arquivos**: O usuário pode selecionar um arquivo para criptografia. O software usa a chave pública para proteger o conteúdo.
- **Descriptografia de Arquivos**: O usuário pode selecionar um arquivo criptografado e usar a chave privada para restaurar o conteúdo original.
- **Interface Gráfica Intuitiva**: Interface fácil de usar, desenvolvida com Tkinter, permitindo geração de chaves e seleção de arquivos de maneira interativa.

## Requisitos

- **Windows 7 ou superior**.
- **Nenhuma dependência externa é necessária**, pois o executável contém todas as bibliotecas necessárias.

## Como Usar

### 1. Baixar o Executável

Clique no link abaixo para baixar o software:

[Baixar Criptografia Assimétrica de Arquivos](./dist/seu_script.exe)

### 2. Executar o Programa

- Execute o arquivo `seu_script.exe` para iniciar o software.
- O programa permite gerar chaves, criptografar e descriptografar arquivos diretamente pela interface gráfica.

### 3. Gerar Chaves RSA
- Clique em **"Gerar Novas Chaves"** para criar um novo par de chaves (pública e privada).
- As chaves geradas serão exibidas na interface. Você pode copiar e salvar as chaves se desejar reutilizá-las.

### 4. Criptografar um Arquivo
- Clique em **"Selecionar Arquivo"** e escolha o arquivo que deseja criptografar.
- Certifique-se de que a chave pública está exibida na interface.
- Clique em **"Criptografar"**. O arquivo será salvo com o sufixo `.encrypted`.

### 5. Descriptografar um Arquivo
- Selecione o arquivo `.encrypted` que deseja descriptografar.
- Certifique-se de que a chave privada está exibida na interface.
- Clique em **"Descriptografar"**. O arquivo descriptografado será salvo com o sufixo `.decrypted`.

## Estrutura do Projeto

- `encryption_gui.py`: O script principal que contém a interface gráfica e lógica de criptografia/descriptografia.
- Dependências: Apenas a biblioteca `cryptography` e `tkinter`.

## Notas de Segurança

- **Salve as chaves**: As chaves geradas são essenciais para criptografar e descriptografar arquivos. Sem a chave privada, não é possível descriptografar um arquivo.
- **Proteção da Chave Privada**: A chave privada deve ser protegida, pois ela permite o acesso aos dados criptografados. Evite compartilhá-la.

## Contribuições

Sinta-se à vontade para abrir issues e enviar pull requests para melhorias.

## Licença

Este projeto está licenciado sob a licença MIT.
