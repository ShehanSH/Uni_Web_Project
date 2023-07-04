

window.addEventListener('scroll',function(){
    const header = document.querySelector('header');
    
    header.classList.toggle("sticky", window.scrollY > 0);
    const body = document.querySelector('body');
    body.style.backgroundColor = window.scrollY > 0 ? '#f0e1e1' : '';
});

function togglemenu(){
    const menutoggle = document.querySelector('.menutoggle');
    const navigation = document.querySelector('.navigation');
    menutoggle.classList.toggle('active');
    navigation.classList.toggle('active');
};