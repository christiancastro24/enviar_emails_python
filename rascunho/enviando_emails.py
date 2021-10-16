from string import Template
from datetime import datetime
from dados_email import minha_senha, meu_email

# IMPORTS EMAIL 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Conecta no servidor GMAIL, o que vai mandar a mensagem
import smtplib

meu_email = meu_email
minha_senha = minha_senha
email_recebedor = "e-mail para qual vai mandar"

print('Carregando o e-mail...')
for _ in range(1):
    # Abrir o index, r => leitura
    with open('./enviar_emails/index.html', 'r') as html:
        template = Template(html.read())
        data_atual = datetime.now().strftime('%d/%m/%Y')
        corpo_msg = template.safe_substitute(nome='christian silveira', data=data_atual) 

    msg = MIMEMultipart()
    # Quem está enviando o e-mail
    msg['from'] = 'Christian Silveira'
    # Para quem vai o e-mail
    msg['to'] = email_recebedor 
    # O assunto do e-mail
    msg['subject'] = 'Sobre o e-mail'

    corpo = MIMEText(corpo_msg, 'html')
    msg.attach(corpo)

     # ENVIO DE IMAGEM EM ANEXO
    with open('imgwes.png', 'rb') as img:
        img = MIMEImage(img.read())
        msg.attach(img)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        try:
            # Olá para o servidor
            smtp.ehlo()
            # Iniciando o servidor
            smtp.starttls()
            # Fazendo login
            smtp.login(meu_email, minha_senha)
            # Enviando a mensagem
            smtp.send_message(msg)
            print('E-mail enviado com sucesso.')
        except Exception as e:
            print('E-mail não enviado...')
            print('Erro:', e)


   