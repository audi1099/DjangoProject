document.addEventListener('DOMContentLoaded', function () {
    const carCards = document.querySelectorAll('.card');
    carCards.forEach(card => {
        card.addEventListener('click', function() {
            const targetDetails = document.getElementById('car-details');
            targetDetails.style.display = 'block';
        });
    });
});