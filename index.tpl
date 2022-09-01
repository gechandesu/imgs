<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>imgs</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
<main>

    % if not_found:
        <div class="not-found">
            <p><h1>404 Not found</h1></p>
            <h1>(╯°□°）╯︵ ┻━┻</h1>
        </div>
    % end

    % if bad_mime_type:
        <div class="bad-mime-type">
            <p><h1>415 Bad file MIME type</h1></p>
            <h1>(´•ω•̥`)</h1>
        </div>
    % end

    <div id="drop-area" class="drop-area" ondragover="dragOverHover();" ondragleave="dragLeave()">
        <form action="/" method="POST" enctype="multipart/form-data">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"· fill="none" stroke="#fff" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M3 15v4c0 1.1.9 2 2 2h14a2 2 0 0 0 2-2v-4M17 8l-5-5-5 5M12 4.2v10.3"/></svg><br>
            <label for="image_web" class="file-input-label"><b> Choose images</b> or drag and drop it here</label>
            <input class="file-input" type="file" multiple onchange="this.form.submit();" name='image_web' id='image_web'>
        </form>
    </div>

    <script>
        let dropArea = document.getElementById('drop-area');
        function dragOverHover() {
            dropArea.className = "drop-area dragover";
        }
        function dragLeave() {
            dropArea.className = "drop-area";
        }
    </script>

    <p><b>or</b> upload images via cURL:</p>

    <div class="curl">
        <pre>curl -F 'image=@/path/to/image.jpg' {{ base_url }}</pre>
    </div>

    % if uploaded:
        <div class="copy-to-clipboard">
            <input type="text" value="{{ image_url }}" id="text-input">
            <button onclick="CopyToClipboard()" onmouseout="mouseOut()">
                <span id="copy-button">Copy URL</span>
            </button>
        </div>

        <script>
            let copyButton = document.getElementById("copy-button"),
                copyText = document.getElementById("text-input");

            function CopyToClipboard() {
                copyText.select();
                copyText.setSelectionRange(0, 99999); /*For mobile devices*/
                document.execCommand("copy");
                copyButton.innerHTML = "Copied!";
            }
            function mouseOut() {
                copyButton.innerHTML = "Copy URL";
            }
        </script>

        <img src="{{ image_url }}" alt="{{ image_url }}" width="640">
    % end

    <div class="logo">
        <pre> __<br>|__| _____   ____  ______<br>|  |/     \ / ___\/  ___/<br>|  |  Y Y  / /_/  \___ \<br>|__|__|_|  \___  /____  ><br>         \/_____/     \/</pre>
    </div>
    <p><a href="https://github.com/AdrianR25/imgs" target="_blank">v1.2</a></p>

</main>
</body>
</html>
