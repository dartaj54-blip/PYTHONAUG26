let registerForm = document.querySelector(".register");
let inputs = document.querySelectorAll(".register>input");
let textarea = document.querySelector("textarea");

registerForm.addEventListener("submit", (e) => {

    e.preventDefault();

    let name = inputs[0].value;
    let email = inputs[1].value;
    let phone = inputs[2].value;
    let dob = inputs[3].value;
    let gender = inputs[4].value;
    let address = textarea.value;
    let password = inputs[5].value;

    if (!name || !email || !phone || !dob || !gender || !address || !password) {
        alert("Kindly fill all the field");
        return;
    }

    let userData = {
        name,
        email,
        phone,
        dob,
        gender,
        address,
        password
    };

    localStorage.setItem("userData", JSON.stringify(userData));

    inputs[0].value = "";
    inputs[1].value = "";
    inputs[2].value = "";
    inputs[3].value = "";
    inputs[4].value = "";
    inputs[5].value = "";
    textarea.value = "";

    alert("success register");
});

let showButton = document.querySelector(".show");
let showContainer = document.querySelector(".show-container");

showButton.addEventListener("click", () => {

    let userData = JSON.parse(localStorage.getItem("userData"));

    for (let key in userData) {

        let b = document.createElement("b");
        let p = document.createElement("p");

        b.innerText = key;
        p.innerText = userData[key];

        showContainer.append(b, p);
    }
});