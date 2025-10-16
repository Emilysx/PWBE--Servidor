async function carregarFilmes() {
  try {
    const resp = await fetch("/api/filmes");  // Chama a API para pegar os filmes
    const filmes = await resp.json();

    const lista = document.getElementById("filmesLista");
    lista.innerHTML = "";  // Limpa a lista antes de popular

    if (filmes.length === 0) {
      lista.innerHTML = `
        <article class="mensagemVazia">
          <p>Não há filmes cadastrados no momento.</p>
          <p>Comece adicionando seu primeiro filme ao sistema!</p>
        </article>
      `;
      return;
    }

    filmes.forEach((filme, index) => {
      const li = document.createElement("li");

      // Preenche cada item da lista com as informações do filme
      li.innerHTML = `
        <strong>${filme.nomeFilme}</strong><br>
        Ano: ${filme.ano} <br>
        Diretor: ${filme.diretor} <br>
        Atores: ${filme.atores} <br>
        Gênero: ${filme.genero} <br>
        Produtora: ${filme.produtora} <br>
        Sinopse: ${filme.sinopse}<br>

       <div class="acoesCard">
        <!-- Botão de Editar com ícone -->
        <button class="botaoPequeno" onclick="editarFilme(${index})">
          <i class="fas fa-edit"></i> <!-- Ícone de edição -->
        </button>

        <!-- Botão de Excluir com ícone -->
        <button class="botaoPequeno botaoPequenoExcluir" onclick="deletarFilme(${index})">
          <i class="fas fa-trash"></i> <!-- Ícone de lixeira (excluir) -->
        </button>
      </div>
      `;
      lista.appendChild(li);  // Adiciona o item na lista
    });
  } catch (err) {
    console.error("Erro ao carregar filmes:", err);
  }
}

// Função para excluir filme
async function deletarFilme(index) {
  if (!confirm("Tem certeza que deseja excluir este filme?")) return;

  const resposta = await fetch("/delete", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: `index=${index}`  // Envia o índice do filme a ser deletado
  });

  alert(await resposta.text());  // Exibe a resposta do servidor
  carregarFilmes();  // Recarrega a lista de filmes após a exclusão
}

// Função para editar filme
async function editarFilme(index) {
  const resposta = await fetch("/api/filmes");
  const filmes = await resposta.json();
  const filme = filmes[index];

  // Cria prompts para editar os dados do filme (pode ser melhorado com modal ou formulário)
  const novoFilme = prompt("Nome do filme:", filme.nomeFilme) || filme.nomeFilme;
  const novosAtores = prompt("Atores:", filme.atores) || filme.atores;
  const novoDiretor = prompt("Diretor:", filme.diretor) || filme.diretor;
  const novoAno = prompt("Ano:", filme.ano) || filme.ano;
  const novoGenero = prompt("Gênero:", filme.genero) || filme.genero;
  const novaProdutora = prompt("Produtora:", filme.produtora) || filme.produtora;
  const novaSinopse = prompt("Sinopse:", filme.sinopse) || filme.sinopse;

  const params = new URLSearchParams({
    index,
    nomeFilme: novoFilme,
    atores: novosAtores,
    diretor: novoDiretor,
    ano: novoAno,
    genero: novoGenero,
    produtora: novaProdutora,
    sinopse: novaSinopse
  });

  const resp = await fetch("/edit", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: params.toString()  // Envia os dados editados para o servidor
  });

  alert(await resp.text());  // Exibe a resposta do servidor
  carregarFilmes();  // Recarrega a lista de filmes após a edição
}

// Carrega os filmes assim que a página for carregada
carregarFilmes();