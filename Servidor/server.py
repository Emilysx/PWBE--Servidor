# from http.server import SimpleHTTPRequestHandler, HTTPServer #

# #definindo a porta 
# port = 8000 
# # definindo o gerenciador/manipulador de requisições
# handler = SimpleHTTPRequestHandler

# # Criando a instancia do servidor
# server = HTTPServer(("localhost", port), handler)

# #imprimindo mensagem de ok 
# print(f"Server Runing in http://localhost:{port}")

# server.serve_forever()

import os # abrir arquivos (manipular arquivos)
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json

# criando uma classe personalizada para tratar requisições
class MyHandle(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            # para abrir o arquivo index.html da pasta
            f = open(os.path.join(path, 'index.html'), encoding='utf-8')   

            # cabeçalho da resposta
            self.send_response(200)
            self.send_header("Content - type", "text/html")
            self.end_headers()

            # envia o conteúdo do index.html para o navegador
            self.wfile.write(f.read().encode('utf-8'))
            f.close()

            return None
        except FileNotFoundError:
            pass
        return super().list_directory(path)
    
    def accont_user(self, login, password):
        loga = "Emily"
        senha = 12345

        if login == loga and senha == password:
            return "Usuario logado"
        else:
            return "Usuario não existe"
    
    # método que lista diretórios
    def do_GET(self):
        if self.path == "/login":
            try:
                with open(os.path.join(os.getcwd(), 'login.html'), encoding='utf-8') as login:
                    content = login.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            except FileNotFoundError:
                self.send_error(404, "File Not Found")
        
        # rota /cadastro
        elif self.path == "/cadastro":
            try:
                with open(os.path.join(os.getcwd(), 'cadastro.html'), encoding='utf-8') as cadastro:
                    content = cadastro.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        # rota /Listar Filmes
        elif self.path == "/listarfilmes":
            try:
                with open(os.path.join(os.getcwd(), 'listar_filmes.html'), encoding='utf-8') as listar_filmes:
                    content = listar_filmes.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        else:
            super().do_GET()

    #Função do Post
    def do_POST(self):
        if self.path == '/login':
            # Lê o tamanho do conteúdo enviado pelo formulário
            content_length = int(self.headers['Content-length'])
            # Lê o corpo da requisição (os dados enviados pelo formulário)
            body = self.rfile.read(content_length).decode('utf-8')
            # Converte os dados do corpo para um dicionário (chave=campo, valor=dado enviado)
            form_data = parse_qs(body)

            login = form_data.get('usuario', [""])[0]
            password = int(form_data.get('senha', [""])[0])
            logou = self.accont_user(login, password)

            print("Data Form: ")
            print("Usuário: ", form_data.get('usuario', [""])[0])
            print("Senha: ", form_data.get('senha', [""])[0])

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(logou.encode('utf-8'))
        
        elif self.path == '/cadastro':
            # Lê o tamanho do conteúdo enviado pelo formulário
            content_length = int(self.headers['Content-length'])
            # Lê o corpo da requisição (os dados enviados pelo formulário)
            body = self.rfile.read(content_length).decode('utf-8')
            # Converte os dados do corpo para um dicionário (chave=campo, valor=dado enviado)
            form_data = parse_qs(body)

            # Pega os dados do formulário de cadastro
            filme = form_data.get('filme', [""])[0]
            atores = form_data.get('atores', [""])[0]
            diretor = form_data.get('diretor', [""])[0]
            ano = form_data.get('ano', [""])[0]
            genero = form_data.get('genero', [""])[0]
            produtora = form_data.get('produtora', [""])[0]
            sinopse = form_data.get('sinopse', [""])[0]

            # Cria o "objeto filme" em formato de dicionário Python
            novo_filme = {
                "filme": filme,
                "atores": atores,
                "diretor": diretor,
                "ano": ano,
                "genero": genero,
                "produtora": produtora,
                "sinopse": sinopse
            }

            # Salvar os filmes em um arquivo JSON
            try:
                # Abre o arquivo (se existir) e carrega os filmes já cadastrados
                with open("filmes.json", "r", encoding="utf-8") as f:
                    filmes = json.load(f)
            except FileNotFoundError:
                # Se o arquivo não existir, cria uma lista vazia
                filmes = []

            # Adiciona o novo filme na lista
            filmes.append(novo_filme)

            # Salva de volta no JSON (atualiza o arquivo)
            with open("filmes.json", "w", encoding="utf-8") as f:
                json.dump(filmes, f, ensure_ascii=False, indent=4)

            # Mostra no console (só para debug mesmo)
            print("Novo cadastro de filme:")
            print(json.dumps(novo_filme, indent=4, ensure_ascii=False))


            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("Filme cadastrado com sucesso!".encode('utf-8'))

        else:
            super(MyHandle, self).do_POST()

# função principal para rodar o servidor
def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandle)
    print("Server Running in http://localhost:8000")
    httpd.serve_forever()

main()