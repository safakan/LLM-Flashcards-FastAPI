var logoutButton = document.getElementById('logoutButton');
if (logoutButton) {
    logoutButton.onclick = function() {
        var confirmation = confirm("Are you sure you want to log out?");
        if (confirmation) {
            window.location.href = '/logout';
        }
    };
}
