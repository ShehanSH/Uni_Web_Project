window.addEventListener('scroll',function(){
    const header = document.querySelector('header');
    const body = document.querySelector('body');
    header.classList.toggle("sticky", window.scrollY > 0);
    body.classList.toggle("background-color:red", window.scrollY > 0);
});
