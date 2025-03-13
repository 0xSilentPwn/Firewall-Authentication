document.querySelectorAll('.input-box input').forEach(input => {
    input.addEventListener('focus', () => {
        input.previousElementSibling.style.color = "#1DBF73";
    });
    input.addEventListener('blur', () => {
        input.previousElementSibling.style.color = "rgba(255, 255, 255, 0.7)";
    });
});
