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