#!/bin/sh -e

. $(dirname "${0}")/censorship_params.sh

LIST_URL='https://203.0.113.113/' #Replace with the correct IP address
LIST_FILE="${ROOT_DIR}/tmp/blacklist_cncpo.csv"
LIST_OUT="${UNBOUND_CONF_DIR}/db.blacklist_cncpo.conf"
LIST_TYPE="cncpo"

WGET_CERT_FILE="${ROOT_DIR}/cncpo.pem"
WGET_CERT_KEY="${ROOT_DIR}/cncpo.key"
WGET_CERT_CA="${ROOT_DIR}/cncpo-ca.pem"
WGET_CERTS="--certificate=${WGET_CERT_FILE} --private-key=${WGET_CERT_KEY} --ca-certificate=${WGET_CERT_CA}"
WGET_OPTS="${WGET_CERTS} --no-check-certificate"
BLACKHOLE="192.0.2.80" #Replace with the IP address of a stop page
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
