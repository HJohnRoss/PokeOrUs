console.log('scriped linked')
const URL = "https://pokeapi.co/api/v2/pokemon/"


// search poke
function getPoke(event) {
    event.preventDefault()
    console.log('submitted')
    const pokeResultDiv = document.querySelector("#pokeResult")
    const pokeName = document.querySelector("#pokeName").value
    console.log(pokeName)
    pokeResultDiv.innerHTML = `<p class="text-danger">type a valid pokemon</p>`
    fetch(URL + pokeName)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            pokeResultDiv.innerHTML = `
            <img src="${data.sprites.front_default}" style="width:500px"> <br>
            <a href="/poke/show/${data.id}">${data.name}</a>
            `
        })
        .catch(err => console.log(err))
}