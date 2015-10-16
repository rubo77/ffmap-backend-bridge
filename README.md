# ffmap-backend-bridge
two scripts, that serve ffmap-backend to access alfred and batman data

#Install
```
cd /opt
git clone https://github.com/rubo77/ffmap-backend-bridge srv-cgi
cd srv-cgi/
```
##adapt to your community

    # for example for `ffnord`:
    for i in *; do sed -i s/ffki/ffnord/g $i; done

##Install the needed tools to serve via http

    # for example
    apt-get install fcgiwrap
