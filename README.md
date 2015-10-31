# ffmap-backend-bridge
two scripts, that serve ffmap-backend to access alfred and batman data

#Install

#####\#Install the needed tools to serve via http

    apt-get install fcgiwrap nginx apt-get install alfred-json

#####\#clone repository
    cd ~/
    git clone https://github.com/rubo77/ffmap-backend-bridge


#####\#adapt to your community for example for `ffnord`:
    
    cd ffmap-backend-bridge/srv-cgi/
    for i in *; do sed -i s/ffki/ffnord/g $i; done

#####\#copy cgi files into /opt/srv-cgi/:
    
    cp -a ../srv-cgi/ /opt


#####\#configure nginx

```
cd - # back to this git repository
cp etc/nginx/sites-available/ffmap-backend /etc/nginx/sites-available/
cd /etc/nginx/sites-enabled/
ln -s ../sites-available/ffmap-backend .
rm /etc/nginx/sites-enabled/default
/etc/init.d/fcgiwrap restart
/etc/init.d/nginx restart
```


# on the service mashine:
```
cd /opt/
git clone git://git.freifunk.in-kiel.de/ffmap-backend
\# adapt to your site, in this example '89.163.225.200'
sed s/vpn0.freifunk.in-kiel.de/89.163.225.200/g /opt/ffmap-backend/mkmap.sh -i

mkdir /opt/ffmap-backend/json

cd /etc/cron.d
ln -s /opt/ffmap-backend/crontab ffmap-backend
chmod +x /opt/ffmap-backend/crontab
```

######\# allow port 80
```
cat > /etc/iptables.d/600-Allow-HTTP <<EOF
# Allow ssh on wan and mesh
ip46tables -A wan-input -p tcp -m tcp --dport 80    -j ACCEPT
ip46tables -A mesh-input -p tcp -m tcp --dport 80    -j ACCEPT
EOF
build-firewall
#give SGID (Set Group ID up on execution) rights to alfred-json
chmod u+s /usr/bin/alfred-json
```

# open problem:

* alfred output is empty