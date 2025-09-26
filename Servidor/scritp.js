  async function carregarFilmes() {
    try {
      const resp = await fetch("/api/filmes"); // chama a API
      const filmes = await resp.json();

      const lista = document.getElementById("filmesLista");
      lista.innerHTML = ""; 

      filmes.forEach(filme => {
        const li = document.createElement("li");
        li.innerHTML = `
          <strong>${filme.nomeFilme}</strong>
          Ano:${filme.ano} <br>
          Diretor: ${filme.diretor} <br>
          Atores: ${filme.atores} <br>
          Gênero: ${filme.genero} <br>
          Produtora: ${filme.produtora} <br>
          Sinopse: ${filme.sinopse}
        `;
        lista.appendChild(li);
      });
    } catch (err) {
      console.error("Erro ao carregar filmes:", err);
    }
  }

  carregarFilmes();