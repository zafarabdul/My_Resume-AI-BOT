document.addEventListener('DOMContentLoaded', function () {
    const profileContainer = document.querySelector('.profiles');
    const profiles = [...document.querySelectorAll('.platform')];

    // Clone the profiles for seamless looping
    profiles.forEach(profile => {
        let clone = profile.cloneNode(true);
        profileContainer.appendChild(clone);
    });

    profileContainer.classList.add('in-view'); // Start animation immediately
});
