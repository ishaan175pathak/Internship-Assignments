let password_field = document.getElementsByTagName("input")[2]
let email = document.getElementsByTagName("input")[1]
let form_btn = document.getElementsByTagName("form")[0].lastElementChild.firstElementChild
var field = document.getElementsByClassName("form-group")[3]
var email_result = false, password = false


email.addEventListener("keyup", ()=>{
    if(email.value.includes("@xyz.com")){
        email_result = true
    }
    else{
        email_result = false
    }
    
    enableSubmit()
})

password_field.addEventListener("keyup", ()=>{
    var capital = checkCapitalValidity();
    var number = checkNumberValidity();
    var length = checkLengthValidity();
    password = capital && number && length ? true : false

    enableSubmit()
})

function checkCapitalValidity(){
    
    if (password_field.value && !password_field.value[0].match(/\d+/g) && password_field.value[0] == password_field.value[0].toUpperCase()){
        field.firstElementChild.firstElementChild.classList.replace("wrong_text", "success_text")
        field.firstElementChild.firstElementChild.firstElementChild.innerHTML = "&#10004;"
        return true
    }
    else{
        field.firstElementChild.firstElementChild.classList.replace("success_text", "wrong_text")
        field.firstElementChild.firstElementChild.firstElementChild.innerHTML = "&#10006;"
        return false
    }
}

function checkNumberValidity(){
    
    var regex = /\d+/g;

    if (password_field.value.match(regex)){
        field.firstElementChild.children[1].classList.replace("wrong_text", "success_text")
        field.firstElementChild.children[1].firstElementChild.innerHTML = "&#10004;"
        return true
    }
    else{
        field.firstElementChild.children[1].classList.replace("success_text", "wrong_text")
        field.firstElementChild.children[1].firstElementChild.innerHTML = "&#10006;"
        return false
    }
}

function checkLengthValidity(){
        
    if (password_field.value && password_field.value.length >= 10){
        field.firstElementChild.lastElementChild.classList.replace("wrong_text", "success_text")
        field.firstElementChild.lastElementChild.firstElementChild.innerHTML = "&#10004;"
        return true
    }
    else{
        field.firstElementChild.lastElementChild.classList.replace("success_text", "wrong_text")
        field.firstElementChild.lastElementChild.firstElementChild.innerHTML = "&#10006;"
        return false
    }
}

function enableSubmit(){
    if(email_result && password){
        form_btn.removeAttribute("disabled")
    }
    else{
        form_btn.setAttribute("disabled", true)
    }
}