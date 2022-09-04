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

function CopyToClipboard() {
    const copyText = document.getElementById("text-input").value;

    navigator.clipboard.writeText(copyText).then(() => {
        copyButton.innerHTML = "Copied!";
    }, () => {
        console.error('Could not copy text: ', err);
    });
}

function mouseOut() {
    copyButton.innerHTML = "Copy URL";
}

// set default volume to 50% for audio element
const audioPlayer = document.getElementById("audio-player");
if (audioPlayer) {
    audioPlayer.volume = 0.5;
}
