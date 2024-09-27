from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from urllib.parse import urlencode

# Comando de inicio para el bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy tu bot de generación de comprobantes.\n"
        "Usa los comandos /nequi o /bancolombia para generar un comprobante."
    )

# Comando para generar comprobante de Nequi
async def nequi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 3:
        await update.message.reply_text("Uso: /nequi <nombre> <numero> <valor>")
        return

    nombre = context.args[0]
    numero = context.args[1]
    valor = context.args[2]

    # Genera el URL del comprobante de Nequi
    base_url = "https://tuservidor.com/index_nequi.html"
    params = {
        "nombre": nombre,
        "numeroNequi": numero,
        "valor": valor
    }
    comprobante_url = f"{base_url}?{urlencode(params)}"
    
    await update.message.reply_text(f"Tu comprobante de Nequi está listo: {comprobante_url}")

# Comando para generar comprobante de Bancolombia
async def bancolombia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 3:
        await update.message.reply_text("Uso: /bancolombia <productoOrigen> <numeroCelular> <valorEnviado>")
        return

    producto_origen = context.args[0]
    numero_celular = context.args[1]
    valor_enviado = context.args[2]

    # Genera el URL del comprobante de Bancolombia
    base_url = "https://tuservidor.com/bancolombia.html"
    params = {
        "productoOrigen": producto_origen,
        "numeroCelular": numero_celular,
        "valorEnviado": valor_enviado
    }
    comprobante_url = f"{base_url}?{urlencode(params)}"
    
    await update.message.reply_text(f"Tu comprobante de Bancolombia está listo: {comprobante_url}")

# Configuración del bot
if __name__ == "__main__":
    # Usa el token que te proporcionó BotFather
    TOKEN = 'TU_TOKEN_DE_BOT_AQUÍ'

    # Crea la aplicación del bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Agrega los manejadores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("nequi", nequi))
    application.add_handler(CommandHandler("bancolombia", bancolombia))

    # Ejecuta el bot
    application.run_polling()
