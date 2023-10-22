from tkinter import *
from PIL import ImageTk, Image
import geopy
from geopy import distance
import csv
import pandas as pd

usuarios = []
viagens = []
pontos_turisticos = []

class PontoTuristico:
    def __init__(self, nome, descricao, latitude, longitude, avaliacao, cidade, tipo):
        self.nome = nome
        self.descricao = descricao
        self.latitude = latitude
        self.longitude = longitude
        self.avaliacao = avaliacao
        self.cidade = cidade
        self.tipo = tipo
    def getNome(self):
        return self.nome
    def getDescricao(self):
        return self.descricao

class User:
    def __init__(self, nome = None, email = None, senha = None, cidade_natal = None, gênero = None, idade = None):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cidade_natal = cidade_natal
        self.gênero = gênero
        self.idade = idade
        self.pontos_turisticos_visitados = []
        self.viagem = []

class Viagem:
    def __init__(self, transporte=None, n_pessoas=None, tipo_turismo=None, pto_partida=None):
        self.transporte = transporte
        self.n_pessoas = n_pessoas
        self.tipo_turismo = tipo_turismo
        self.pto_partida = pto_partida

with open('pto_tur.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ponto = PontoTuristico(row['nome'], row['descricao'], float(row['latitude']), float(row['longitude']), float(row['avaliacao']), row['cidade'], row['tipo'])
        pontos_turisticos.append(ponto)

with open('viagem.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        viagem = Viagem(row['transporte'], row['n_pessoas'], row['tipo_turismo'])
        viagens.append(viagem)

def fc_iniciar_viagem4(meio_transporte, qt_pessoa, tipo_turismo):
    usuarios[0].viagem.transporte = meio_transporte.get()
    usuarios[0].viagem.n_pessoas = qt_pessoa.get()
    usuarios[0].viagem.tipo_turismo = tipo_turismo.get()
    pg_iniciar_viagem4()

def pg_iniciar_viagem4():
    global current_page

    frame_iniciar_viagem = Frame(root)

    # create a label with text
    label1 = Label(frame_iniciar_viagem, text="Tudo pronto!", font=("Arial", 30))
    label1.pack(pady=10)
    label1.pack()

    texto = "Agora basta você\nentrar em contato com\no hotel escolhido.\nRealizar sua reserva,\npara o dia que desejar.\n\nE ao chegar, conte\nconosco, seremos o\nmelhor guia de viagem,\nque já conheceu.\n\nConhecemos todos os\npontos turisticos da\nregião, e também\no seu tipo de transporte,\nentão sem essa de que\nturistar é cansativo!\n\nAproveite a sua viagem\ncom a ROADUai\n"
    label2 = Label(frame_iniciar_viagem, text=texto, font=("Arial", 20))
    label2.pack(pady=20)
    label2.pack()

    # create a button widget for chosing
    aceitar_button = Button(frame_iniciar_viagem, text="Escolher", font=("Arial", 15), command=pg_explore)
    aceitar_button.pack(padx=5)

    frame_iniciar_viagem.pack()

    if current_page != None:
        current_page.pack_forget()
    frame_iniciar_viagem.pack()
    current_page = frame_iniciar_viagem


def pg_iniciar_viagem3():
    global current_page

    frame_iniciar_viagem = Frame(root)

    # create a label with text
    label1 = Label(frame_iniciar_viagem, text="Só mais algumas perguntinhas...", font=("Arial", 30))
    label1.pack(pady=10)
    label1.pack()

    # create a label with text
    label2 = Label(frame_iniciar_viagem, text="Você terá algum meio de transporte?", font=("Arial", 15))
    label2.pack(pady=10)

    # create an entry widget for e-mail
    meiotrans_entry = Entry(frame_iniciar_viagem, width=30, font=("Arial", 15))
    meiotrans_entry.pack(pady=10)

    # create a label with text
    label3 = Label(frame_iniciar_viagem, text="Com quantas pessoas você irá viajar?", font=("Arial", 15))
    label3.pack(pady=10)

    # create an entry widget for e-mail
    npessoas_entry = Entry(frame_iniciar_viagem, width=30, font=("Arial", 15))
    npessoas_entry.pack(pady=10)

    # create a label with text
    label4 = Label(frame_iniciar_viagem, text="Qual o tipo principal de turismo nessa viagem?", font=("Arial", 15))
    label4.pack(pady=10)

    # create an entry widget for e-mail
    tipoviagem_entry = Entry(frame_iniciar_viagem, width=30, font=("Arial", 15))
    tipoviagem_entry.pack(pady=10)

    frame_buttons = Frame(frame_iniciar_viagem)
    # create a button widget for going back
    voltar_button = Button(frame_buttons, text="Voltar", font=("Arial", 15), command=pg_explore)
    voltar_button.pack(padx=5, side="left")

    # create a button widget for chosing
    aceitar_button = Button(frame_buttons, text="Escolher", font=("Arial", 15), command=lambda: fc_iniciar_viagem4(meiotrans_entry, npessoas_entry, tipoviagem_entry))
    aceitar_button.pack(padx=5, side="left")

    frame_buttons.pack()

    if current_page != None:
        current_page.pack_forget()
    frame_iniciar_viagem.pack()
    current_page = frame_iniciar_viagem

def fc_iniciar_viagem3(hotel_entry):
    usuarios[0].viagem.hotel = hotel_entry.get()
    pg_iniciar_viagem3()

def pg_iniciar_viagem2():
    global current_page

    frame_iniciar_viagem = Frame(root)

    # create a label with text
    label1 = Label(frame_iniciar_viagem, text="Estamos quase lá!", font=("Arial", 30))
    label1.pack(pady=10)
    label1.pack()

    # create a label with text
    label2 = Label(frame_iniciar_viagem, text="Escolha um hotel", font=("Arial", 15))
    label2.pack(pady=10)

    # create an entry widget for e-mail
    hotel_entry = Entry(frame_iniciar_viagem, width=30, font=("Arial", 15))
    hotel_entry.pack(pady=10)

    frame_buttons = Frame(frame_iniciar_viagem)
    # create a button widget for going back
    voltar_button = Button(frame_buttons, text="Voltar", font=("Arial", 15), command=pg_explore)
    voltar_button.pack(padx=5, side="left")

    # create a button widget for chosing
    aceitar_button = Button(frame_buttons, text="Escolher", font=("Arial", 15), command=lambda: fc_iniciar_viagem3(hotel_entry))
    aceitar_button.pack(padx=5, side="left")

    frame_buttons.pack()

    if current_page != None:
        current_page.pack_forget()
    frame_iniciar_viagem.pack()
    current_page = frame_iniciar_viagem

def fc_iniciar_viagem2(city_entry):
    cidade_natal = city_entry.get()
    usuarios[0].viagem = Viagem()
    if cidade_natal == "CSA":
        cidade_natal = "-21.141034, -44.260823"
    usuarios[0].viagem.pto_partida = cidade_natal
    print(city_entry.get())
    pg_iniciar_viagem2()

def pg_iniciar_viagem():
    global current_page

    frame_iniciar_viagem = Frame(root)

    # create a label with text
    label1 = Label(frame_iniciar_viagem, text="Começar viagem!", font=("Arial", 30))
    label1.pack(pady=10)
    label1.pack()

    # create a label with text
    label2 = Label(frame_iniciar_viagem, text="Sua localizacao", font=("Arial", 15))
    label2.pack(pady=10)

    # create an entry widget for e-mail
    city_entry = Entry(frame_iniciar_viagem, width=30, font=("Arial", 15))
    city_entry.pack(pady=10)
    city_entry.get()

    frame_buttons = Frame(frame_iniciar_viagem)
    # create a button widget for going back
    voltar_button = Button(frame_buttons, text="Voltar", font=("Arial", 15), command=pg_explore)
    voltar_button.pack(padx=5, side="left")

    # create a button widget for chosing
    aceitar_button = Button(frame_buttons, text="Escolher", font=("Arial", 15), command=lambda: fc_iniciar_viagem2(city_entry))
    aceitar_button.pack(padx=5, side="left")

    frame_buttons.pack()

    if current_page != None:
        current_page.pack_forget()
    frame_iniciar_viagem.pack()
    current_page = frame_iniciar_viagem

def pg_visitar():
    global current_page

    frame_visitar = Frame(root)

    # open and resize the image
    img = Image.open("cachoeira-veu-da-noiva.png")
    img = img.resize((200, 200))

    # convert the image to a format that tkinter can use
    img_tk = ImageTk.PhotoImage(img)

    # create a label widget and set its image attribute
    label = Label(frame_visitar, image=img_tk)
    label.imagem = img_tk
    label.pack(pady=10)

    # create a label with text
    label1 = Label(frame_visitar, text="Cachoeira Veu da Noiva", font=("Arial", 20))
    label1.pack(pady=10)
    label1.pack()

    label2 = Label(frame_visitar, text="""Localizada em local de fácil acesso\n
a Cachoeira Veu da Noiva é uma das\n
mais populares na Serra do Cipó\n
pela facilidade de acesso e infraestrutura\n
para camping. Aqui no Portal Serra\n
do Cipó preparamos uma matéria detalhada\n
para você curtir a Cachoeira com\n
segurança e tranquilidade.""", font=("Arial", 15))
    label2.pack(pady=10)
    label2.pack()

    # create a frame with 3 buttons
    tinder = Frame(frame_visitar)

    # create the no button
    no_button = Button(tinder, text="Não", font=("Arial", 15), width=10, height=2)
    no_button.pack(padx=5, side="left")

    #create the already visited button
    already_visited_button = Button(tinder, text="Já visitei", font=("Arial", 15), width=10, height=2)
    already_visited_button.pack(padx=5, side="left")

    # create the yes button
    yes_button = Button(tinder, text="Sim", font=("Arial", 15), width=10, height=2)
    yes_button.pack(padx=5, side="left")

    tinder.pack()

    # go back frame
    frame_voltar = Frame(frame_visitar)
    # create the go back button 
    back_button = Button(frame_voltar, text="Voltar", font=("Arial", 8), width=10, height=2, command=pg_explore)
    back_button.pack(padx=5, side="right")
    frame_voltar.pack()

    if current_page != None:
        current_page.pack_forget()
    frame_visitar.pack()
    current_page = frame_visitar

def pg_restaurante():
    global current_page

    frame_restaurante = Frame(root)

    # open and resize the image
    img = Image.open("bar-do-tonho.png")
    img = img.resize((200, 200))

    # convert the image to a format that tkinter can use
    img_tk = ImageTk.PhotoImage(img)

    # create a label widget and set its image attribute
    label = Label(frame_restaurante, image=img_tk)
    label.imagem = img_tk
    label.pack(pady=10)

    # create a label with text
    label1 = Label(frame_restaurante, text="Bar do Tonho", font=("Arial", 20))
    label1.pack(pady=10)
    label1.pack()

    label2 = Label(frame_restaurante, text="Visite o Bar do Tonho e desfrute de\ncervejas geladas e saborosas porções!", font=("Arial", 20))
    label2.pack(pady=10)
    label2.pack()

    # create a frame with 3 buttons
    tinder = Frame(frame_restaurante)

    # create the no button
    no_button = Button(tinder, text="Não", font=("Arial", 15), width=10, height=2)
    no_button.pack(padx=5, side="left")

    #create the already visited button
    already_visited_button = Button(tinder, text="Já visitei", font=("Arial", 15), width=10, height=2)
    already_visited_button.pack(padx=5, side="left")

    # create the yes button
    yes_button = Button(tinder, text="Sim", font=("Arial", 15), width=10, height=2)
    yes_button.pack(padx=5, side="left")

    tinder.pack()

    # go back frame
    frame_voltar = Frame(frame_restaurante)
    # create the go back button 
    back_button = Button(frame_voltar, text="Voltar", font=("Arial", 8), width=10, height=2, command=pg_explore)
    back_button.pack(padx=5, side="right")
    frame_voltar.pack()


    if current_page != None:
        current_page.pack_forget()
    frame_restaurante.pack()
    current_page = frame_restaurante

def pg_hoteis():
    global current_page

    frame_hoteis = Frame(root)

    # open and resize the image
    img = Image.open("pousada-dos-viajantes.png")
    img = img.resize((200, 200))

    # convert the image to a format that tkinter can use
    img_tk = ImageTk.PhotoImage(img)

    # create a label widget and set its image attribute
    label = Label(frame_hoteis, image=img_tk)
    label.imagem = img_tk
    label.pack(pady=10)

    # create a label with text
    label1 = Label(frame_hoteis, text="Pousada dos Viajantes", font=("Arial", 20))
    label1.pack(pady=3)
    label1.pack()

    label2 = Label(frame_hoteis, text="""Localizado em Piedade do Rio Grande, o Hotel\n
Quincas e Restaurante é conhecido pela\n
sua tradicional culinária mineira e a\n
comodidade oferecida,  com uma \n
avaliação de 3,8 estrelas""", font=("Arial", 14))
    label2.pack(pady=3)
    label2.pack()

    # create a frame with 3 buttons
    tinder = Frame(frame_hoteis)

    # create the no button
    no_button = Button(tinder, text="Não", font=("Arial", 15), width=10, height=2)
    no_button.pack(padx=5, side="left")

    #create the already visited button
    already_visited_button = Button(tinder, text="Já visitei", font=("Arial", 15), width=10, height=2)
    already_visited_button.pack(padx=5, side="left")

    # create the yes button
    yes_button = Button(tinder, text="Sim", font=("Arial", 15), width=10, height=2)
    yes_button.pack(padx=5, side="left")

    tinder.pack()

    # go back frame
    frame_voltar = Frame(frame_hoteis)
    # create the go back button 
    back_button = Button(frame_voltar, text="Voltar", font=("Arial", 8), width=10, height=2, command=pg_explore)
    back_button.pack(padx=5, side="right")
    frame_voltar.pack()

    if current_page != None:
        current_page.pack_forget()
    frame_hoteis.pack()
    current_page = frame_hoteis

def calcular_distancias (longitude1, latitude1):
    
    coords_1 = (longitude1, latitude1)
    vetor_distancias = []
    global pontos_turisticos

    for ponto in pontos_turisticos:
        coord_2 = (ponto.longitude, ponto.latitude)
        dist = geopy.distance.geodesic(coords_1, coord_2).km

        vetor_distancias.append((ponto.nome, dist))

    sorted_list = sorted(vetor_distancias, key=lambda x: x[1])
    print(sorted_list)

    # pontos_turisticos = sorted(pontos_turisticos, key=lambda x: sorted_list.index(x.nome))
    pontos_turisticos = sorted(pontos_turisticos, key=lambda x: sorted_list.index(x.nome) if x.nome in sorted_list else len(sorted_list))
    print(pontos_turisticos[0])

def pg_explore():
    global current_page

    frame_explore = Frame(root)

    frame_titulo = Frame(frame_explore)

    # create a label with text
    label1 = Label(frame_titulo, text="ROADUai", font=("Arial", 30))
    label1.pack(padx=10, side="left")

    # open and resize the image
    img = Image.open("interface/user.png")
    img = img.resize((80, 80))

    # convert the image to a format that tkinter can use
    img_tk = ImageTk.PhotoImage(img)

    # create a label widget and set its image attribute
    label2 = Label(frame_titulo, image=img_tk)
    label2.imagem = img_tk
    label2.pack(pady=10, side="right")

    frame_titulo.pack()

    frame_titulo1 = Frame(frame_explore)

    # create a label with button
    label3 = Button(frame_titulo1, text="Iniciar Viagem", font=("Arial", 15), width=12, height=2, command=pg_iniciar_viagem)
    label3.pack(padx="5", pady="5", side="left")

    #create a label with button
    label4 = Button(frame_titulo1, text="Turistar", font=("Arial", 15), width=12, height=2, command=pg_visitar)
    label4.pack(padx="5", pady="5", side="left")

    frame_titulo1.pack()

    frame_titulo2 = Frame(frame_explore)

    # create a label with button
    label5 = Button(frame_titulo2, text="Hoteis", font=("Arial", 15), width=12, height=2, command=pg_hoteis)
    label5.pack(padx="5", pady="5",side="left")

    #create a label with button
    label6 = Button(frame_titulo2, text="Restaurantes", font=("Arial", 15), width=12, height=2, command=pg_restaurante)
    label6.pack(padx="5", pady="5", side="left")

    frame_titulo2.pack()

    frame_corpo = Frame(frame_explore)

    # create a label with text
    label7 = Label(frame_corpo, text="Começar viagem!", font=("Arial", 15))
    label7.pack(pady=10)

    # create a label with text
    label8 = Label(frame_corpo, text="Escolha um dos pontos\n sugeridos para começar sua viagem!", font=("Arial", 12))
    label8.pack(pady=10)
    
    frame_corpo.pack()

    frame_carrocel = Frame(frame_explore)


    # create the back button
    back_button_img = Image.open("interface/back.png")
    back_button_img = back_button_img.resize((50, 50))
    back_button_img_tk = ImageTk.PhotoImage(back_button_img)
    back_button = Button(frame_carrocel, image=back_button_img_tk)
    back_button.image = back_button_img_tk
    back_button.place(relx=0, rely=0.5, anchor="w")

    # create the forward button
    foward_button_img = Image.open("interface/foward.png")
    foward_button_img = foward_button_img.resize((50, 50))
    foward_button_img_tk = ImageTk.PhotoImage(foward_button_img)
    foward_button = Button(frame_carrocel, image=foward_button_img_tk)
    foward_button.image = foward_button_img_tk
    foward_button.place(relx=1, rely=0.5, anchor="e")

    # open and resize the image
    img_dentro_carrocel = Image.open("Igreja-Nossa-Senhora-do-Rosário.png")
    img_dentro_carrocel = img_dentro_carrocel.resize((200, 200))

    # convert the image to a format that tkinter can use
    img_tk_carrocel = ImageTk.PhotoImage(img_dentro_carrocel)

    # create a label widget and set its image attribute
    label_imagem_carrocel = Label(frame_carrocel, image=img_tk_carrocel)
    label_imagem_carrocel.imagem = img_tk_carrocel
    label_imagem_carrocel.pack(pady=10)

    # create a label with text
    label_nome_carrocel = Label(frame_carrocel, text="Igreja São Francisco", font=("Arial", 15))
    label_nome_carrocel.pack(pady=10)

    descricao = """A Igreja de São Francisco de Assis é\n
    um templo católico fundado pela Venerável\n
    Ordem Terceira de São Francisco de Assis\n
    na cidade brasileira de São João del-Rei,\n
    no estado de Minas Gerais."""
    # create a label with text
    label_descricao_carrocel = Label(frame_carrocel, text=descricao, font=("Arial", 15))
    label_descricao_carrocel.pack(pady=2)

    frame_carrocel.pack()

    if current_page != None:
        current_page.pack_forget()
    frame_explore.pack()
    current_page = frame_explore

def get_value(email, senha):
    email_value = email.get()
    senha_value = senha.get()
    usuarios[0].email = email_value
    usuarios[0].senha = senha_value
    pg_explore()

def pg_email():
    global current_page

    frame_email = Frame(root)

    # open and resize the image
    img = Image.open("logo.png")
    img = img.resize((200, 200))

    # convert the image to a format that tkinter can use
    img_tk = ImageTk.PhotoImage(img)

    # create a label widget and set its image attribute
    label = Label(frame_email, image=img_tk)
    label.imagem = img_tk
    label.pack(pady=10)

    # create a label with text
    label1 = Label(frame_email, text="e-mail", font=("Arial", 15))
    label1.pack(pady=10)

    # create an entry widget for e-mail
    email_entry = Entry(frame_email, width=30, font=("Arial", 15))
    email_entry.pack(pady=10)

    # create a label with text
    label2 = Label(frame_email, text="senha", font=("Arial", 15))
    label2.pack(pady=10)

    # create an entry widget for password
    password_entry = Entry(frame_email, width=30, font=("Arial", 15))
    password_entry.pack(pady=10)

    # create a label with text
    label3 = Label(frame_email, text="Esqueceu sua senha?", font=("Arial", 10))
    label3.pack(pady=2)

    frame_buttons = Frame(frame_email)
    # create a button widget for login
    login_button = Button(frame_buttons, text="Entrar", font=("Arial", 15), command=lambda: get_value(email_entry, password_entry))
    login_button.pack(padx=5, side="left")

    # create a button widget for password
    password_button = Button(frame_buttons, text="Criar conta", font=("Arial", 15))
    password_button.pack(padx=5, side="left")

    frame_buttons.pack()

    if current_page != None:
        current_page.pack_forget()
    frame_email.pack()
    current_page = frame_email

def pg_login(warning = None):
    frame_login = Frame(root)

    # open and resize the image
    img = Image.open("logo.png")
    img = img.resize((200, 200))

    # convert the image to a format that tkinter can use
    img_tk = ImageTk.PhotoImage(img)

    # create a label widget and set its image attribute
    label = Label(frame_login, image=img_tk)
    label.imagem = img_tk
    label.pack(pady=10)

    # create a label with text
    label1 = Label(frame_login, text="ROADUai", font=("Arial", 30))
    label1.pack(pady=10)
    label1.pack()

    # create a label with text
    label2 = Label(frame_login, text="O seu guia de turismo favorito!", font=("Arial", 20))
    label2.pack(pady=10)
    label2.pack()

    # create a label with text
    label3 = Label(frame_login, text="Ao continuar você está concordando com nossos\nTermos de uso e confirmando ter lido\nnossa politica de privacidade e uso de cookies", font=("Arial", 10))
    label3.pack(pady=10)
    label3.pack()

    # create an entry widget for login with google
    username_entry = Button(frame_login, height=2, width=20, text="Continuar com o google", font=("Arial", 20))
    username_entry.pack(pady=(100,5))
    username_entry.pack()
    # create an entry widget for login with e-mail
    email_entry = Button(frame_login, height=2, width=20, text="Continuar com e-mail", font=("Arial", 20), command=pg_email)
    email_entry.pack(pady=10)
    email_entry.pack()

    # changing root frame to frame_login frame forgetint the current frame
    global current_page
    current_page = None
    if current_page != None:
        current_page.pack_forget()
    frame_login.pack()
    current_page = frame_login



def main():
    # pg_login()
    # global variable root
    global root
    root = Tk()
    root.geometry("540x960")
    root.title("ROADUai")
    usuarios.append(User())
    #execute page
    pg_login() 
    root.mainloop()
    #spliting the string
    latitude, longitude = usuarios[0].viagem.pto_partida.split(", ")
    calcular_distancias(latitude, longitude)

main()
