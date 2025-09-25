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
from urllib.parse import urlparse  #  para processar a URL sem query string
import re # para conseguir o article

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
        # remove a query string da URL para comparação
        path = urlparse(self.path).path

        # rota principal "/" redireciona para index.html
        if self.path in ["/", "/index", "/index.html"]:
            try:
                with open(os.path.join(os.getcwd(), 'index.html'), encoding='utf-8') as index:
                    content = index.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            except FileNotFoundError:
                self.send_error(404, "File Not Found")

        elif self.path == "/login":
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
        elif path in ["/cadastro", "/cadastro/"]:
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
        elif path in ["/listarfilmes", "/listarfilmes/", "/listar_filmes.html"]:
            try:
                with open("filmes.json", "r", encoding="utf-8") as f:
                    filmes = json.load(f)

                # monta lista em HTML
                lista_html = "<h2>Filmes Cadastrados</h2><ul>"
                for filme in filmes:
                    lista_html += f"""
                    <li>
                        <strong>{filme['nomeFilme']}</strong>
                        Ano: {filme['ano']} <br>
                        Diretor: {filme['diretor']} <br>
                        Atores: {filme['atores']} <br>
                        Gênero: {filme['genero']} <br>
                        Produtora: {filme['produtora']} <br>
                        Sinopse: {filme['sinopse']}
                    </li><br>
                    """
                lista_html += "</ul>"

                # abre o HTML base
                with open("listar_filmes.html", "r", encoding="utf-8") as f:
                    content = f.read()

               # insere a lista no lugar do article (independente dos espaços)
                content = re.sub(
                    r'<article id="listaFilmes".*?</article>',
                    f'<article id="listaFilmes">{lista_html}</article>',
                    content,
                    flags=re.DOTALL
                )

                # envia resposta final
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))


            except FileNotFoundError:
                self.send_error(404, "Arquivo de filmes não encontrado")

        else:
            super().do_GET()

    #Função do Post
    def do_POST(self):
        path = urlparse(self.path).path

        if path == '/login':
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
        
        elif path in ["/cadastro", "/cadastro/"]:

            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            # Pega os dados do formulário
            filme = form_data.get('nomeFilme', [""])[0]
            atores = form_data.get('atores', [""])[0]
            diretor = form_data.get('diretor', [""])[0]
            ano = form_data.get('ano', [""])[0]
            genero = form_data.get('genero', [""])[0]
            produtora = form_data.get('produtora', [""])[0]
            sinopse = form_data.get('sinopse', [""])[0]

            # Cria o objeto filme
            novo_filme = {
                "nomeFilme": filme,
                "atores": atores,
                "diretor": diretor,
                "ano": ano,
                "genero": genero,
                "produtora": produtora,
                "sinopse": sinopse
            }

            # Salva no JSON
            try:
                with open("filmes.json", "r", encoding="utf-8") as f:
                    filmes = json.load(f)
            except FileNotFoundError:
                filmes = []

            filmes.append(novo_filme)

            with open("filmes.json", "w", encoding="utf-8") as f:
                json.dump(filmes, f, ensure_ascii=False, indent=4)

            print("Novo cadastro de filme:")
            print(json.dumps(novo_filme, indent=4, ensure_ascii=False))

            # --- REDIRECIONAMENTO PARA LISTAGEM ---
            self.send_response(303)  # código 303 = redirecionamento após POST
            self.send_header("Location", "/listarfilmes")
            self.end_headers()

        else:
            super(MyHandle, self).do_POST()

# função principal para rodar o servidor
def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandle)
    print("Server Running in http://localhost:8000")
    httpd.serve_forever()

main()