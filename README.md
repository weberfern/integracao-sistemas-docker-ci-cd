# [ADS0024] Integração de Sistemas

## Estudo Guiado 01 - Pipeline CI: Integração Contínua, Testes e Deploy com Docker

Este projeto foi desenvolvido para a disciplina **[ADS0024] Integração de Sistemas** e apresenta uma API web em Flask preparada para um fluxo básico de Integração Contínua (CI), execução de testes automatizados e empacotamento com Docker.

A aplicação representa a API do serviço **FastOrder** e disponibiliza endpoints para validar o funcionamento do serviço e realizar uma operação simples de soma.

## Tecnologias

- Python 3.9
- Flask
- Pytest e pytest-flask
- Flake8
- Docker

## Funcionalidades

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/` | Retorna uma mensagem de boas-vindas. |
| `GET` | `/api/status` | Informa o status e o nome do servico. |
| `GET` | `/api/soma?a=10&b=5` | Soma os valores `a` e `b` recebidos como parâmetros. |

Exemplo de resposta de `/api/soma?a=10&b=5`:

```json
{
  "resultado": 15
}
```

## Estrutura do projeto

```text
.
├── app.py             # Código da API Flask
├── test_app.py        # Testes automatizados
├── requirements.txt   # Dependências Python
├── Dockerfile         # Configuração da imagem Docker
└── README.md          # Documentação do projeto
```

## Execução local

1. Crie e ative um ambiente virtual:

	```bash
	python -m venv venv
	```

	No Windows PowerShell:

	```powershell
	.\venv\Scripts\Activate.ps1
	```

2. Instale as dependências:

	```bash
	pip install -r requirements.txt
	```

3. Inicie a API:

	```bash
	python app.py
	```

A aplicação ficará disponível em `http://localhost:5000`.

## Testes e verificação de qualidade

Execute os testes automatizados com:

```bash
pytest
```

Para executar a verificação de estilo:

```bash
flake8 app.py test_app.py
```

O pipeline de CI deve instalar as dependências e executar essas verificações antes de considerar a alteração apta para empacotamento.

## Execução com Docker

1. Construa a imagem:

	```bash
	docker build -t fastorder-api .
	```

2. Execute o contêiner:

	```bash
	docker run --name fastorder-api -p 5000:5000 fastorder-api
	```

Acesse `http://localhost:5000` ou teste os endpoints diretamente:

```bash
curl http://localhost:5000/
curl http://localhost:5000/api/status
curl "http://localhost:5000/api/soma?a=10&b=5"
```

Para parar e remover o contêiner:

```bash
docker stop fastorder-api
docker rm fastorder-api
```

## Fluxo de Integração Contínua

O fluxo proposto para o projeto é:

1. Receber uma alteracao no repositório.
2. Instalar as dependências do projeto.
3. Executar os testes automatizados com `pytest`.
4. Verificar o padrão do codigo com `flake8`.
5. Construir a imagem Docker com `docker build`.
6. Disponibilizar a imagem ou a aplicação para a etapa de deploy.

Esse processo ajuda a identificar erros rapidamente e garante que somente alterações verificadas avancem para a entrega.

## Objetivo acadêmico

O Estudo Guiado 01 tem como objetivo praticar conceitos de Integração Contínua, testes automatizados, conteinerização e preparação de uma aplicação para um processo de deploy repetível.
