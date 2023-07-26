 // Auto-dismiss the messages after 5 seconds
 setTimeout(function() {
    var messages = document.getElementsByClassName('messages');
    if (messages.length > 0) {
        messages[0].style.display = 'none';
    }
}, 5000);

// Add event listener to close button to manually dismiss the error message
// var closeButton = document.getElementsByClassName('close-button');
// if (closeButton.length > 0) {
//     closeButton[0].addEventListener('click', function() {
//         var messages = document.getElementsByClassName('messages');
//         if (messages.length > 0) {
//             messages[0].style.display = 'none';
//         }
//     });
// }


