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
    const copyText = document.getElementById("text-input");

    if (navigator.clipboard) {
        navigator.clipboard.writeText(copyText.value).then(() => {
            copyButton.innerHTML = "Copied!";
        }, () => {
            console.error('Could not copy text: ', err);
        });
    } else { // fallback for insecure environments 
        copyText.select();
        document.execCommand("copy");
        copyButton.innerHTML = "Copied!";
    }
}

// set default volume to 50% for audio element
const audioPlayer = document.getElementById("audio-player");
if (audioPlayer) {
    audioPlayer.volume = 0.5;
}
