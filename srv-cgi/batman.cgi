#!/bin/sh

echo Status: 200 OK
echo Content-Type: application/json
echo
echo -n '{"gw":"'$(sudo /usr/sbin/batctl -m bat-ffki gw)'",'
echo -n '"gwl":"'$(sudo /usr/sbin/batctl -m bat-ffki gwl -n | base64 -w 0)'",'

# nicht mehr n..tig bei meshviewer:
echo -n '"vd":"'$(sudo /usr/sbin/batctl -m bat-ffki vd json -n | sort -u | gzip -c | base64 -w 0)'",'

echo -n '"vis":"'$(sudo /opt/alfred/vis/batadv-vis -i bat-ffki -u /var/run/alfred.bat-ffki.sock -f json | sort -u | gzip -c | base64 -w 0)'"}'

exit 0

# EOF
