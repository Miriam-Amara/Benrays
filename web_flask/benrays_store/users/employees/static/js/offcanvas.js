// from chatgpt

// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', () => {
    // Show the offcanvas automatically
    new bootstrap.Offcanvas(document.getElementById('staticBackdrop')).show();

    // Redirect when the close button is clicked
    document.getElementById('closeRedirectBtn').addEventListener('click', (event) => {
        const redirectUrl = event.target.getAttribute('data-redirect');
        window.location.href = redirectUrl;
    });
});
