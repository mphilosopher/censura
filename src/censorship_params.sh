#!/bin/sh -e
# Tune the following parameters according to your environment

ROOT_DIR="/root/censorship/src"
TMP_DL_DIR="${ROOT_DIR}/tmp"
PARSER_BIN="${ROOT_DIR}/censor_parser.py"
WGET_BIN=$(which wget)
GNU_GREP_BIN=$(which grep)

BLACKHOLE="127.0.0.1" #Replace with the chosen IP address
OUTPUT_FORMAT="unbound"  # Replace to "bind" or to "unbound" or to "powerdns"

# Unbound params
UNBOUND_CONF_DIR="/usr/local/etc/unbound/blacklists.d"

# Bind params
BIND_CONF_DIR="/etc/bind/zones/blacklist.d"
