let form = document.querySelector("#registerForm");

let name = document.querySelector("#name");
let email = document.querySelector("#email");
let phone = document.querySelector("#phone");
let course = document.querySelector("#course");
let password = document.querySelector("#password");
let confirmPassword = document.querySelector("#confirmPassword");
let message = document.querySelector("#message");

let gender = document.querySelectorAll('input[name="gender"]');

form.addEventListener("submit", (e) => {
    e.preventDefault();

    let selectedGender = "";

    for (let i = 0; i < gender.length; i++) {
        if (gender[i].checked) {
            selectedGender = gender[i].value;
        }
    }

    if (
        name.value == "" ||
        email.value == "" ||
        phone.value == "" ||
        selectedGender == "" ||
        course.value == "" ||
        password.value == "" ||
        confirmPassword.value == ""
    ) {
        message.textContent = "Please fill all fields";
        message.style.color = "red";
        return;
    }

    if (password.value != confirmPassword.value) {
        message.textContent = "Password does not match";
        message.style.color = "red";
        return;
    }

    let student = {
        name: name.value,
        email: email.value,
        phone: phone.value,
        gender: selectedGender,
        course: course.value,
        password: password.value
    };

    localStorage.setItem("student", JSON.stringify(student));

    message.textContent = "Registration successful";
    message.style.color = "green";

    name.value = "";
    email.value = "";
    phone.value = "";
    course.value = "";
    password.value = "";
    confirmPassword.value = "";

    for (let i = 0; i < gender.length; i++) {
        gender[i].checked = false;
    }
});