document.addEventListener('DOMContentLoaded', function() {
    const animatedBox = document.querySelector('.profiles');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animatedBox.classList.add('in-view');
            }
            else{
                // animatedBox.classList.remove('in-view');
            }
        });
s
    });

    observer.observe(animatedBox);
});

