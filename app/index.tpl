<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>imgs</title>
    <link rel="stylesheet" href="/style.css">
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const useOriginalNameCheckbox = document.querySelector('input[name="use_original_name"]');
            const overwriteExistingCheckbox = document.querySelector('input[name="overwrite_existing"]');

            function toggleOverwriteCheckbox() {
                overwriteExistingCheckbox.disabled = !useOriginalNameCheckbox.checked;
                if (!useOriginalNameCheckbox.checked) {
                    overwriteExistingCheckbox.checked = false;
                }
            }

            useOriginalNameCheckbox.addEventListener('change', toggleOverwriteCheckbox);

            // Initial check on page load
            toggleOverwriteCheckbox();
        });
    </script>

</head>
<body>
<main>

    % if not_found:
        <div class="not-found">
            <p><h1>404 Not found</h1></p>
            <h1>(╯°□°）╯︵ ┻━┻</h1>
        </div>
   

    % elif bad_mime_type:
        <div class="bad-mime-type">
            <p><h1>415 Bad file MIME type</h1></p>
            <h1>(´•ω•̥`)</h1>
        </div>
    % else:

    
        <form action="/" method="POST" enctype="multipart/form-data">
            <div class="file-upload-container drop-area" id="drop-area" ondragover="dragOverHover();" ondragleave="dragLeave()">
                <input class="file-input" type="file" multiple onchange="this.form.submit();" name='image_web' id='image_web'>
                <label for="image_web" class="file-input-label">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M3 15v4c0 1.1.9 2 2 2h14a2 2 0 0 0 2-2v-4M17 8l-5-5-5 5M12 4.2v10.3"/></svg><br>
                    <b>Choose images</b> or drag and drop them here
                </label>
            </div>
            <div class="options">
                <label><input type="checkbox" name="use_original_name"> Use original file name</label><br>
                <label><input type="checkbox" name="overwrite_existing"> Overwrite if file exists</label>
            </div>
        </form>



        <script>
            let dropArea = document.getElementById('drop-area');
            function dragOverHover() {
                dropArea.className = "file-upload-container drop-area dragover";
            }
            function dragLeave() {
                dropArea.className = "file-upload-container drop-area";
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

            <p>- - -</p>
        % end
    % end

    <div class="logo">
        <pre> __<br>|__| _____   ____  ______<br>|  |/     \ / ___\/  ___/<br>|  |  Y Y  / /_/  \___ \<br>|__|__|_|  \___  /____  ><br>         \/_____/     \/</pre>
    </div>
    <p><a href="https://git.nxhs.cloud/ge/imgs" target="_blank">v1.2</a></p>

</main>
</body>
</html>
