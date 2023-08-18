#!/bin/sh -e

. $(dirname "${0}")/censorship_params.sh

LIST_FILE="${TMP_DL_DIR}/blacklist_consob.txt"
LIST_OUT="${UNBOUND_CONF_DIR}/db.blacklist_consob.conf"
LIST_TYPE="consob"
BLACKHOLE="127.0.0.1"

if [ ! -d "${TMP_DL_DIR}" ]
then
   echo "Missing temp download dir ${TMP_DL_DIR}"
   mkdir "${TMP_DL_DIR}"
fi

PARSER_OPTS="-i ${LIST_FILE} -o ${LIST_OUT} -f ${OUTPUT_FORMAT} -d ${LIST_TYPE} -b ${BLACKHOLE}"

## downloading ###############################################################
$(python3 $(dirname "${0}")/download_consob.py -o ${LIST_FILE})

## parsing ###################################################################
${PARSER_BIN} ${PARSER_OPTS}
