// website/static/js/login.js

document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');
    const showPasswordToggle = document.getElementById('showPassword');

    loginForm.addEventListener('submit', function (e) {
        const username = loginForm.username.value.trim();
        const password = loginForm.password.value.trim();

        if (!username || !password) {
            e.preventDefault();
            alert('Please fill in both username and password.');
        }
    });

    if (showPasswordToggle) {
        showPasswordToggle.addEventListener('click', function () {
            const passwordInput = document.getElementById('password');
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            this.textContent = type === 'password' ? 'Show' : 'Hide';
        });
    }
});
