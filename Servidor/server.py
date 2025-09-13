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

# função principal para rodar o servidor
def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandle)
    print("Server Running in http://localhost:8000")
    httpd.serve_forever()

main()