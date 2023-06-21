#!/bin/sh -e
# Tune the following parameters according to your environment

ROOT_DIR="/root/censorship/src"
TMP_DL_DIR="${ROOT_DIR}/tmp"
PARSER_BIN="${ROOT_DIR}/censor_parser.py"
WGET_BIN=$(which wget)

MANUAL_LIST_FILE="${ROOT_DIR}/blacklist_manual.txt"

BLACKHOLE_CNCPO="127.0.0.1" #Replace with the chosen IP address for the CNCPO list
BLACKHOLE_AGCOM="127.0.0.1" #Replace with the chosen IP address for the AGCOM list
BLACKHOLE_AAMS="217.175.53.72" #Replace, if changed, with the chosen IP address for the AAMS list
BLACKHOLE_ADMT="217.175.53.228" #Replace, if changed, with the chosen IP address for the ADMT list
BLACKHOLE_MANUAL="127.0.0.1" #Replace with the chosen IP address for the Manual list

OUTPUT_FORMAT="unbound"  # Replace to "bind" or to "unbound"

# Unbound params
UNBOUND_CONF_DIR="/usr/local/etc/unbound/blacklists.d"

# Bind params
BIND_CONF_DIR="/etc/bind/zones/blacklist.d"
