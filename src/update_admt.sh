#!/bin/sh -e

. $(dirname "${0}")/censorship_params.sh

LIST_URL="https://www1.adm.gov.it/files_siti_inibiti_tabacchi/elenco_siti_inibiti.txt"
LIST_FILE="${ROOT_DIR}/tmp/blacklist_admt.txt"
LIST_OUT="${UNBOUND_CONF_DIR}/db.blacklist_admt.conf"
LIST_TYPE="admt"

WGET_CERTS=""
WGET_OPTS="${WGET_CERTS} --no-check-certificate"

PARSER_OPTS="-i ${LIST_FILE} -o ${LIST_OUT} -f ${OUTPUT_FORMAT} -d ${LIST_TYPE} -b ${BLACKHOLE}"

##############################################################################
# be verbose when stdout is a tty
if [ ! -t 0 ]; then
  WGET_OPTS="$WGET_OPTS -q"
fi

## downloading ###############################################################
${WGET_BIN} ${WGET_OPTS} ${LIST_URL} -O ${LIST_FILE}

## parsing ###################################################################
${PARSER_BIN} ${PARSER_OPTS}
