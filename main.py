import time
import ttkbootstrap
from ttkbootstrap.dialogs import Messagebox
import ttkbootstrap as ttk
from ttkbootstrap.tableview import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import mysql.connector
import pandas as pd
import random
import threading
from pathlib import Path
import requests
import sqlite3
from tkinter import *
import re
from placeholder import EntPlaceHold
from tkinter import simpledialog
from random import randint

class application():

    def lista_busca_relatorio(self):
        self.res_data_relatorio = self.busca.entry.get()
        self.data1 = self.res_data_relatorio[0:2]
        self.data2 = self.res_data_relatorio[3:5]
        self.data3 = self.res_data_relatorio[6:10]
        self.data_convertida = self.data3 + "-" + self.data2 + "-" + self.data1
        print(self.data_convertida)
        self.res_data_relatorio2 = self.busca2.entry.get()
        self.data4 = self.res_data_relatorio2[0:2]
        self.data5 = self.res_data_relatorio2[3:5]
        self.data6 = self.res_data_relatorio2[6:10]
        self.data_convertida2 = self.data6 + "-" + self.data5 + "-" + self.data4
        print(self.data_convertida2)
        self.banco = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database='racao'
        )
        self.cursor = self.banco.cursor()
        self.query_busca = (f""" SELECT * FROM relatorio
                    WHERE Data BETWEEN '{self.data_convertida}' and '{self.data_convertida2}' ORDER BY id ASC   """)
        self.res = self.cursor.execute(self.query_busca)
        self.res_busca = self.cursor.fetchall()
        print(self.res_busca)
        self.delete_pages()
        colors = self.app.style.colors
        coldata = [
            "Id",
            "Nome",
            "Código",
            "Silo",
            "Milho",
            "Farelo de Soja",
            "Farelo de Carne",
            "Farelo de Trigo",
            "Óleo",
            "Núcleo",
            "Metionina",
            "Ração Kg",
            "Data",
            "Hora"
        ]
        self.rowdata_busca = self.res_busca
        self.dt = Tableview(
            master=self.main_frame2,
            coldata=coldata,
            rowdata=self.rowdata_busca,
            paginated=True,
            searchable=True,
            bootstyle=LIGHT,
            stripecolor=(colors.light, None),
        )
        self.dt.autofit_columns()
        self.dt.pack(fill=BOTH, expand=YES, padx=5, pady=5)

    def func_buscar(self):
        self.res_data_relatorio = self.busca.entry.get()
        self.data1 = self.res_data_relatorio[0:2]
        self.data2 = self.res_data_relatorio[3:5]
        self.data3 = self.res_data_relatorio[6:10]
        self.data_convertida = self.data3 +"-"+ self.data2 +"-"+ self.data1
        print(self.data_convertida)
        self.res_data_relatorio2 = self.busca2.entry.get()
        self.data4 = self.res_data_relatorio2[0:2]
        self.data5 = self.res_data_relatorio2[3:5]
        self.data6 = self.res_data_relatorio2[6:10]
        self.data_convertida2 = self.data6 + "-" + self.data5 + "-" + self.data4
        print(self.data_convertida2)

    def busca_relatorio(self):
        self.busca = ttk.DateEntry(self.main_frame)
        self.busca.pack()
        self.busca2 = ttk.DateEntry(self.main_frame)
        self.busca2.pack()
        self.btn_buscar_relatorio = ttk.Button(self.main_frame, text="Buscar!", command=self.lista_busca_relatorio)
        self.btn_buscar_relatorio.pack()

    def relatorio(self):
        self.banco = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database='racao'
        )
        self.cursor = self.banco.cursor()
        self.query = (""" SELECT * FROM relatorio ORDER BY id ASC
                                                                       """)
        self.res = self.cursor.execute(self.query)
        self.rela = self.cursor.fetchall()
        colors = self.app.style.colors
        coldata = [
            "Id",
            "Nome",
            "Código",
            "Silo",
            "Milho",
            "Farelo de Soja",
            "Farelo de Carne",
            "Farelo de Trigo",
            "Óleo",
            "Núcleo",
            "Metionina",
            "Ração Kg",
            "Data",
            "Hora"
        ]
        self.rowdata = self.rela
        self.dt = Tableview(
            master=self.main_frame2,
            coldata=coldata,
            rowdata=self.rowdata,
            paginated=True,
            searchable=True,
            bootstyle=LIGHT,
            stripecolor=(colors.light, None),
        )
        self.dt.autofit_columns()
        self.dt.pack(fill=BOTH, expand=YES, padx=5, pady=5)

    def center(self,win):
        
        win.update_idletasks()  # Update "requested size" from geometry manager
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def informar_batelada(self):
        self.janela3 = tk.Toplevel()
        self.janela3.geometry('300x250')
        self.center(self.janela3)
        self.janela3.title('Bateladas')
        self.img_enviar_batelada = PhotoImage(file=r"assets/enviar.png")
        self.frame_janela3 = ttk.Frame(self.janela3, bootstyle="light")
        self.frame_janela3.place(height=250, width=300)
        self.lb_batelada = ttk.Label(self.frame_janela3, text= "Bateladas", font=('Arial', 9), bootstyle="inverse-light")
        self.lb_batelada.pack(pady=30)
        self.entry_batelada = ttk.Entry(self.frame_janela3)
        self.entry_batelada.pack()
        self.btn_bateladas = ttk.Button(self.frame_janela3, text="Enviar!",bootstyle='light', image=self.img_enviar_batelada, command=self.simulacao )
        self.btn_bateladas.pack(pady=10)

    def simulacao(self):
        self.nome_enviar = self.entry_nome_gerar.get()
        self.codigo_enviar = self.entry_codigo_gerar.get()
        self.silo_enviar = randint(0,4)
        self.milho_enviar = self.entry_milho_gerar.get()
        self.farelodesoja_enviar = self.entry_farelodesoja_gerar.get()
        self.farelodecarne_enviar = self.entry_farelodecarne_gerar.get()
        self.farelodetrigo_enviar = self.entry_farelodetrigo_gerar.get()
        self.oleo_enviar = self.entry_oleo_gerar.get()
        self.nucleo_enviar = self.entry_nucleo_gerar.get()
        self.metionina_enviar = self.entry_metionina_gerar.get()
        self.quantidade = randint(900,1000)
        self.res_batelada = self.entry_batelada.get()
        print(self.silo_enviar)
        print(self.quantidade)
        self.janela3.destroy()
        time.sleep(10)
        self.banco = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database='racao'
        )
        self.cursor = self.banco.cursor()
        self.query_batelada = (f""" INSERT INTO relatorio(Nome, Codigo, Silo, Milho, Farelodesoja, Farelodecarne, Farelodetrigo, Oleo, Nucleo, Metionina, RacaoKG) VALUES('{self.nome_enviar}', '{self.codigo_enviar}','{self.silo_enviar}', '{self.milho_enviar}', '{self.farelodesoja_enviar}', '{self.farelodecarne_enviar}', '{self.farelodetrigo_enviar}', '{self.oleo_enviar}', '{self.nucleo_enviar}', '{self.metionina_enviar}','{self.quantidade}')
                                                            """)
        self.res = self.cursor.execute(self.query_batelada)
        self.banco.commit()
        Messagebox.show_info("Batelada finalizada e adicionada com sucesso!")


    def limpar_entry_cadastro(self):
        self.entry_nome.delete('0', 'end')
        self.entry_codigo.delete('0', 'end')
        self.entry_milho.delete('0', 'end')
        self.entry_farelodesoja.delete('0', 'end')
        self.entry_farelodecarne.delete('0', 'end')
        self.entry_farelodetrigo.delete('0', 'end')
        self.entry_oleo.delete('0', 'end')
        self.entry_nucleo.delete('0', 'end')
        self.entry_metionina.delete('0', 'end')


    def delete_pages_principal(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()
        for frame in self.main_frame2.winfo_children():
            frame.destroy()


    def delete_pages(self):
        for frame in self.main_frame2.winfo_children():
            frame.destroy()

    def excluir_linha(self):
        Item = self.dt.get_rows(selected=True)
        self.id_excluir = Item[0].values
        self.id_excluir2 = self.id_excluir[0]
        print(self.id_excluir2)
        self.banco = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database='racao'
        )
        self.cursor = self.banco.cursor()
        self.query_excluir = (
            f""" DELETE FROM produto WHERE id = {self.id_excluir2}""")
        self.cursor.execute(self.query_excluir)
        self.banco.commit()
        self.delete_pages()
        self.lista_racao()

    def editar_final(self):

        self.info_nome = self.entry_nome_editar.get()
        self.info_codigo = self.entry_codigo_editar.get()
        self.info_milho = self.entry_milho_editar.get()
        self.info_farelodesoja = self.entry_farelodesoja_editar.get()
        self.info_farelodecarne = self.entry_farelodecarne_editar.get()
        self.info_farelodetrigo = self.entry_farelodetrigo_editar.get()
        self.info_oleo = self.entry_oleo_editar.get()
        self.info_nucleo = self.entry_nucleo_editar.get()
        self.info_metionina = self.entry_metionina_editar.get()
        print(self.info_codigo)
        self.banco = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database='racao'
        )
        self.cursor = self.banco.cursor()
        self.query = (
            f""" UPDATE
                    produto 
                 SET 
                    Nome = '{self.info_nome}',
                    Codigo = '{self.info_codigo}',
                    Milho = '{self.info_milho}',
                    Farelodesoja = '{self.info_farelodesoja}',
                    Farelodecarne = '{self.info_farelodecarne}',
                    Farelodetrigo = '{self.info_farelodetrigo}',
                    Oleo = '{self.info_oleo}',
                    Nucleo = '{self.info_nucleo}',
                    Metionina = '{self.info_metionina}'
                    WHERE
                        id = {self.id_editar}
                    
                                                                """)
        self.res = self.cursor.execute(self.query)
        self.banco.commit()
        self.delete_pages()
        self.lista_racao()
        self.janela2.destroy()

    def editar(self):
        self.janela2 = tk.Toplevel()
        self.center(self.janela2)
        self.janela2.geometry('700x300')
        self.janela2.title('Editar Ração')
        self.frame_janela2 = ttk.Frame(self.janela2, bootstyle="light")
        self.frame_janela2.place(height=300, width=700)
        Item = self.dt.get_rows(selected=True)
        self.img_enviar = PhotoImage(file=r"assets/enviar.png")

        self.lb_nome_editar = ttk.Label(self.frame_janela2, text="Nome:", bootstyle='inverse-light')
        self.lb_nome_editar.place(relx=0.1, rely=0.18)
        self.entry_nome_editar = ttk.Entry(self.frame_janela2)
        self.entry_nome_editar.place(relx = 0.16, rely=0.165)

        self.lb_codigo_editar = ttk.Label(self.frame_janela2, text="Código:", bootstyle='inverse-light')
        self.lb_codigo_editar.place(relx=0.092, rely=0.30)
        self.entry_codigo_editar = ttk.Entry(self.frame_janela2)
        self.entry_codigo_editar.place(relx=0.16, rely=0.285)

        self.lb_milho_editar = ttk.Label(self.frame_janela2, text="Milho:", bootstyle='inverse-light')
        self.lb_milho_editar.place(relx=0.102, rely=0.42)
        self.entry_milho_editar = ttk.Entry(self.frame_janela2)
        self.entry_milho_editar.place(relx=0.16, rely=0.405)

        self.lb_farelodesoja_editar = ttk.Label(self.frame_janela2, text="Frl Sója:", bootstyle='inverse-light')
        self.lb_farelodesoja_editar.place(relx=0.375, rely=0.18)
        self.entry_farelodesoja_editar = ttk.Entry(self.frame_janela2)
        self.entry_farelodesoja_editar.place(relx=0.446, rely=0.165)

        self.lb_farelodecarne_editar = ttk.Label(self.frame_janela2, text="Frl Carne:", bootstyle='inverse-light')
        self.lb_farelodecarne_editar.place(relx=0.3630, rely=0.30)
        self.entry_farelodecarne_editar = ttk.Entry(self.frame_janela2)
        self.entry_farelodecarne_editar.place(relx=0.446, rely=0.285)

        self.lb_farelodetrigo_editar = ttk.Label(self.frame_janela2, text="Frl Trigo:", bootstyle='inverse-light')
        self.lb_farelodetrigo_editar.place(relx=0.3681, rely=0.42)
        self.entry_farelodetrigo_editar = ttk.Entry(self.frame_janela2)
        self.entry_farelodetrigo_editar.place(relx=0.446, rely=0.405)

        self.lb_oleo_editar = ttk.Label(self.frame_janela2, text="Óleo:", bootstyle='inverse-light')
        self.lb_oleo_editar.place(relx=0.664, rely=0.18)
        self.entry_oleo_editar = ttk.Entry(self.frame_janela2)
        self.entry_oleo_editar.place(relx=0.712, rely=0.165)

        self.lb_nucleo_editar = ttk.Label(self.frame_janela2, text="Núcleo:", bootstyle='inverse-light')
        self.lb_nucleo_editar.place(relx=0.645, rely=0.30)
        self.entry_nucleo_editar = ttk.Entry(self.frame_janela2)
        self.entry_nucleo_editar.place(relx=0.712, rely=0.285)

        self.lb_metionina_editar = ttk.Label(self.frame_janela2, text="Metion:", bootstyle='inverse-light')
        self.lb_metionina_editar.place(relx=0.645, rely=0.42)
        self.entry_metionina_editar = ttk.Entry(self.frame_janela2)
        self.entry_metionina_editar.place(relx=0.712, rely=0.405)

        self.btn_editar_final = ttk.Button(self.frame_janela2, text="Finalizar", image=self.img_editar, bootstyle="light", command=self.editar_final)
        self.btn_editar_final.place(relx=0.46, rely=0.650)

        self.res_editar = Item[0].values
        self.id_editar = self.res_editar[0]
        print(self.id_editar)
        self.entry_nome_editar.delete('0', 'end')
        self.entry_nome_editar.insert(END, self.res_editar[1])
        self.entry_codigo_editar.delete('0', 'end')
        self.entry_codigo_editar.insert(END, self.res_editar[2])
        self.entry_milho_editar.delete('0', 'end')
        self.entry_milho_editar.insert(END, self.res_editar[3])
        self.entry_farelodesoja_editar.delete('0', 'end')
        self.entry_farelodesoja_editar.insert(END, self.res_editar[4])
        self.entry_farelodecarne_editar.delete('0', 'end')
        self.entry_farelodecarne_editar.insert(END, self.res_editar[5])
        self.entry_farelodetrigo_editar.delete('0', 'end')
        self.entry_farelodetrigo_editar.insert(END, self.res_editar[6])
        self.entry_oleo_editar.delete('0', 'end')
        self.entry_oleo_editar.insert(END, self.res_editar[7])
        self.entry_nucleo_editar.delete('0', 'end')
        self.entry_nucleo_editar.insert(END, self.res_editar[8])
        self.entry_metionina_editar.delete('0', 'end')
        self.entry_metionina_editar.insert(END, self.res_editar[9])


    def cadastrar(self):
        self.nome = self.entry_nome.get()
        self.codigo = self.entry_codigo.get()
        self.milho = self.entry_milho.get()
        self.farelodesoja = self.entry_farelodesoja.get()
        self.farelodecarne = self.entry_farelodecarne.get()
        self.farelodetrigo = self.entry_farelodetrigo.get()
        self.oleo = self.entry_oleo.get()
        self.nucleo = self.entry_nucleo.get()
        self.metionina = self.entry_metionina.get()
        if self.entry_nome == 'Digite o nome' or self.codigo == 'Digite o código' or self.milho == 'Milho em Kg' or self.farelodesoja == 'Farelo de Soja em Kg' or self.farelodecarne == 'Farelo de Carne em Kg' or self.farelodetrigo == 'Farelo de Trigo em Kg' or self.oleo == 'Óleo em Kg' or self.nucleo == 'Núcleo' or self.metionina == 'Metionina Kg':
            Messagebox.show_error("Preencha todos os campos")
        else:
            self.banco = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                passwd="",
                database='racao'
                )
            self.cursor = self.banco.cursor()
            self.query_validar = (f""" SELECT Nome FROM produto WHERE Nome = '{self.nome}'
                                    """)
            self.query = (f""" INSERT INTO produto(Nome, Codigo, Milho, Farelodesoja, Farelodecarne, Farelodetrigo, Oleo, Nucleo, Metionina) VALUES('{self.nome}', '{self.codigo}', '{self.milho}', '{self.farelodesoja}', '{self.farelodecarne}', '{self.farelodetrigo}', '{self.oleo}', '{self.nucleo}', '{self.metionina}')
                                                            """)
            self.res = self.cursor.execute(self.query_validar)
            self.res_validar = self.cursor.fetchall()
            print(self.res_validar)

            if len(self.res_validar) != 0:  # Verifica se o retorno contém alguma linha
                Messagebox.show_error("Este nome de ração ja existe!")

            else:
                self.query_validar2 = (f""" SELECT Codigo FROM produto WHERE Codigo = '{self.codigo}'
                                                    """)
                self.res3 = self.cursor.execute(self.query_validar2)
                self.res_validar2 = self.cursor.fetchall()
                print("validando codigo")
                if len(self.res_validar2) != 0:  # Verifica se o retorno contém alguma linha
                    Messagebox.show_error("Este codigo ja existe!")
                else:
                    self.res = self.cursor.execute(self.query)
                    self.banco.commit()
                    self.delete_pages()
                    self.lista_racao()
                    self.formulario()

    def dados(self):
        self.banco = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database='racao'
        )
        self.cursor = self.banco.cursor()
        self.query = (""" SELECT * FROM produto ORDER BY id ASC
                                                """)
        self.res = self.cursor.execute(self.query)

    def conectar(self):
        self.banco = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database='racao'
        )


        self.cursor = self.banco.cursor()

        # self.cursor.execute("""DELETE FROM clientes
        # WHERE id = 4;""")
        self.cursor.execute("INSERT INTO produto(Nome, Codigo, Milho, Farelodesoja, Farelodecarne, Farelodetrigo, Oleo, Nucleo, Metionina) VALUES('Raçãonometal', 0001, 600, 200, 150, 170, 25, 40, 10)")
            #f"INSERT INTO produto(Nome, Codigo, Milho, Farelo de Soja, Farelo de Carne, Farelo de Trigo, Oleo, Núcleo, Metionina) VALUES('{self.nome}', '{self.codigo}', '{self.milho}', '{self.farelo_de_soja}', '{self.farelo_de_carne}', '{self.farelo_de_trigo}', '{self.oleo}', '{self.nucleo}', '{self.metionina}')")
        # self.cursor.execute("""INSERT INTO clientes(nome, logradouro, complemento, bairro, cep, telefone) VALUES('gabriel', 'rua dos eucalipstos', 'numero 527', 'canasvieiras', 88054150, 48996967749)""")
        self.banco.commit()

    def pegar(self):

        Item = self.dt.get_rows(selected=True)
        print (Item[0].values)

    def formulario(self):

        self.img_add = PhotoImage(file=r"sinal-de-mais.png")
        self.img_editar = PhotoImage(file=r"assets/editar.png")
        self.img_excluir = PhotoImage(file=r"assets/excluir.png")

        self.lb_nome = ttk.Label(self.main_frame, text="Nome", font=('Arial', 7), bootstyle="inverse-light")
        self.lb_nome.place(relx=0.159, rely=0.165)
        self.lb_codigo = ttk.Label(self.main_frame, text="Código", font=('Arial', 7), bootstyle="inverse-light")
        self.lb_codigo.place(relx=0.159, rely=0.275)
        self.lb_milho = ttk.Label(self.main_frame, text="Milho", font=('Arial', 7), bootstyle="inverse-light")
        self.lb_milho.place(relx=0.159, rely=0.375)
        self.lb_farelodesoja = ttk.Label(self.main_frame, text="Farelo de soja", font=('Arial', 7), bootstyle="inverse-light")
        self.lb_farelodesoja.place(relx=0.409, rely=0.165)
        self.lb_farelodecarne = ttk.Label(self.main_frame, text="Farelo de Carne", font=('Arial', 7),bootstyle="inverse-light")
        self.lb_farelodecarne.place(relx=0.409, rely=0.275)
        self.lb_farelodetrigo = ttk.Label(self.main_frame, text="Farelo de Trigo", font=('Arial', 7), bootstyle="inverse-light")
        self.lb_farelodetrigo.place(relx=0.409, rely=0.375)
        self.lb_oleo = ttk.Label(self.main_frame, text="Óleo", font=('Arial', 7), bootstyle="inverse-light")
        self.lb_oleo.place(relx=0.659, rely=0.165)
        self.lb_nucleo = ttk.Label(self.main_frame, text="Núcleo", font=('Arial', 7), bootstyle="inverse-light")
        self.lb_nucleo.place(relx=0.659, rely=0.275)
        self.lb_metionina = ttk.Label(self.main_frame, text="Metionina", font=('Arial', 7),  bootstyle="inverse-light")
        self.lb_metionina.place(relx=0.659, rely=0.375)

        self.entry_nome = EntPlaceHold(self.main_frame, 'Digite o nome')
        self.entry_nome.place(relx=0.16, rely=0.2, height=25, width=150)

        self.entry_codigo = EntPlaceHold(self.main_frame, 'Digite o código')
        self.entry_codigo.place(relx=0.16, rely=0.31, height=25, width=150)

        self.entry_milho = EntPlaceHold(self.main_frame, 'Milho em Kg')
        self.entry_milho.place(relx=0.16, rely=0.41, height=25, width=150)

        self.entry_farelodesoja = EntPlaceHold(self.main_frame, 'Farelo de Soja em Kg')
        self.entry_farelodesoja.place(relx=0.41, rely=0.2, height=25, width=150)

        self.entry_farelodecarne = EntPlaceHold(self.main_frame, 'Farelo de Carne em Kg')
        self.entry_farelodecarne.place(relx=0.41, rely=0.31, height=25, width=150)

        self.entry_farelodetrigo = EntPlaceHold(self.main_frame, 'Farelo de Trigo em Kg')
        self.entry_farelodetrigo.place(relx=0.41, rely=0.41, height=25, width=150)

        self.entry_oleo = EntPlaceHold(self.main_frame, 'Óleo em Kg')
        self.entry_oleo.place(relx=0.66, rely=0.2, height=25, width=150)

        self.entry_nucleo = EntPlaceHold(self.main_frame, 'Núcleo em Kg')
        self.entry_nucleo.place(relx=0.66, rely=0.31, height=25, width=150)

        self.entry_metionina = EntPlaceHold(self.main_frame, 'Metionina Kg')
        self.entry_metionina.place(relx=0.66, rely=0.41, height=25, width=150)

        self.btn_cadastrar = ttk.Button(self.main_frame, text="Cadastrar", image=self.img_add, bootstyle="light", command = self.cadastrar)
        self.btn_cadastrar.place(x=490, y=250)

        self.btn_editar = ttk.Button(self.main_frame, text="Editar", image=self.img_editar, bootstyle="light", command=self.editar)
        self.btn_editar.place(x=590, y=250)

        self.btn_excluir = ttk.Button(self.main_frame, text="Excluir",image=self.img_excluir, bootstyle="light", command=self.excluir_linha)
        self.btn_excluir.place(x=690, y=250)

    def lista_racao(self):
        self.banco =  mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database='racao'
        )
        self.cursor = self.banco.cursor()
        self.query = (""" SELECT * FROM produto ORDER BY id ASC
                                                       """)

        self.res = self.cursor.execute(self.query)
        self.r = self.cursor.fetchall()
        colors = self.app.style.colors

        coldata = [
            "Id",
            "Nome",
            "Código",
            "Milho",
            "Farelo de Soja",
            "Farelo de Carne",
            "Farelo de Trigo",
            "Óleo",
            "Núcleo",
            "Metionina",

        ]

        self.rowdata = self.r

        self.dt = Tableview(
            master=self.main_frame2,
            coldata=coldata,
            rowdata=self.rowdata,
            paginated=True,
            searchable=True,

            bootstyle=LIGHT,
            stripecolor=(colors.light, None),
        )
        self.dt.autofit_columns()
        self.dt.pack(fill=BOTH, expand=YES, padx=5, pady=5)

    def pegar_lista_gerar(self):
        Item = self.dt.get_rows(selected=True)
        print(Item[0].values)
        self.resultado = Item[0].values
        self.lb_nome_gerar = ttk.Label(self.main_frame, text="Nome", font=('Arial', 7), bootstyle="inverse-light")
        self.lb_nome_gerar.place(relx=0.159, rely= 0.165)
        self.lb_codigo_gerar = ttk.Label(self.main_frame, text="Código", font=('Arial', 7), bootstyle="inverse-light")
        self.lb_codigo_gerar.place(relx=0.159, rely=0.275)
        self.lb_milho_gerar = ttk.Label(self.main_frame, text="Milho", font=('Arial', 7), bootstyle="inverse-light")
        self.lb_milho_gerar.place(relx=0.159, rely=0.375)
        self.lb_farelodesoja_gerar = ttk.Label(self.main_frame, text="Farelo de soja", font=('Arial', 7), bootstyle="inverse-light")
        self.lb_farelodesoja_gerar.place(relx=0.409, rely=0.165)
        self.lb_farelodecarne_gerar = ttk.Label(self.main_frame, text="Farelo de Carne", font=('Arial', 7),bootstyle="inverse-light")
        self.lb_farelodecarne_gerar.place(relx=0.409, rely=0.275)
        self.lb_farelodetrigo_gerar = ttk.Label(self.main_frame, text="Farelo de Trigo", font=('Arial', 7), bootstyle="inverse-light")
        self.lb_farelodetrigo_gerar.place(relx=0.409, rely=0.375)

        self.lb_oleo_gerar = ttk.Label(self.main_frame, text="Farelo de soja", font=('Arial', 7),
                                               bootstyle="inverse-light")
        self.lb_oleo_gerar.place(relx=0.659, rely=0.165)
        self.lb_nucleo_gerar = ttk.Label(self.main_frame, text="Farelo de Carne", font=('Arial', 7),
                                                bootstyle="inverse-light")
        self.lb_nucleo_gerar.place(relx=0.659, rely=0.275)
        self.lb_metionina_gerar = ttk.Label(self.main_frame, text="Farelo de Trigo", font=('Arial', 7),
                                                bootstyle="inverse-light")
        self.lb_metionina_gerar.place(relx=0.659, rely=0.375)


        self.entry_nome_gerar = Entry(self.main_frame)
        self.entry_nome_gerar.place(relx=0.16, rely=0.2, height=25, width=150)


        self.entry_codigo_gerar = Entry(self.main_frame)
        self.entry_codigo_gerar.place(relx=0.16, rely=0.31, height=25, width=150)

        self.entry_milho_gerar = Entry(self.main_frame)
        self.entry_milho_gerar.place(relx=0.16, rely=0.41, height=25, width=150)

        self.entry_farelodesoja_gerar = Entry(self.main_frame)
        self.entry_farelodesoja_gerar.place(relx=0.41, rely=0.2, height=25, width=150)

        self.entry_farelodecarne_gerar = Entry(self.main_frame)
        self.entry_farelodecarne_gerar.place(relx=0.41, rely=0.31, height=25, width=150)

        self.entry_farelodetrigo_gerar = Entry(self.main_frame)
        self.entry_farelodetrigo_gerar.place(relx=0.41, rely=0.41, height=25, width=150)

        self.entry_oleo_gerar = Entry(self.main_frame)
        self.entry_oleo_gerar.place(relx=0.66, rely=0.2, height=25, width=150)

        self.entry_nucleo_gerar = Entry(self.main_frame)
        self.entry_nucleo_gerar.place(relx=0.66, rely=0.31, height=25, width=150)

        self.entry_metionina_gerar = Entry(self.main_frame)
        self.entry_metionina_gerar.place(relx=0.66, rely=0.41, height=25, width=150)

        self.entry_nome_gerar.delete('0', 'end')
        self.entry_nome_gerar.insert(END, self.resultado[1])
        self.entry_codigo_gerar.delete('0', 'end')
        self.entry_codigo_gerar.insert(END, self.resultado[2])
        self.entry_milho_gerar.delete('0', 'end')
        self.entry_milho_gerar.insert(END, self.resultado[3])
        self.entry_farelodesoja_gerar.delete('0', 'end')
        self.entry_farelodesoja_gerar.insert(END, self.resultado[4])
        self.entry_farelodecarne_gerar.delete('0', 'end')
        self.entry_farelodecarne_gerar.insert(END, self.resultado[5])
        self.entry_farelodetrigo_gerar.delete('0', 'end')
        self.entry_farelodetrigo_gerar.insert(END, self.resultado[6])
        self.entry_oleo_gerar.delete('0', 'end')
        self.entry_oleo_gerar.insert(END, self.resultado[7])
        self.entry_nucleo_gerar.delete('0', 'end')
        self.entry_nucleo_gerar.insert(END, self.resultado[8])
        self.entry_metionina_gerar.delete('0', 'end')
        self.entry_metionina_gerar.insert(END, self.resultado[9])

        #self.entry_gerar.insert(END,self.resultado[1])
        self.entry_nome_gerar.configure(state="readonly")
        self.entry_codigo_gerar.configure(state="readonly")
        self.entry_milho_gerar.configure(state="readonly")
        self.entry_farelodesoja_gerar.configure(state="readonly")
        self.entry_farelodecarne_gerar.configure(state="readonly")
        self.entry_farelodetrigo_gerar.configure(state="readonly")
        self.entry_oleo_gerar.configure(state="readonly")
        self.entry_nucleo_gerar.configure(state="readonly")
        self.entry_metionina_gerar.configure(state="readonly")

        self.btn_enviar_gerar = ttk.Button(self.main_frame, text="ok", image=self.img_enviar_gerar, bootstyle="light",
                                           command=self.informar_batelada)
        self.btn_enviar_gerar.place(x=690, y=250)

    def gerar_ordem(self):
        self.img_upload_gerar = PhotoImage(file=r"assets/configuracao.png")
        self.img_enviar_gerar = PhotoImage(file=r"assets/enviar.png")
        self.img_limpar_gerar = PhotoImage(file=r"assets/excluir.png")

        self.btn_limpar_gerar = ttk.Button(self.main_frame, text="ok", image=self.img_limpar_gerar, bootstyle="light", command=self.pegar_lista_gerar)
        self.btn_limpar_gerar.place(x=490, y=250)

        self.btn_upload_gerar = ttk.Button(self.main_frame, text="ok",image= self.img_upload_gerar, bootstyle="light", command=self.pegar_lista_gerar)
        self.btn_upload_gerar.place(x=590, y=250)

        self.banco =  mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database='racao'
        )
        self.cursor = self.banco.cursor()
        self.query = (""" SELECT * FROM produto ORDER BY id ASC
                                                               """)

        self.res = self.cursor.execute(self.query)
        self.r = self.cursor.fetchall()
        colors = self.app.style.colors

        coldata = [
            "Id",
            "Nome",
            "Código",
            "Milho",
            "Farelo de Soja",
            "Farelo de Carne",
            "Farelo de Trigo",
            "Óleo",
            "Núcleo",
            "Metionina",

        ]

        self.rowdata = self.r

        self.dt = Tableview(
            master=self.main_frame2,
            coldata=coldata,
            rowdata=self.rowdata,
            paginated=True,
            searchable=True,

            bootstyle=LIGHT,
            stripecolor=(colors.light, None),
        )
        self.dt.autofit_columns()
        self.dt.pack(fill=BOTH, expand=YES, padx=5, pady=5)


    def __init__(self):

        self.app = ttk.Window(themename="flatly")
        self.app.geometry("1200x900")
        self.app.title("Controle de Produção")

        self.dados()

        self.main_frame_menu = ttk.Frame(self.app, bootstyle="light")
        self.main_frame_menu.pack(fill=X, pady=1, side=TOP)
        self.main_frame_menu.place(x= 1,  height=130, width=1198)
        self.main_frame = ttk.Frame(self.app, bootstyle="light", borderwidth=1, relief="raised")
        self.main_frame.place(height=350, width=800, relx=0.17, rely=0.2)
        self.main_frame2 = ttk.Frame(self.app, bootstyle="light" ,borderwidth=1, relief="raised")
        self.main_frame2.place(height=300, width=800, relx=0.17, rely=0.65)

        #self.formulario()
        self.lista_racao()

        image_files = {
            'menu_add': 'pasta.png',
            'home': 'casa.png',
            'editar': 'editar.png',
            'grafico': 'estatistica.png',
            'excluir': 'excluir.png',
            'procurar': 'procurar.png',
            'add': 'sinal-de-mais.png',
            'carrinho': 'carrinho.png',
            'ordem': 'documento.png',
            'online': 'mundo.png',

        }
        self.photoimages = []
        imgpath = Path(__file__).parent / 'assets'
        for key, val in image_files.items():
            _path = imgpath / val
            self.photoimages.append(ttk.PhotoImage(name=key, file=_path))

        self.menu_cadastrar = ttk.Button(
            master=self.main_frame_menu, text='Cadastrar',
            image='home',
            compound=LEFT,
            bootstyle="light",
            command= lambda : [self.delete_pages_principal(), self.formulario(), self.lista_racao()]

            #command=self.pagina_lista,

        )
        self.menu_cadastrar.pack(side=LEFT, ipadx=3, ipady=5, padx=(215, 0), pady=1)

        self.menu_ordem = ttk.Button(
            master=self.main_frame_menu, text='Gerar Ordem',
            image='ordem',
            compound=LEFT,
            bootstyle="light",
            command = lambda :[self.delete_pages_principal(), self.gerar_ordem()]

            # command=self.pagina_lista,

        )
        self.menu_ordem.pack(side=LEFT, ipadx=2, ipady=5, padx=(50, 0), pady=1)


        self.menu_grafico = ttk.Button(
            master=self.main_frame_menu, text='Relatórios',
            image='grafico',
            compound=LEFT,
            bootstyle="light",
            command = lambda :[self.delete_pages_principal(), self.relatorio(), self.busca_relatorio()]
            # command=self.pagina_lista,

        )
        self.menu_grafico.pack(side=LEFT, ipadx=2, ipady=5, padx=(50, 0), pady=1)

        self.menu_temporeal = ttk.Button(
            master=self.main_frame_menu, text='Tempo Real',
            image='online',
            compound=LEFT,
            bootstyle="light"

            # command=self.pagina_lista,

        )
        self.menu_temporeal.pack(side=LEFT, ipadx=2, ipady=5, padx=(50, 0), pady=1)
        self.center(self.app)  

        self.app.mainloop()

application()
