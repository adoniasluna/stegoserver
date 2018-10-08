#Thiago Lourenço C. Bezerra.
#Interface Gráfica usando Tkinter.
#Python 3.6.

from functools import partial
import tkinter
import Client
import ImageOperations

class GuiRedes:

    #Construtor que recebe a janela.
    def __init__(self, window):

        def getMessage(buttonHide):
            print(self.entryMessage.get())

            msg = bytes(self.entryMessage.get(), 'utf8')
            img = self.entryImagem.get()
            image = bytes(ImageOperations.extracting_blue(img))

            blue = Client.insert_image(image, msg)
            ImageOperations.write_image(img, blue)

        def extractMessage(buttonExtract):
            self.photo["file"] = self.entryImagem.get()

            img = self.entryImagem.get()
            image = bytes(ImageOperations.extracting_blue(img))

            msg = Client.extract_msg(image)
            decoded_msg = "".join(chr(x) for x in msg)

            self.labelMessageExtract["text"] = "Extracted message: \n" + decoded_msg

        self.frame = tkinter.Frame(window)
        self.frame.pack()

        self.photo = tkinter.PhotoImage(file = "icon.png")
        self.labelPhoto = tkinter.Label(self.frame, image=self.photo)
        self.labelPhoto.grid(row=0, column=0)

        # Label q vai receber a mensagem EXTRAIDA.
        self.labelMessageExtract = tkinter.Label(self.frame, fg="black")
        self.labelMessageExtract.grid(row=2, column=0)

        #Label q vai receber a mensagem.
        self.labelMessage = tkinter.Label(self.frame, text = "Message:", fg = "black")
        self.labelMessage.grid(row = 1, column = 1)

        #Obtem a mensagem pra começa a esteganografia.
        self.entryMessage = tkinter.Entry(self.frame)
        self.entryMessage.grid(row = 1, column = 2)

        #Label q vai receber a imagem.
        self.labelImagem = tkinter.Label(self.frame, text ="Image:", fg = "black")
        self.labelImagem.grid(row = 2, column = 1)

        #Obtem endereço da imagem.
        self.entryImagem = tkinter.Entry(self.frame)
        self.entryImagem.grid(row = 2, column = 2)

        #Botão q começa a esteganografia.
        self.buttonHide = tkinter.Button(self.frame, text = "Hide", width = 15)
        self.buttonHide["bg"] = "black"
        self.buttonHide["fg"] = "white"
        self.buttonHide["command"] = partial(getMessage, self.buttonHide)
        self.buttonHide.grid(row = 3, column = 1)

        # Botão q começa a estração do q está na imagem.
        self.buttonExtract = tkinter.Button(self.frame, text = "Extract", width=15)
        self.buttonExtract["bg"] = "black"
        self.buttonExtract["fg"] = "white"
        self.buttonExtract["command"] = partial(extractMessage, self.buttonExtract)
        self.buttonExtract.grid(row = 3, column = 2)

        #Botão q fecha o programa.
        self.quitButton = tkinter.Button(self.frame, text = "Quit", width = 15, command = self.frame.quit)
        self.quitButton["bg"] = "black"
        self.quitButton["fg"] = "white"
        self.quitButton.grid(row = 4, column = 1, columnspan = 2)


window = tkinter.Tk()
window.title("Esteganografia")
guiRedes = GuiRedes(window)

window.mainloop()
