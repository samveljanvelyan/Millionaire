jQuery(document).ready(function($) {
    let sound = document.getElementById("audioId");
    sound.currentTime = 0;
    sound.loop = true;
    sound.play();
});