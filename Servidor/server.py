# só pra mudar a data no commit 
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
import mysql.connector  # pip install mysql-connector-python

# Conectar ao banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senai",
    database="webserver_filmes"  # Adicionando o nome do banco de dados
)

# Função auxiliar para carregar filmes do banco de dados
def carregar_filmes():
    # Garante que a conexão esteja ativa
    if not mydb.is_connected():
        mydb.reconnect()

    try:
        cursor = mydb.cursor(dictionary=True)  # Retorna resultados como dicionários
        cursor.execute("SELECT * FROM Filme")
        result = cursor.fetchall()
        cursor.close()
        print('Banco conectado e filmes carregados com sucesso!')
        return result
    except Exception as e:
        print(f'Erro ao carregar filmes: {e}')
        return []
    

    def insertFilmes(self, nome, produtora, orcamento, duracao, ano, poster):
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO webserver_filmes(titulo, tempo_duracao, ano, poster, id_linguagem)")
        cursor.execute("SELECT id_filme FROM webserver_filmes WHERE titulo... ")
        resultado = cursor.fetchall()
        print(resultado)
        cursor.execute("SELECT * FROM webserver_filmes WHERE id_filme = %s...")
        resultado = cursor.fetchall()
        print(resultado)

        cursor.close()
        mydb.commit()
        return resultado

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
            filmes = carregar_filmes()  # Puxa filmes do banco de dados mysql
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
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            titulo = form_data.get('nomeFilme', [""])[0]
            ano = form_data.get('ano', [""])[0]

            try:
                cursor = mydb.cursor()
                sql = "INSERT INTO Filme (titulo, ano) VALUES (%s, %s)"
                cursor.execute(sql, (titulo, ano))
                mydb.commit()
                cursor.close()

                self.send_response(303)
                self.send_header("Location", "/listar_filmes.html")
                self.end_headers()

            except Exception as e:
                self.send_error(500, f"Erro ao cadastrar filme: {str(e)}")

        elif path == "/api/filmes":
            try:
                cursor = mydb.cursor(dictionary=True)
                cursor.execute("""
                    SELECT 
                        f.id_filme,
                        f.titulo AS nomeFilme,
                        -- converte TIME em string 'HH:MM:SS' para evitar erro do timedelta
                        IFNULL(TIME_FORMAT(f.tempo_duracao, '%H:%i:%s'), '') AS tempo_duracao,
                        f.ano,
                        IFNULL(f.poster, '') AS poster,
                        IFNULL(l.linguagem, '') AS linguagem
                    FROM Filme f
                    LEFT JOIN Linguagem l ON f.id_linguagem = l.id_linguagem
                    ORDER BY f.titulo;
                """)
                filmes = cursor.fetchall()
                cursor.close()

                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(filmes, ensure_ascii=False).encode("utf-8"))

            except Exception as e:
                print("Erro ao buscar filmes:", e)
                self.send_error(500, f"Erro ao buscar filmes: {str(e)}")

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

         #Função do Post - Cadastro
        elif path in ["/cadastro", "/cadastro/"]:

            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            # Captura os dados do formulário
            titulo = form_data.get('titulo', [''])[0].strip()
            tempo_duracao = form_data.get('tempo_duracao', [''])[0].strip()
            ano = form_data.get('ano', [''])[0].strip()
            poster = form_data.get('poster', [''])[0].strip()
            id_linguagem = form_data.get('id_linguagem', [''])[0].strip()

            # Validações básicas
            if not titulo or not ano or not id_linguagem:
                resposta = "Erro: campos obrigatórios não preenchidos!"

            elif not ano.isdigit() or int(ano) < 1900 or int(ano) > 2025:
                resposta = "Erro: ano inválido!"

            elif tempo_duracao and not re.match(r'^\d{2}:\d{2}(:\d{2})?$', tempo_duracao):
                resposta = "Erro: duração deve estar no formato HH:MM ou HH:MM:SS!"

            else:
                try:
                    if not mydb.is_connected():
                        mydb.reconnect()
                    cursor = mydb.cursor(dictionary=True)

                    # Verifica duplicidade de título (case-insensitive)
                    cursor.execute("SELECT COUNT(*) AS total FROM Filme WHERE LOWER(titulo) = LOWER(%s)", (titulo,))
                    duplicado = cursor.fetchone()['total']

                    if duplicado > 0:
                        resposta = "Erro: já existe um filme com esse título!"
                    else:
                        sql = """
                            INSERT INTO Filme (titulo, tempo_duracao, ano, poster, id_linguagem)
                            VALUES (%s, %s, %s, %s, %s)
                        """
                        cursor.execute(sql, (titulo, tempo_duracao, ano, poster, id_linguagem))
                        mydb.commit()
                        resposta = "Filme cadastrado com sucesso!"
                    cursor.close()

                except Exception as e:
                    resposta = f"Erro ao cadastrar filme: {str(e)}"

            # Retorna resposta ao navegador
            self.wfile.write(resposta.encode('utf-8'))    
    
        elif self.path == '/edit':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            id_filme = int(form_data.get('index', [0])[0])
            titulo = form_data.get('filme', [""])[0]
            ano = form_data.get('ano', [""])[0]

            try:
                cursor = mydb.cursor()
                sql = "UPDATE Filme SET titulo = %s, ano = %s WHERE id_filme = %s"
                cursor.execute(sql, (titulo, ano, id_filme))
                mydb.commit()
                cursor.close()

                resposta = "Filme editado com sucesso!"
            except Exception as e:
                resposta = f"Erro ao editar: {str(e)}"

                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(resposta.encode('utf-8'))

        elif self.path == '/delete':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            id_filme = int(form_data.get('index', [0])[0])

            try:
                cursor = mydb.cursor()
                sql = "DELETE FROM Filme WHERE id_filme = %s"
                cursor.execute(sql, (id_filme,))
                mydb.commit()
                cursor.close()

                resposta = "Filme deletado com sucesso!"

            except Exception as e:
                resposta = f"Erro ao deletar: {str(e)}"

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(resposta.encode('utf-8'))

        else:
            super(MyHandle, self).do_POST()

# função principal para rodar o servidor
def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandle)
    print(" 🎀 Server Running in http://localhost:8000")
    httpd.serve_forever()

main()