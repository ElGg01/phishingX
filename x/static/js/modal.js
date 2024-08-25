const loginBTN = document.getElementById("loginBTN");
const modal = document.getElementById("modal");

const inputEmail = document.getElementById("log_in");

function openModal(){
    modal.style.display = "flex";
}

function closeModal(){
    modal.style.display = "none";
}

function getEmail() {
    const email = inputEmail.value;

    console.log(email);
}