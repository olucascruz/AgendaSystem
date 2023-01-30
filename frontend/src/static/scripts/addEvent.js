const date = new Date();
const now = date.toLocaleString();
const form = document.getElementById("form-add-event")
const url_api = document.getElementById("url_api").textContent

const currentDate = date.toISOString().substring(0,10);
const currentTime = date.toISOString().substring(11,16);

document.getElementById('date').value = currentDate;
document.getElementById('time').value = currentTime;

console.log(url_api)

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

        

        await fetch(url_api, {
            method: "POST",
            body: JSON.stringify(data),
            mode:"cors",
            headers:{
                "Content-type": "application/json",
            }, 
         }).then(window.history.back())
    
        
})