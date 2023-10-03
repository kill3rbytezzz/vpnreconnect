#!/bin/sh
GATEWAY="$2"
IP="$1"
mkdir -p /var/run/xl2tpd
/bin/sleep 1
touch /var/run/xl2tpd/l2tp-control
/bin/sleep 1
ipsec restart
/bin/sleep 1
service xl2tpd restart
/bin/sleep 3
ipsec up myvpn
/bin/sleep 3
echo "c myvpn" > /var/run/xl2tpd/l2tp-control
/bin/sleep 1
route add $IP gw $GATEWAY 
/bin/sleep 3
route add default dev ppp0