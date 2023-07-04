 // Auto-dismiss the messages after 5 seconds
 setTimeout(function() {
    var messages = document.getElementsByClassName('messages');
    if (messages.length > 0) {
        messages[0].style.display = 'none';
    }
}, 5000);

// Add event listener to close button to manually dismiss the error message
var closeButton = document.getElementsByClassName('close-button');
if (closeButton.length > 0) {
    closeButton[0].addEventListener('click', function() {
        var messages = document.getElementsByClassName('messages');
        if (messages.length > 0) {
            messages[0].style.display = 'none';
        }
    });
}


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