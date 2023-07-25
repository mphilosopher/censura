#!/bin/sh -e

. $(dirname "${0}")/censorship_params.sh

ADMT_DOMAIN="https://www.adm.gov.it"
PAGE_URL="${ADMT_DOMAIN}/portale/siti-inibiti-tabacchi"
LIST_FILE="${TMP_DL_DIR}/blacklist_admt.txt"
LIST_OUT="${UNBOUND_CONF_DIR}/db.blacklist_admt.conf"
LIST_TYPE="admt"
BLACKHOLE="217.175.53.228"

WGET_CERTS=""
WGET_OPTS="${WGET_CERTS} --no-check-certificate"

if [ ! -d "${TMP_DL_DIR}" ]
then
   echo "Missing temp download dir ${TMP_DL_DIR}"
   mkdir "${TMP_DL_DIR}"
fi

##############################################################################
# be verbose when stdout is a tty
if [ ! -t 0 ]; then
  WGET_OPTS="$WGET_OPTS -q"
fi

LIST_URL=$(${WGET_BIN} ${WGET_OPTS} ${PAGE_URL} -q -O - | ${GNU_GREP_BIN} -Po "(?<=href=\")[^^\"]*/elenco_siti_inibiti_tabacchi.txt")
if [ -z ${LIST_URL} ]
then
  exit 1
fi
LIST_URL="${ADMT_DOMAIN}${LIST_URL}"
PARSER_OPTS="-i ${LIST_FILE} -o ${LIST_OUT} -f ${OUTPUT_FORMAT} -d ${LIST_TYPE} -b ${BLACKHOLE}"


## downloading ###############################################################
${WGET_BIN} ${WGET_OPTS} ${LIST_URL} -O ${LIST_FILE}

## parsing ###################################################################
${PARSER_BIN} ${PARSER_OPTS}
