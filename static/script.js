function togglePassword() {

    var password =
    document.getElementById("password");

    if(password.type === "password") {
        password.type = "text";
    }

    else {
        password.type = "password";
    }
}
function generatePassword() {

    let chars =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";

    let password = "";

    for(let i = 0; i < 12; i++) {

        password += chars.charAt(
            Math.floor(Math.random() * chars.length)
        );
    }

    document.getElementById("password").value = password;
}
function copyPassword() {

    let password =
    document.getElementById("password");

    navigator.clipboard.writeText(
        password.value
    );

    alert("Password copied!");
}