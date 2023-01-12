const date = new Date();
const now = date.toLocaleString();


const currentDate = date.toISOString().substring(0,10);
const currentTime = date.toISOString().substring(11,16);

document.getElementById('date').value = currentDate;
document.getElementById('time').value = currentTime;