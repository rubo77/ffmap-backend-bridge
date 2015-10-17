# ffmap-backend-bridge
two scripts, that serve ffmap-backend to access alfred and batman data

#Install

    cd ~/
    git clone https://github.com/rubo77/ffmap-backend-bridge
    cd ffmap-backend-bridge/srv-cgi/

#####\#adapt to your community for example for `ffnord`:
    
    for i in *; do sed -i s/ffki/ffnord/g $i; done

#####\#copy cgi files into /opt/srv-cgi/:
    
    cp -a ../srv-cgi/ /opt

#####\#Install the needed tools to serve via http

```
apt-get install fcgiwrap nginx

#####\#configure nginx

cp /usr/share/doc/fcgiwrap/examples/nginx.conf /etc/nginx/fcgiwrap.conf
cd /etc/nginx/sites-available/
cat > /etc/nginx/sites-available/ffmap-backend <<EOF
server {
  listen 80;

  root /var/www;

  location ~ ^/[0-9a-z_-]+.cgi$ {
    root /opt/srv-cgi/;
    include /etc/nginx/fcgiwrap.conf;
    allow all;
    gzip off;
  }
}
EOF
cd ../sites-enabled/
ln -s ../sites-available/ffmap-backend .
rm /etc/nginx/sites-enabled/default
/etc/init.d/fcgiwrap restart
/etc/init.d/nginx restart
```
# open problem:
    
    Restarting nginx: nginx: [emerg] location "/cgi-bin/" is outside location "^/[0-9a-z_-]+.cgi$" in /etc/nginx/fcgiwrap.conf:3
