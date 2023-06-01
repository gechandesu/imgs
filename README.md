# imgs

imgs is a minimalictic image sharing web app written with Bottle framework.

No database. No image compression. No time limits. No additional dependencies.

Features:

* Upload images via Drag&Drop
* Easy copy share link
* MIME type detecting

See deployment options in Bottle documentation: https://bottlepy.org/docs/dev/deployment.html

# Run imgs in Docker

Clone repository and edit **imgs.ini**.

Build Docker image:

```shell
docker build --tag imgs .
```

Run container from image. Replace **/path/to/your/uploads/dir** with path to directory where you want to store images:

```shell
docker run -d \
    --name imgs \
    --publish 127.0.0.1:5000:5000 \
    --volume /path/to/your/uploads/dir:/opt/imgs/uploads \
    imgs
```

imgs will launched on `127.0.0.1:5000`. Set up reverse proxy server. I recommed to use basic authentication to prevent abuses. 

## Nginx virtual host example:

```nginx
server {
    listen 80;
    server_name yourdomain.tld;
    root /path/to/imgs/root;

    location / {
        auth_basic "Authentication required";
        auth_basic_user_file /path/to/.htpasswd;
        proxy_pass http://127.0.0.1:5000;
    }

    location ~* ^/favicon.ico$ {
        try_files $uri $uri/ =404;
    }

    location ~* \..* {
        auth_basic off;
        proxy_pass http://127.0.0.1:5000;
    }
}
```

## Apache2 virtual host example

```apache2

<VirtualHost *:80>
    ServerName yourdomain.tld
 	AllowEncodedSlashes     NoDecode

    RewriteEngine On
	RemoteIPHeader X-Remote-Ip

    ProxyRequests off
    ProxyPreserveHost on
    <LocationMatch "^/.">
        Allow From All
        Satisfy Any
        ProxyPass "http://127.0.0.1:5000/"
        ProxyPassReverse "http://127.0.0.1:5000/"
    </LocationMatch>
    <Location />
        AuthName "Authentication required"
        AuthType Basic
        AuthBasicProvider file
        AuthUserFile "/path/to/.htpasswd"
        Require valid-user
        ProxyPass "http://127.0.0.1:5000/"
        ProxyPassReverse "http://127.0.0.1:5000/"
    </Location>

   

</VirtualHost>

```

# Additional

## imgs client with CLI

imgs has a simple CLI tool based on curl. Copy **imgs** script to your PATH.

```shell
sudo cp imgs /usr/bin/imgs
```

## Nautilus integration

Push files to your imgs instance via GNOME Files (former name: Nautilus). Depends on: curl, libnotify (notify-send utility).

Just place **Upload to imgs** script into **~/.local/share/nautilus/scripts/** directory.

```shell
DIR=~/.local/share/nautilus/scripts/; mkdir -p $DIR && cp Upload\ to\ imgs $DIR
```
