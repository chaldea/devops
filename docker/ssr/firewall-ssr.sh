#!/bin/bash
echo remove port: $1
firewall-cmd --zone=public --remove-port=$1/tcp --permanent
firewall-cmd --zone=public --remove-port=$1/udp --permanent
echo add port: $2
firewall-cmd --zone=public --add-port=$2/tcp --permanent
firewall-cmd --zone=public --add-port=$2/udp --permanent
firewall-cmd --reload
firewall-cmd --zone=public --list-ports