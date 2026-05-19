# 🤖 Telegram Bot com Gemini AI

Bot desenvolvido em Python que integra o Telegram com a API da Gemini AI, permitindo conversas inteligentes diretamente pelo Telegram.

---

# 🧠 Como a aplicação funciona

A aplicação funciona como uma ponte entre:

```text
Usuário → Telegram → Bot Python → Gemini AI → Bot Python → Telegram → Usuário
```

---

# ⚙️ Fluxo completo da aplicação

## 1. Usuário envia mensagem

O usuário envia uma mensagem para o bot no Telegram.

Exemplo:

```text
Quem é você?
```

---

## 2. Telegram entrega a mensagem ao bot

A biblioteca `python-telegram-bot` mantém uma conexão ativa com os servidores do Telegram utilizando polling.

O bot constantemente verifica:

```text
"Existe alguma nova mensagem?"
```

---

## 3. O bot recebe a mensagem

A mensagem chega na função principal responsável pelas respostas:

```python
async def responder(update, context):
```

A mensagem enviada pelo usuário é extraída:

```python
mensagem = update.message.text
```

---

## 4. O bot envia a mensagem para a Gemini AI

A aplicação utiliza a SDK oficial da Gemini AI:

```python
google-generativeai
```

A mensagem é enviada para o modelo:

```python
model.generate_content(mensagem)
```

---

## 5. Gemini gera a resposta

A API da Gemini processa:
- interpretação do texto
- contexto
- geração de linguagem natural
- inferência do modelo

E retorna uma resposta textual.

---

## 6. O bot responde no Telegram

A resposta é enviada de volta ao usuário:

```python
await update.message.reply_text(resposta.text)
```

---

# 🏗️ Arquitetura da aplicação

## Backend

O backend inteiro é desenvolvido em:

- Python 3

Responsabilidades:
- comunicação com Telegram
- comunicação com Gemini
- processamento das mensagens
- gerenciamento do fluxo da aplicação

---

# 📚 Stack utilizada

## 🐍 Python

Linguagem principal da aplicação.

Responsável por:
- lógica do sistema
- integração das APIs
- execução do bot

---

## 📦 python-telegram-bot

Biblioteca responsável pela comunicação com a API do Telegram.

Funções principais:
- receber mensagens
- enviar respostas
- gerenciar comandos
- polling
- sistema assíncrono

---

## 🧠 Google Gemini API

Modelo de inteligência artificial utilizado pelo bot.

Responsável por:
- interpretação da linguagem
- geração das respostas
- raciocínio contextual

Modelo utilizado:

```text
gemini-2.5-flash
```

---

## 🔐 python-dotenv

Biblioteca responsável por carregar variáveis sensíveis do arquivo `.env`.

- token do Telegram
- API Key da Gemini

---

# 🔄 Sistema de Polling

A aplicação utiliza:

```python
app.run_polling()
```

Isso cria um loop contínuo que:
- consulta o Telegram
- verifica novas mensagens
- processa eventos

Funcionamento:

```text
while True:
    verificar mensagens novas
```

---

# ⚡ Sistema assíncrono

O projeto utiliza programação assíncrona através de:

```python
async / await
```

Isso permite:
- múltiplas requisições simultâneas
- melhor desempenho
- menor bloqueio da aplicação

---

# 🔐 Variáveis de ambiente

As credenciais ficam isoladas no arquivo:

```text
.env
```

Isso evita:
- vazamento de tokens
- exposição de chaves no GitHub

---

# ☁️ Hospedagem

A aplicação pode ser executada:
- localmente
- VPS Linux
- plataformas cloud
- Termux Android


---

# 📡 APIs utilizadas

## Telegram Bot API

Responsável pela comunicação entre:
- usuários
- Telegram
- bot

---

## Gemini API

Responsável pela geração das respostas inteligentes.

---

# 📂 Estrutura do projeto

```bash
telegram-bot/
│
├── main.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

---

# 🚀 Execução da aplicação

## Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Executar

```bash
python main.py
```

---

# 🎯 Objetivo do projeto

- integração de APIs
- desenvolvimento de bots
- utilização de IA generativa
- arquitetura backend simples
- automação de mensagens

---

# 📜 Licença

Projeto desenvolvido por: Gustavo Vinícius de Sousa Galvão.
Para fins educacionais e aprendizado.
