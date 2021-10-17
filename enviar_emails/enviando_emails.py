from dados_email import minha_senha, meu_email

# IMPORTS EMAIL 
from email.mime.multipart import MIMEMultipart
# Texto
from email.mime.text import MIMEText
# Imagem
from email.mime.image import MIMEImage

# Conecta no servidor GMAIL, o que vai mandar a mensagem
import smtplib

# Import de seus dados
meu_email = meu_email
minha_senha = minha_senha
email_recebedor = "E-MAIL PARA QUEM VOCÊ QUER ENVIAR"

print('Carregando o e-mail...')
for _ in range(1):  
    msg = MIMEMultipart()
    # Quem está enviando o e-mail
    msg['from'] = 'Christian Silveira'
    # Para quem vai o e-mail
    msg['to'] = email_recebedor 
    # O assunto do e-mail
    msg['subject'] = 'Sobre o e-mail'

    # Corpo do texto
    corpo = MIMEText(f'Teste isso aqui pra ver se da boa <br /><strong>DEUUU</strong>', 'html')
    msg.attach(corpo)

    # ENVIO DE IMAGEM EM ANEXO
    # Abrir a imagem na rota certa e salvar na variavel img
    with open('./enviar_emails/image.png', 'rb') as img:
        # Ler a imagem
        img = MIMEImage(img.read())
        msg.attach(img)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        try:
            # Msg de alo para o servidor
            smtp.ehlo() 
            # Ligando servidor
            smtp.starttls()
            # Fazendo login
            smtp.login(meu_email, minha_senha)
            # Enviando a mensagem
            smtp.send_message(msg)
            print('E-mail enviado com sucesso.')
        except Exception as e:
            print('E-mail não enviado...')
            print('Erro:', e)
