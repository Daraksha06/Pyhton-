function validate() {
    var uname = document.getElementById("uname").value;
    var pass = document.getElementById("pass").value;
    var span1 = document.getElementById("span1");
    var span2 = document.getElementById("span2");

    if (uname === "" || uname == null) {
        span1.innerHTML = "Username should not be empty";
        span1.style.color = "red";
    } else {
        span1.innerHTML = "";
    }

    if (pass === "" || pass == null) {
        span2.innerHTML = "Password should not be empty";
        span2.style.color = "red";
    } else {
        span2.innerHTML = "";
    }
}