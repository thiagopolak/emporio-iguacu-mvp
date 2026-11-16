# Empório Iguaçu — MVP

Aplicação Web para consulta de catálogo digital e organização de encomendas do **Empório Iguaçu**, comércio de produtos naturais, produtos a granel e itens artesanais localizado no bairro Vila Izabel, em Curitiba (PR).

> Projeto acadêmico desenvolvido na disciplina **Projeto de Software**, com foco em transformar necessidades identificadas junto ao parceiro comunitário em uma solução digital simples, acessível e compatível com a realidade de um pequeno comércio.

## Sobre o projeto

O Empório Iguaçu possui uma trajetória de mais de 30 anos na comunidade. Durante o diagnóstico, foram identificadas dificuldades na manutenção de um catálogo digital, na atualização de preços e na organização das encomendas recebidas principalmente por WhatsApp e telefone.

A proposta do MVP é centralizar a consulta de produtos e a montagem de encomendas em uma aplicação Web responsiva. A solução considera especialmente clientes com pouca familiaridade digital, incluindo pessoas idosas, e busca reduzir tarefas manuais na rotina dos funcionários.

## Objetivos do MVP

- Disponibilizar um catálogo digital organizado por categorias.
- Apresentar produtos, variações, preços e unidades de venda (kg ou unidade).
- Permitir que o cliente monte e revise uma encomenda.
- Registrar os dados necessários para o atendimento do pedido.
- Oferecer uma área administrativa para manutenção do catálogo e acompanhamento das encomendas.
- Priorizar uma interface simples, responsiva e acessível.

## Escopo inicial

O escopo foi definido para manter o produto viável e concentrado nas necessidades prioritárias do parceiro.

**Previsto para o MVP:**

- Consulta ao catálogo e às categorias.
- Cadastro, edição e desativação de produtos e variações por usuários autorizados.
- Montagem de carrinho com quantidades por peso ou unidade.
- Registro de encomendas com opção de retirada ou entrega.
- Consulta e atualização do status das encomendas pela equipe da loja.

**Fora do escopo inicial:** integração automática com o sistema de ponto de venda (PDV), pagamentos on-line, sincronização automática de estoque e integração direta com WhatsApp. Essas possibilidades poderão ser avaliadas em versões futuras.

## Tecnologias

| Tecnologia | Uso no projeto |
|---|---|
| Python 3.14 | Linguagem principal |
| Flask 3.1.3 | Framework Web e rotas da aplicação |
| Flask-SQLAlchemy 3.1.1 | Integração entre Flask e camada ORM |
| SQLAlchemy 2.1.0 | Mapeamento objeto-relacional |
| Flask-Login 0.6.3 | Gerenciamento de autenticação e sessões administrativas |
| Flask-WTF 1.3.0 | Formulários e proteção CSRF |
| argon2-cffi 25.1.0 | Hash seguro de senhas |
| Psycopg 3 | Driver de conexão com PostgreSQL |
| python-dotenv 1.2.4 | Leitura de configurações por variáveis de ambiente |
| HTML e CSS | Estrutura e apresentação das páginas |

**Banco de dados planejado:** PostgreSQL 18. A conexão e os modelos de persistência ainda serão implementados nas próximas etapas.

## Arquitetura e organização

O projeto utiliza Flask com uma estrutura inicial organizada por responsabilidades:

```text
emporio-iguacu-mvp/
├── app/
│   ├── models/       # Modelos e entidades de dados
│   ├── routes/       # Rotas e controle das requisições
│   ├── services/     # Regras e serviços da aplicação
│   ├── templates/    # Páginas HTML com Jinja
│   └── static/
│       ├── css/      # Folhas de estilo
│       ├── js/       # Scripts do navegador
│       └── images/   # Imagens e recursos visuais
├── tests/            # Testes automatizados
├── config.py         # Configurações da aplicação
├── requirements.txt  # Dependências Python
├── run.py            # Inicialização local
├── .env.example      # Exemplo de variáveis de ambiente (quando criado)
├── .gitignore
└── README.md
```

A estrutura será ampliada conforme os módulos forem implementados. No estágio atual, a página inicial do catálogo é executada com dados demonstrativos definidos na rota; a persistência no PostgreSQL, o carrinho funcional e a área administrativa ainda estão em desenvolvimento.

## Como executar localmente

### Pré-requisitos

- Windows 11 (ou outro sistema compatível com Python).
- Python 3.14 instalado.
- Git instalado.

### 1. Clonar o repositório

```powershell
git clone https://github.com/thiagopolak/emporio-iguacu-mvp.git
cd emporio-iguacu-mvp
```

### 2. Criar e ativar o ambiente virtual

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação, uma alternativa para o usuário atual é:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Depois, execute novamente o comando de ativação.

### 3. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

### 4. Iniciar a aplicação

```powershell
python run.py
```

Abra no navegador: <http://127.0.0.1:5000>

Para encerrar o servidor, pressione `Ctrl + C` no terminal.

## Segurança e configuração

- Não publique arquivos `.env`, senhas, tokens, chaves secretas ou credenciais do banco de dados.
- O arquivo `.env.example` deverá conter apenas nomes de variáveis e valores ilustrativos, nunca segredos reais.
- Em produção, a aplicação deverá utilizar HTTPS, `DEBUG` desativado e uma `SECRET_KEY` forte fornecida pelo ambiente.
- Senhas de usuários administrativos deverão ser armazenadas somente como hashes seguros, nunca em texto puro.

## Status do desenvolvimento

**Etapa atual:** estrutura inicial do Flask e primeira versão demonstrativa do catálogo publicadas no GitHub.

| Módulo | Situação |
|---|---|
| Repositório Git e estrutura inicial | Concluído |
| Aplicação Flask e rota inicial | Concluído |
| Catálogo demonstrativo | Concluído |
| Integração com PostgreSQL | Planejada / em desenvolvimento |
| Modelos e persistência de produtos | Pendente |
| Carrinho e registro de encomendas | Pendente |
| Autenticação e área administrativa | Pendente |
| Testes automatizados e integração contínua | Pendente |
| Validação com representantes da comunidade | Planejada |

## Contexto acadêmico

Projeto desenvolvido como parte da Experiência Prática da disciplina **Projeto de Software**. O trabalho contempla diagnóstico comunitário, definição do MVP, análise de soluções semelhantes, arquitetura, requisitos, prototipação, implementação, testes e validação.

A proposta está relacionada ao **ODS 8 — Trabalho Decente e Crescimento Econômico**, especialmente à meta 8.3, por buscar apoiar a produtividade e a modernização de um pequeno empreendimento.

## Autor

**Thiago Polak**

Repositório: <https://github.com/thiagopolak/emporio-iguacu-mvp>
