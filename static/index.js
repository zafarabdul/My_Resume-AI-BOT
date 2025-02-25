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
function change(a){
    var ch=document.getElementById("chat");
    var ic=document.getElementById("icon");
    if(a==1){
        ic.style.display="none";
        ch.style.display="block";
    }
    else{
        ic.style.display="block";
        ch.style.display="none";
    }
}
document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".card, ul,h4"); // Select both cards and containers

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("in-view");
            }
            else{
                entry.target.classList.remove("in-view");
            }
        });
    }, { threshold: 0.5 }); // Trigger when 50% of the element is visible

    elements.forEach(element => {
        observer.observe(element);
    });
});

