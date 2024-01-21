let elements = Array.from(document.querySelectorAll(".thumbnail"))
let img, img_name

// adding event listener for every button

elements.forEach((btn) => {
    btn.addEventListener("click", () => {
        document.querySelector(".vote-modal").style.display = "block"
        document.getElementById("candidate-name").textContent = btn.lastElementChild.textContent
        
        // setting the image in the vote modal

        img_path = btn.firstElementChild.getAttribute("src")
        img = document.querySelector(".selected-img").firstElementChild
        img.setAttribute("scr", img_path)
        img.src = img_path

        // setting the value of the vote field
        document.querySelector("#vote").value = btn.lastElementChild.textContent
  
    })
})
    

// adding close function

close_btn = document.querySelector(".close")

close_btn.onclick = () =>{
    document.querySelector(".vote-modal").style.display = "none"
}
