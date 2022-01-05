# imgs

imgs is a minimalictic image sharing web app written with Bottle framework.

No database. No image compression. No time limits. No additional dependencies.

Features:
* Upload images via Drag&Drop
* Easy copy share link
* MIME type detecting

See deployment options in Bottle documentation: https://bottlepy.org/docs/dev/deployment.html

# Additional

## imgs client with CLI

imgs has a simple CLI tool based on curl. Copy **imgs** script to your PATH.

```bash
sudo cp imgs /usr/bin/imgs
```

## Nautilus integration

Push files to your imgs instance via GNOME Files (former name: Nautilus). Depends packages: curl, notyfy-send.

Just place **Upload to imgs** script into **~/.local/share/nautilus/scripts**.
