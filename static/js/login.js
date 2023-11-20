var loginForm = document.getElementById('loginForm');
if (loginForm) {
    loginForm.onsubmit = function(event) {
        event.preventDefault(); // Prevent default form submission

        var username = document.querySelector('[name="username"]').value;
        var password = document.querySelector('[name="password"]').value;

        // AJAX request to the server
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
        })
        .then(response => {
            if (response.redirected) {
                window.location.href = response.url;
            } else {
                // Handle login failure
                alert("Invalid username or password");
                document.getElementById('loginPopup').style.display = "none";
                document.body.classList.remove('popup-active');
            }
        })
        .catch(error => console.error('Error:', error));
    };
}
