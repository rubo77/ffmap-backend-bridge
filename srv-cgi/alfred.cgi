#!/bin/sh

echo Status: 200 OK
echo Content-Type: application/json
echo

/usr/bin/alfred-json -s /var/run/alfred.bat-ffki.sock -r "$QUERY_STRING" -z

exit 0

# EOF
