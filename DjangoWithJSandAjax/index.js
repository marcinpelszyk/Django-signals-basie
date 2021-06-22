





const url = 'https://swapi.dev/api/people/'



$.ajax({
    type: 'GET',
    url: url,
    success: function(response){
        console.log('ajax', response)
    },
    error: function(error){
        console.log(error)
    },
})
    

const req = new XMLHttpRequest()

req.addEventListener('readystatechange', ()=>{
    if(req.readyState===4){
        console.log('xhttps', JSON.PARSreq.responseText)
    }
})


req.open('GET', url)
req.send()


fetch(url)
.then(resp=>resp.json()).then(data=>console.log('fetch', data))
.catch(err=> console.log(err))


