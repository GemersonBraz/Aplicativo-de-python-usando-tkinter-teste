# Sistema de Cadastro de Pessoal

Este repositório contém um sistema de cadastro de pessoal desenvolvido em Python, utilizando a biblioteca Tkinter para a interface gráfica e outras bibliotecas como `ttkbootstrap`, `openpyxl`, e `fpdf` para funcionalidades adicionais. O objetivo principal do projeto é permitir o registro, gerenciamento e exportação de dados de pessoal em um formato amigável.

## Descrição do Projeto

### Funcionalidades Principais
- **Cadastro de Pessoal**: Permite a inserção de dados como documento, nome, validade, status militar, veículo, placa e cor.
- **Verificação de Cadastro**: Antes de registrar um novo pessoal, o sistema verifica se o documento já está cadastrado.
- **Gerenciamento de Registros**: Os usuários podem visualizar, apagar e editar registros existentes através de uma interface intuitiva.
- **Exportação para PDF**: Os dados cadastrados podem ser salvos em um arquivo PDF, facilitando a impressão e compartilhamento.
- **Interface Amigável**: Utiliza o Tkinter e `ttkbootstrap` para criar uma interface gráfica moderna e responsiva.

### Estrutura do Código
O código é organizado em várias funções que tratam diferentes aspectos do sistema:
- **Funções de Manipulação de Arquivo**: Criação e leitura de arquivos Excel usando `openpyxl`.
- **Funções de Registro**: Captura e validação dos dados inseridos pelo usuário.
- **Funções de Formatação**: Formata automaticamente os campos de entrada (como placa e validade) para garantir a consistência dos dados.
- **Funções da Interface Gráfica**: Configuração da janela principal, botões, entradas e Treeview para visualização dos registros.
