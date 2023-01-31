
const form = document.getElementById('form-register')

const register = async (data) =>{
    const endpoint = 'register'
    await fetch('http://localhost:8000/'+endpoint, {
        method: "POST",
        body: JSON.stringify(data),
        mode:"cors",
        headers:{
            "Content-type": "application/json",
        }, 
     })
}

form.addEventListener('submit', async (event)=>{
    event.preventDefault();
    

    const name = form['name'].value
    const email = form['email'].value
    const password = form['password'].value
    

    const data = {
        "name": name,
        "email":email, 
        "password": password, 
    }
    register(data).then(window.history.back())

    
})