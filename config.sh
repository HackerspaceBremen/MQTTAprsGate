export mycallsign=CALLSI-1
export mypasscode=12345

sed  -i "1i mycallsign = '""${mycallsign}'" app.py
sed  -i "1i mypasscode = '${mypasscode}'" app.py 

echo "Config aprs user"
echo ${mycallsign}
echo ${mypasscode}