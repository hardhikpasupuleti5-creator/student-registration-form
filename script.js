
document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let phone = document.getElementById("phone").value;
    let gender = document.getElementById("gender").value;
    let course = document.getElementById("course").value;

    document.getElementById("message").innerHTML =
        "Registration Successful! Welcome " + name;

    console.log(name, email, phone, gender, course);

    this.reset();
});
