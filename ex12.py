class Livro():
    def __init__(self, autor, titulo):
        self.autor = autor
        self.titulo = titulo
    def info(self):
        print(f"O autor do livro é {self.autor}, e o titulo é {self.titulo}")

livro1 = Livro("Dale Carnegie","Como fazer amigos e influenciar pessoas")
livro2 = Livro("George Orwell","A revolução dos bichos: Um conto de fadas")

livro1.info()
livro2.info()



    

        