window.addEventListener('scroll',function(){
    const header = document.querySelector('header');
    
    header.classList.toggle("sticky", window.scrollY > 0);
    const body = document.querySelector('body');
    body.style.backgroundColor = window.scrollY > 0 ? 'red' : '';
});

function togglemenu(){
    const menutoggle = document.querySelector('.menutoggle');
    const navigation = document.querySelector('.navigation');
    menutoggle.classList.toggle('active');
    navigation.classList.toggle('active');
};