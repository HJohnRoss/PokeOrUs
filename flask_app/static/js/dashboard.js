console.log('scriped linked')
const URL = "https://pokeapi.co/api/v2/pokemon/"


async function asyncCall() {
    const allLikes = document.querySelectorAll('.all_likes')
    console.log(allLikes)
    for (like of allLikes) {
        console.log(like)
        const img = document.querySelector(`.img${like.id}${like.innerHTML}`)
        const name = document.querySelector(`.name${like.id}${like.innerHTML}`)
        const name2 = document.querySelector(`.name2${like.id}${like.innerHTML}`)
        const types = document.querySelector(`.types${like.id}${like.innerHTML}`)
        console.log(like.id)
        fetch(URL + like.id)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            img.innerHTML = `
            <img src="${data.sprites.front_default}" style="height: 150px;">
            `
            if(name){
                name.innerHTML = `
                <a href="/poke/show/${data.id}">${data.name}</a>
                `
            }
            else {
                name2.innerHTML = `
                <p>${data.name}</p>
                `
            }
            for (let type of data.types) {
                types.innerHTML += `<p>${type.type.name}</p>`
            }
            const element = document.getElementById(`${data.id}`)
            element.remove()
            })
            .catch(err => console.log(err))
        }
}
asyncCall()