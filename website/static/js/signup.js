// website/static/js/signup.js

document.addEventListener('DOMContentLoaded', function () {
    const signupForm = document.getElementById('signupForm');
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirmPassword');
    const showPasswordToggle = document.getElementById('showPassword');

    signupForm.addEventListener('submit', function (e) {
        const username = signupForm.username.value.trim();
        const password = passwordInput.value.trim();
        const confirmPassword = confirmPasswordInput.value.trim();

        if (!username || !password || !confirmPassword) {
            e.preventDefault();
            alert('All fields are required.');
            return;
        }

        if (password !== confirmPassword) {
            e.preventDefault();
            alert('Passwords do not match.');
        }
    });

    if (showPasswordToggle) {
        showPasswordToggle.addEventListener('click', function () {
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            confirmPasswordInput.setAttribute('type', type);
            this.textContent = type === 'password' ? 'Show' : 'Hide';
        });
    }
});
