console.log('hELLO');


const hello = document.getElementById('hello')



$.ajax({
    type: 'GET',
    url: '/hello/',
    success: function(response){
        console.log(response.text)
        hello.textContent = response.text
    },
    error: function(error){
        console.log(error)
    }
})

