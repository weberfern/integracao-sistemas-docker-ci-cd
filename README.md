# [ADS0024] Integracao de Sistemas

## Estudo Guiado 01 - Pipeline CI: Integracao Continua, Testes e Deploy com Docker

Este projeto foi desenvolvido para a disciplina **[ADS0024] Integracao de Sistemas** e apresenta uma API web em Flask preparada para um fluxo basico de Integracao Continua (CI), execucao de testes automatizados e empacotamento com Docker.

A aplicacao representa a API do servico **FastOrder** e disponibiliza endpoints para validar o funcionamento do servico e realizar uma operacao simples de soma.

## Tecnologias

- Python 3.9
- Flask
- Pytest e pytest-flask
- Flake8
- Docker

## Funcionalidades

| Metodo | Rota | Descricao |
| --- | --- | --- |
| `GET` | `/` | Retorna uma mensagem de boas-vindas. |
| `GET` | `/api/status` | Informa o status e o nome do servico. |
| `GET` | `/api/soma?a=10&b=5` | Soma os valores `a` e `b` recebidos como parametros. |

Exemplo de resposta de `/api/soma?a=10&b=5`:

```json
{
  "resultado": 15
}
```

## Estrutura do projeto

```text
.
├── app.py             # Codigo da API Flask
├── test_app.py        # Testes automatizados
├── requirements.txt   # Dependencias Python
├── Dockerfile         # Configuracao da imagem Docker
└── README.md          # Documentacao do projeto
```

## Execucao local

1. Crie e ative um ambiente virtual:

	```bash
	python -m venv venv
	```

	No Windows PowerShell:

	```powershell
	.\venv\Scripts\Activate.ps1
	```

2. Instale as dependencias:

	```bash
	pip install -r requirements.txt
	```

3. Inicie a API:

	```bash
	python app.py
	```

A aplicacao ficara disponivel em `http://localhost:5000`.

## Testes e verificacao de qualidade

Execute os testes automatizados com:

```bash
pytest
```

Para executar a verificacao de estilo:

```bash
flake8 app.py test_app.py
```

O pipeline de CI deve instalar as dependencias e executar essas verificacoes antes de considerar a alteracao apta para empacotamento.

## Execucao com Docker

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

## Fluxo de Integracao Continua

O fluxo proposto para o projeto e:

1. Receber uma alteracao no repositorio.
2. Instalar as dependencias do projeto.
3. Executar os testes automatizados com `pytest`.
4. Verificar o padrao do codigo com `flake8`.
5. Construir a imagem Docker com `docker build`.
6. Disponibilizar a imagem ou a aplicacao para a etapa de deploy.

Esse processo ajuda a identificar erros rapidamente e garante que somente alteracoes verificadas avancem para a entrega.

## Objetivo academico

O Estudo Guiado 01 tem como objetivo praticar conceitos de Integracao Continua, testes automatizados, conteinerizacao e preparacao de uma aplicacao para um processo de deploy repetivel.
