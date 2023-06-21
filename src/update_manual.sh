#!/bin/sh -e

. $(dirname "${0}")/censorship_params.sh

LIST_OUT="${UNBOUND_CONF_DIR}/db.blacklist_manual.conf"
LIST_TYPE="manuale"

PARSER_BIN="${ROOT_DIR}/censor_parser.py"
PARSER_OPTS="-i ${MANUAL_LIST_FILE} -o ${LIST_OUT} -f ${OUTPUT_FORMAT} -d ${LIST_TYPE} -b ${BLACKHOLE_MANUAL}"

if [ -f "${MANUAL_LIST_FILE}" ]
then
   ${PARSER_BIN} ${PARSER_OPTS}
else
    echo "No manual list file found, skipping."
fi

