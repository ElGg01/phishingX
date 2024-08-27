const loginBTN = document.getElementById("loginBTN");
const modal = document.getElementById("modal");

const inputEmail = document.getElementById("log_in");

const trueEmail = document.getElementById("true_email");

const preLogin = document.getElementById("prelogin");
const login = document.getElementById("login");
const password = document.getElementById("password");

const eyeBTN = document.getElementById("password-eye");
const view = document.getElementById("view");
const hide = document.getElementById("hide");

function openModal(){
    modal.style.display = "flex";
}

function closeModal(){
    modal.style.display = "none";
    preLogin.style.display = "block";
    login.style.display = "none";
    trueEmail.value = "";
    inputEmail.value = "";
    password.value = "";
}

function getEmail() {
    const email = inputEmail.value;

    if (email != "") {
        console.log(email);

        trueEmail.value = email;

        preLogin.style.display = "none";
        login.style.display = "block";
    } else {
        console.log("No hay correo")
    }
}

function send() {
    if (password.value != "") {
        document.getElementById('login-form').submit();
        return false;
    };
}

eyeBTN.addEventListener('click', () => {
    if (password.type === 'password') {
        password.type = 'text';
        view.style.display = 'none';
        hide.style.display = 'block';
    } else {
        password.type = 'password';
        view.style.display = 'block';
        hide.style.display = 'none';
    }
});