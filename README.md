# Monitoramento de Preço do Bitcoin

Este projeto é uma aplicação em Python desenvolvida para monitorar o preço do Bitcoin utilizando a API pública da Binance. Os dados obtidos são registrados em um banco de dados PostgreSQL para análise e visualização posterior.

## Funcionalidades

- **Monitoramento em Tempo Real:** Busca os preços do Bitcoin em intervalos regulares usando a API pública da Binance.
- **Registro em Banco de Dados:** Armazena os dados de preço em um banco de dados PostgreSQL para armazenamento persistente.
- **Intervalos Configuráveis:** Permite a personalização dos intervalos de monitoramento.
- **Tratamento de Erros:** Inclui tratamento robusto de erros para operações na API e no banco de dados.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados:

- **Python 3.8+**
- **PostgreSQL**
- Bibliotecas Python: `requests`, `psycopg2`, `dotenv`

## Instruções de Configuração

### 1. Clone o Repositório

```bash
git clone https://github.com/seuusuario/monitoramento-preco-bitcoin.git
cd monitoramento-preco-bitcoin
```

### 2. Instale as Dependências

Crie um ambiente virtual e instale os pacotes Python necessários:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Configure as Variáveis de Ambiente

Crie um arquivo `.env` no diretório raiz e especifique as seguintes variáveis:

```env
DB_HOST=seu_host_postgresql
DB_PORT=sua_porta_postgresql
DB_NAME=seu_nome_banco_de_dados
DB_USER=seu_usuario_banco_de_dados
DB_PASSWORD=sua_senha_banco_de_dados
```

### 4. Configure o Banco de Dados

Execute o script SQL fornecido para configurar as tabelas necessárias:

```bash
psql -U seu_usuario_banco_de_dados -d seu_nome_banco_de_dados -f setup.sql
```

### 5. Execute a Aplicação

Inicie a aplicação com:

```bash
python main.py
```

## Como Usar

1. O script buscará o preço do Bitcoin periodicamente e registrará os dados no banco de dados PostgreSQL.
2. Você pode consultar o banco de dados para analisar as tendências de preço ou integrar os dados em outras aplicações.

## Estrutura do Projeto

```plaintext
monitoramento-preco-bitcoin/
├── main.py          # Script principal para buscar e registrar os preços
├── db.py            # Conexão e operações no banco de dados
├── api.py           # Lógica de interação com a API
├── requirements.txt # Dependências do Python
├── setup.sql        # Script SQL para configuração do banco de dados
├── .env.example     # Exemplo de arquivo de variáveis de ambiente
└── README.md        # Documentação do projeto
```

## Dependências

O projeto utiliza as seguintes bibliotecas Python:

- `requests`: Para realizar requisições HTTP à API da Binance.
- `psycopg2`: Para interagir com o banco de dados PostgreSQL.
- `dotenv`: Para carregar variáveis de ambiente.

## Melhorias Futuras

- Adicionar suporte para monitoramento de múltiplas criptomoedas.
- Implementar uma interface web para visualização em tempo real dos preços.
- Adicionar funcionalidade de alertas para mudanças significativas no preço.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## Contribuições

Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request para quaisquer mudanças ou melhorias.
