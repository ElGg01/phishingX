const code = document.getElementById("2FACODE");

function closeModal() {
    location.href = "/"
}

function send() {
    if (code.value != "") {
        document.getElementById('login-form').submit();
        return false;
    };
}