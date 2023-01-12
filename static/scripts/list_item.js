const edit_bnt = document.querySelectorAll(".icon_edit")
const del_bnt = document.querySelectorAll(".icon_del")

console.log(del_bnt)

function delete_event(){
    let id = document.querySelector("#id")
    fetch(`/event_del/${id}`,{
    method:'DELETE'
}).then(response=>{
    return response.json()
}).then(data=>{console.log(data)}) 
}


del_bnt.forEach((el)=>{
    el.addEventListener("click", ()=>{
        const modal = document.querySelector(".modal_delete");
        modal.classList.remove("hidden")    
    })

    let input_id = document.querySelector("#id")

    input_id.value = el.value
})