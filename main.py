import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Carrega variáveis do .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv("chave_bot")
GEMINI_API_KEY = os.getenv("chave_gemini")

# Função que responde
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        mensagem_usuario = update.message.text

        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

        data = {
            "contents": [
                {
                    "parts": [{"text": mensagem_usuario}]
                }
            ]
        }

        response = requests.post(url, json=data)

        # DEBUG (ver no terminal se algo der errado)
        print("STATUS:", response.status_code)
        print("RESPOSTA:", response.text)

        if response.status_code != 200:
            await update.message.reply_text("Erro na API da Gemini.")
            return

        resposta_json = response.json()

        texto = None

        # Forma segura de pegar resposta
        if "candidates" in resposta_json:
            partes = resposta_json["candidates"][0].get("content", {}).get("parts", [])
            for parte in partes:
                if "text" in parte:
                    texto = parte["text"]
                    break

        if texto:
            await update.message.reply_text(texto)
        else:
            await update.message.reply_text("Não consegui gerar resposta.")
            print("Resposta inesperada:", resposta_json)

    except Exception as e:
        print("ERRO:", e)
        await update.message.reply_text("Erro ao processar sua mensagem.")

# Inicializa o bot
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Bot rodando...")
app.run_polling()