import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

# Carrega as variáveis do arquivo .env
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
SMTP_SERVER = "smtp.gmail.com"  # Servidor SMTP do Gmail
SMTP_PORT = 587  # Porta padrão para TLS

def scrap_headlines():
    # URL do site de notícias
    url = "https://www.cnnbrasil.com.br/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Seleciona os títulos das manchetes principais
    headlines = []
    for headline in soup.find_all("h3", class_="block__news__title"):
        title = headline.get_text(strip=True)
        headlines.append(title)

    return headlines

def send_email(content):
    # Configura o e-mail
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = "Resumo das Principais Notícias do Dia"

    # Corpo do e-mail
    body = f"As principais manchetes do dia são:\n\n" + "\n".join(content)
    msg.attach(MIMEText(body, "plain"))

    # Envia o e-mail
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Segurança de conexão
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, RECEIVER_EMAIL, msg.as_string())
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

# Executa a função para capturar manchetes e envia o e-mail
headlines = scrap_headlines()
if headlines:
    send_email(headlines)
else:
    print("Nenhuma manchete encontrada.")
