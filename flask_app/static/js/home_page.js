console.log('scriped linked')
const URL = "https://pokeapi.co/api/v2/pokemon/"


async function asyncCall() {
    const arr = document.querySelectorAll('.pokeArr')
    console.log(arr)
    for (poke of arr) {
        console.log(poke.id)
        const img = document.querySelector(`.img${poke.id}`)
        const name = document.querySelector(`.name${poke.id}`)
        const types = document.querySelector(`.types${poke.id}`)
        fetch(URL + poke.id)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            img.innerHTML = 
            `<img class="card-img-top" src="${data.sprites.front_default}">`
            name.innerHTML = `
            ${data.name}
            `
            for (let type of data.types) {
                types.innerHTML += `${type.type.name}<br>`
            }
            })
            .catch(err => console.log(err))
        }
}
asyncCall()