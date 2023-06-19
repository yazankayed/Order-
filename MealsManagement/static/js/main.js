console.log("llsss");

const url = window.location.href
const search = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultSerach = document.getElementById('result-serach')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const sendInputSearch = (restaurant) => {
    $.ajax({
        type: "POST",
        url: 'search/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'restaurant': restaurant,
        },
        success: (response) => {
            console.log(response.daa);
            data = response.data;
            if (searchInput.value.length < 1) {
                resultSerach.classList.add('hidden-visible')
            }
            if (Array.isArray(data)) {
                resultSerach.innerHTML = ""
                data.forEach(resturent => {
                    resultSerach.innerHTML += `
                    <a
                     class= "item" 
                     href="rest/${resturent.PRIMARY_KEY}">
                     <div class="cardItemSearch">
                     <div>
                       <img 
                       class="imageCategory"
                       src="${resturent.image_logo}" alt="">
                     </div>
                     <div class="namewithPhone">
                       <span> Name:${resturent.name}</span></br>
                       <span>Mobile: ${resturent.phone}</span>
                     </div>
                   </div>
                    <a> `
                });
            }
            else {
                if (searchInput.value.length > 0) {
                    resultSerach.innerHTML = `<b>${data}<b>`
                }
                // else{
                //     resultSerach.classList.add('hidden-visible')
                // }
            }
        },
        error: (error) => {
            console.log(error);
        }
    })
}

searchInput.addEventListener('keyup', e => {
    console.log(e.target.value);
    if (resultSerach.classList.contains('hidden-visible')) {
        resultSerach.classList.remove('hidden-visible')
    }

    sendInputSearch(e.target.value);
})
console.log(csrf);