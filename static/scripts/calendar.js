const currentDate = document.querySelector(".current-date");
const daysTag = document.querySelector(".days")
const prevNextIcons = document.querySelectorAll(".icon span")


let date = new Date(),
currentYear = date.getFullYear(),
currentMonth = date.getMonth();


const months = [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

const renderCalendar = ()=>{
    let firstDayofMonth = new Date(currentYear, currentMonth, 1).getDay(),
    lastDateofMonth = new Date(currentYear, currentMonth + 1,0 ).getDate(),
    lastDateofLastMonth = new Date(currentYear, currentMonth, 0).getDate();

    let liTag = ""

    for(let i = firstDayofMonth; i>0; i--){
        liTag += `<li>${lastDateofLastMonth - i + 1}</li>`;
    }

    for(let i = 1; i<=lastDateofMonth; i++){
        if(i == date.getDate() && currentMonth == date.getMonth()){
            liTag += `<li class="active">${i}</li>`    
        }else{
            liTag += `<li>${i}</li>`
        }
    }

    currentDate.innerText = `${months[currentMonth]} ${currentYear}`;
    daysTag.innerHTML = liTag;
}
renderCalendar();

prevNextIcons.forEach(icon =>{
    icon.addEventListener("click", ()=>{
        currentMonth = icon.id === "prev" ? currentMonth-1 : currentMonth+1;
        

        if(currentMonth<0 || currentMonth>11){
            date=date.getFullYear();
            currentMonth = date.getMonth();
        }else{
            date = new Date();
        }
        renderCalendar();
    })
})

