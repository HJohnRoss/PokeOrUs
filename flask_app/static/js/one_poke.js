console.log('scriped linked')
const URL = "https://pokeapi.co/api/v2/pokemon/"


// one poke
async function asyncCall() {
    console.log('called')
    const name = document.querySelector('#poke_name')
    const title = document.querySelector('#name2')
    const onePoke = document.querySelector('#one_poke')
    const poke_data = document.querySelector('#poke_data')
    const addFav = document.querySelector('#addFav')
    const deleteFav = document.querySelector('#deleteFav')
    fetch(URL + name.innerHTML)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            name.innerHTML = `
            <h1>${data.name}</h1>
            `
            title.innerHTML = `
            ${data.name}
            `
            onePoke.innerHTML += `
            <img src="${data.sprites.front_default}" style="width:400px">
            `
            poke_data.innerHTML = `<h5>Types:</h5>`
            for (let type of data.types) {
                poke_data.innerHTML += `<p>${type.type.name}</p>`
            }
            poke_data.innerHTML += `<h5>Stats:</h5>`
            for (let stat of data.stats) {
                poke_data.innerHTML += `<p>${stat.stat.name}: ${stat.base_stat}</p>`
            }
            if(addFav){
                addFav.innerHTML += `
                <a class="btn btn-primary" href="/api/fav/${data.id}">Favorite</a>
                `
            }
            else{
                deleteFav.innerHTML += `
                <a class="btn btn-danger" href="/api/fav/delete/${data.id}">Unfavorite</a>
                `
            }
        })
        .catch(err => console.log(err))
}
asyncCall();