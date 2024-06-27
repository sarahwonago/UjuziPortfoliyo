document.addEventListener('DOMContentLoaded', function() {
    var dropdowns = document.querySelectorAll('.dropdown .dropbtn');
    var links = document.querySelectorAll('.dropdown-content a');
    var dashboardItems = document.querySelectorAll('.dashboard-item');

    dropdowns.forEach(function(dropdown) {
        dropdown.addEventListener('click', function() {
            var dropdownContent = this.nextElementSibling;
            var arrow = this.querySelector('.arrow');

            if (dropdownContent.style.display === 'block') {
                dropdownContent.style.display = 'none';
                arrow.classList.remove('open');
            } else {
                dropdownContent.style.display = 'block';
                arrow.classList.add('open');
            }
        });
    });

    links.forEach(function(link) {
        link.addEventListener('click', function() {
            links.forEach(function(link) {
                link.classList.remove('active');
            });
            this.classList.add('active');
        });
    });

    dashboardItems.forEach(function(item) {
        item.addEventListener('click', function() {
            dashboardItems.forEach(function(item) {
                item.classList.remove('active');
            });
            this.classList.add('active');
        });
    });
});
