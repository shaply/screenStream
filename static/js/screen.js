let scrn = null;
let count = 1;
let scrn64 = "";

$(document).ready(function() {
    window.alert("Start");
    scrn = document.getElementById("livefeed");
    window.setInterval(randomFunc, 1000);
});

function randomFunc() {
    fetch('/getScreen')
        .then(response => response.json())
        .then(data => {
            scrn64 = data.ssBase64;
        });
    scrn.setAttribute("src", "data:image/jpeg;base64," + scrn64);
}