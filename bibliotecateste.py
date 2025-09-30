import json
import os

class Livro:
    def __init__(self, id, titulo, autor, ano):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def to_dict(self):
        return {"id": self.id, "titulo": self.titulo, "autor": self.autor, "ano": self.ano}


class Biblioteca:
    def __init__(self, arquivo="livros.json"):
        self.arquivo = arquivo
        self.livros = self.carregar()

    def carregar(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r") as f:
                return [Livro(**livro) for livro in json.load(f)]
        return []

    def salvar(self):
        with open(self.arquivo, "w") as f:
            json.dump([livro.to_dict() for livro in self.livros], f, indent=4)

    def cadastrar(self, titulo, autor, ano):
        novo_id = len(self.livros) + 1
        livro = Livro(novo_id, titulo, autor, ano)
        self.livros.append(livro)
        self.salvar()
        print(f"Livro '{titulo}' cadastrado com sucesso! (ID {novo_id})")

    def listar(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        for livro in self.livros:
            print(f"[{livro.id}] {livro.titulo} - {livro.autor} ({livro.ano})")

    def atualizar(self, id, titulo=None, autor=None, ano=None):
        for livro in self.livros:
            if livro.id == id:
                if titulo: livro.titulo = titulo
                if autor: livro.autor = autor
                if ano: livro.ano = ano
                self.salvar()
                print(f"Livro ID {id} atualizado com sucesso!")
                return True
        print(f"Livro ID {id} não encontrado.")
        return False

    def excluir(self, id):
        for livro in self.livros:
            if livro.id == id:
                self.livros.remove(livro)
                self.salvar()
                print(f"✅ Livro ID {id} excluído com sucesso!")
                return True
        print(f" Livro ID {id} não encontrado.")
        return False

class App:
    def __init__(self):
        self.biblioteca = Biblioteca()

    def menu(self):
        while True:
            print("\n--- Bem vindo(a) a biblioteca ---")
            print("\n--- Por favor, escolha uma opção ---")
            print("1. Cadastrar livro")
            print("2. Listar livros")
            print("3. Atualizar livro")
            print("4. Excluir livro")
            print("5. Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                titulo = input("Insira o título da obra: ")
                autor = input("Insira o autor da obra: ")
                ano = input("Insira o ano de publicação: ")
                self.biblioteca.cadastrar(titulo, autor, ano)
            elif opcao == "2":
                self.biblioteca.listar()
            elif opcao == "3":
                id = int(input("ID do livro a atualizar: "))
                titulo = input("Novo título (ou Enter): ")
                autor = input("Novo autor (ou Enter): ")
                ano = input("Novo ano (ou Enter): ")
                self.biblioteca.atualizar(id, titulo or None, autor or None, ano or None)
            elif opcao == "4":
                id = int(input("Insira o ID do livro a excluir: "))
                self.biblioteca.excluir(id)
            elif opcao == "5":
                print("Desligando o sistema")
                break
            else:
                print("Opção inválida!")


if __name__ == "__main__":
    app = App()
    app.menu()
