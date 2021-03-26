import email.message
import smtplib
from dados_planilha import DadosPlanilha


class EmailBot:
    def __init__(self, email_from, senha):
        self.email_from = email_from
        self.senha = senha
        self.email_enviar = DadosPlanilha().email
        self.computador = DadosPlanilha().computadores
        self.nome01 = DadosPlanilha().nomes

    def enviar_email(self):
        cont = -1
        for emails in self.email_enviar:
            cont += 1
            corpo_email = f"""
                <p>Prezado, {self.nome01[cont]} </p>
                <p> O Computador {self.computador[cont]}, precisa de atualização </p>
                <p> Segue o procedimento anexo abaixo<p/>
        
            
            """
            try:
                msg = email.message.Message()
                msg["Subject"] = "Atualização do Windows"
                msg["From"] = self.email_from
                msg["To"] = emails
                msg.add_header("Content-Type", "text/html")
                msg.set_payload(corpo_email)
                s = smtplib.SMTP("smtp.gmail.com:587")
                s.starttls()
                s.login(msg["From"], self.senha)
                s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
                print("Email Enviado")
            except:
                print("Email não Enviado")
