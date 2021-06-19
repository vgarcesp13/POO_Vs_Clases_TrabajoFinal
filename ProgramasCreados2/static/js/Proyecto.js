const Enlace = document.querySelector(".Enlaces")
const Salchi = document.getElementsByClassName("Salchipapa")[0]
const MSalchi = document.getElementById("Salchipapa")

const QuitarPonerMenu = () =>{
    Enlace.classList.toggle('Enlaces2')
    Enlace.style.transition = "transform 0.5s ease-in-out"
}
MSalchi.addEventListener('click',()=> QuitarPonerMenu())