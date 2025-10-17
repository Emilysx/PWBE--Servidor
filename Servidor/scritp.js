async function carregarFilmes() {
  try {
    const resp = await fetch("/api/filmes"); // busca dados do servidor
    const filmes = await resp.json();

    const lista = document.getElementById("filmesLista");
    lista.innerHTML = ""; // limpa antes de popular

    if (!filmes || filmes.length === 0) {
      lista.innerHTML = `
        <article class="mensagemVazia">
          <p>🎬 Não há filmes cadastrados no momento.</p>
          <p>Comece adicionando seu primeiro filme!</p>
        </article>
      `;
      return;
    }

    filmes.forEach((filme) => {
      const li = document.createElement("li");

      // Monta o card de cada filme com dados do banco
      li.innerHTML = `
        <div class="cardFilme">
          <img src="${filme.poster || 'https://via.placeholder.com/150x220?text=Sem+Imagem'}"
               alt="Poster do filme" class="posterFilme">

          <div class="infoFilme">
            <h3>${filme.nomeFilme}</h3>
            <p><strong>Ano:</strong> ${filme.ano || "N/A"}</p>
            <p><strong>Duração:</strong> ${filme.tempo_duracao || "N/A"}</p>
            <p><strong>Linguagem:</strong> ${filme.linguagem || "N/A"}</p>
          </div>

          <div class="acoesCard">
            <button class="botaoPequeno" onclick="editarFilme(${filme.id_filme})">
              <i class="fas fa-edit"></i>
            </button>
            <button class="botaoPequeno botaoPequenoExcluir" onclick="deletarFilme(${filme.id_filme})">
              <i class="fas fa-trash"></i>
            </button>
          </div>
        </div>
      `;

      lista.appendChild(li);
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


// --- Controle do envio do formulário e modal de feedback ---

const formCadastro = document.getElementById("formCadastro");

if (formCadastro) {
  formCadastro.addEventListener("submit", async (e) => {
    e.preventDefault(); // Impede o reload da página

    const formData = new FormData(formCadastro);

    const resp = await fetch("/cadastro", {
      method: "POST",
      body: new URLSearchParams(formData)
    });

    const texto = await resp.text();
    mostrarModal(texto); // Exibe a resposta do servidor
  });
}

function mostrarModal(mensagem) {
  const modal = document.createElement("div");
  modal.classList.add("modal");

  modal.innerHTML = `
    <div class="modal-conteudo">
      <h2>${mensagem.includes("Erro") ? "❌ Erro" : "✅ Sucesso"}</h2>
      <p>${mensagem}</p>
      <button id="fecharModal">OK</button>
    </div>
  `;

  document.body.appendChild(modal);

  document.getElementById("fecharModal").addEventListener("click", () => {
    modal.remove();
    if (mensagem.includes("sucesso")) {
      window.location.href = "/listar_filmes.html";
    }
  });
}
