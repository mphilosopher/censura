#!/bin/sh -e

. $(dirname "${0}")/censorship_params.sh

${ROOT_DIR}/update_cncpo.sh || true
${ROOT_DIR}/update_consob.sh || true
${ROOT_DIR}/update_aams.sh  || true
${ROOT_DIR}/update_admt.sh  || true
${ROOT_DIR}/update_manual.sh  || true

/usr/local/etc/rc.d/unbound reload # or `rndc reload` according to your mileage
