#!/bin/sh -e

. $(dirname "${0}")/censorship_params.sh

LIST_URL='https://203.0.113.113/' #Replace with the correct IP address
LIST_FILE="${TMP_DL_DIR}/blacklist_cncpo.csv"
LIST_OUT="${UNBOUND_CONF_DIR}/db.blacklist_cncpo.conf"
LIST_TYPE="cncpo"

WGET_CERT_FILE="${ROOT_DIR}/cncpo.pem"
WGET_CERTS="--certificate=${WGET_CERT_FILE}"
WGET_OPTS="${WGET_CERTS} --no-check-certificate"
PARSER_OPTS="-i ${LIST_FILE} -o ${LIST_OUT} -f ${OUTPUT_FORMAT} -d ${LIST_TYPE} -b ${BLACKHOLE_CNCPO}"

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

## downloading ###############################################################
${WGET_BIN} ${WGET_OPTS} ${LIST_URL} -O ${LIST_FILE}

## parsing ###################################################################
${PARSER_BIN} ${PARSER_OPTS}
