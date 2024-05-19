document.addEventListener('DOMContentLoaded', function() {
    var myCarousel = document.querySelector('#newsCarousel');
    var carousel = new bootstrap.Carousel(myCarousel, {
        interval: 2000,
        wrap: true
    });

    // Dark mode toggle
    var toggleSwitch = document.querySelector('.toggle-switch input[type="checkbox"]');
    toggleSwitch.addEventListener('change', function() {
        if (this.checked) {
            document.body.classList.add('dark-mode');
        } else {
            document.body.classList.remove('dark-mode');
        }
    });
});

