#!/bin/sh -e

. $(dirname "${0}")/censorship_params.sh

${ROOT_DIR}/update_cncpo.sh
${ROOT_DIR}/update_aams.sh
${ROOT_DIR}/update_admt.sh
${ROOT_DIR}/update_manual.sh

/usr/local/etc/rc.d/unbound reload
