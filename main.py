from enviar_arquivo import EmailBot


if __name__ == "__main__":

    login = open("Arquivos/login.txt", "r").readlines()
    email = login[0]
    senha = login[1]
    enviar = EmailBot(email, senha)
    enviar.enviar_email()