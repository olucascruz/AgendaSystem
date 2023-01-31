const date = new Date();
const now = date.toLocaleString();
const form = document.getElementById("form-add-event")

const currentDate = date.toISOString().substring(0,10);
const currentTime = date.toISOString().substring(11,16);

document.getElementById('date').value = currentDate;
document.getElementById('time').value = currentTime;


const addEvent = async (data) => {
    const endpoint = 'add_event' 
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
        

        const title = form['title'].value
        const description = form['description'].value
        const date = form['date'].value
        const hour = form['hour'].value
        const user_id = form['user_id'].value
        

        const data = {
            "title": title,
            "description":description, 
            "date": date, 
            "hour": hour, 
            "user_id": parseInt(user_id)
        }

        
        addEvent(data)
        .then(window.history.back())
    
        
})