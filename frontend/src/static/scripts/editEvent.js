const form = document.getElementById('form-edit-event')
const id  = document.getElementById('event-id').textContent


const editEvent = async (data) => {
    const endpoint = 'edit_event/' 
    await fetch('http://localhost:8000/'+endpoint+id, {
        method: "PUT",
        body: JSON.stringify(data),
        mode:"cors",
        headers:{
            "Content-type": "application/json",
        }, 
     })
}


form.addEventListener('submit', async (event)=>{
    event.preventDefault();
    

    const title = form['title'].value
    const description = form['description'].value
    const date = form['date'].value
    const hour = form['hour'].value
    

    const data = {
        "title": title,
        "description":description, 
        "date": date, 
        "hour": hour, 
    }

    console.log(data)
    editEvent(data)
    .then(window.history.back())

    
})