

filme = [
    {
    "id": result [0],
    "titulo": result [1],
    "categoria": result [2],
    "orcamento": float(result [3]),
    "duracao": str(result [4]),
    "ano": result [5],
    "imagem": result [6],
    }
    for result in resultado
]

return filmes 

# transformou em json e pegou a url, caminha de acesso
# src > api > films.jsx

export async function default carregarFilmes(){
    try{
        const resposta = await fetch(LINK DA URL)
        if(!resposta.ok){
           throw new Error("Erro ao carregar filmes");
        }
        const dados = await resposta.json();
        return dados;
    }catch (erro){
        console.log("Erro na API: ", erro)
        return [];
    }
}


# pesquis com id:

export async function default carregarFilmes(){
    try{
        const resposta = await fetch(`LINK DA URL?id=${id}`)
        if(!resposta.ok){
           throw new Error("Erro ao carregar filmes");
        }
        const dados = await resposta.json();
        return dados;
    }catch (erro){
        console.log("Erro na API: ", erro)
        return [];
    }
}


# No arquivo app:
import { carregarFilmes } from './api/filmes.jsx'
import { useState, useEffect} from 'react'

#Dentro da função APP:
const [filmes, setFilmes] = useState([]);
const [loading, setLoading] = useState(True);

useEffect(()=>{
    async function pegaFilmes(){
        try{
            const dados = await carregarFilmes();
            setFilmes(dados);
        } catch (erro){
            consele.log ("Erro ao carregar filmes", erro);
        } finally {
            setLoading(false)
        }
    }
    pegarFilmes()
}, [])


return(
    <>

    {loading? {
        <h1>Carregar Filmes.... </h1>
    }:}

    <div clasName = 'App'>
    <Home>
    </div>
)

# No servidor tem que colocar a linha do cors
self.send_herder()

# Home



