// change drop area style when dragging a file
const dropArea = document.getElementById('drop-area');
function dragOverHover() {
    dropArea.className = "drop-area dragover";
}
function dragLeave() {
    dropArea.className = "drop-area";
}

// copy URL button
const copyButton = document.getElementById("copy-button");
const copyText = document.getElementById("text-input");

function CopyToClipboard() {
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/
    document.execCommand("copy");
    copyButton.innerHTML = "Copied!";
}
function mouseOut() {
    copyButton.innerHTML = "Copy URL";
}


// set default volume to 50% for audio element
const audioPlayer = document.getElementById("audio-player");
if (audioPlayer) {
    audioPlayer.volume = 0.5;
}
