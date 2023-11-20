var registerButton = document.getElementById('registerButton');

if (registerButton) {
    registerButton.onclick = function() {
        var username = document.querySelector('[name="username"]').value;
        var password = document.querySelector('[name="password"]').value;

        fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            if (data.status === "success") {
                // Close the popup or provide a clear indication to the user to now log in
                document.getElementById('loginPopup').style.display = "none";
            }
        })
        .catch(error => console.error('Error:', error));
    };
}
