#!/bin/sh


# +
# edit as required
# -
export OBS_HOME=${1:-${PWD}}
export OBS_APP_HOST=${2:-"locahost"}
export OBS_APP_PORT=${3:-6000}
export OBS_BIN=${OBS_HOME}/bin
export OBS_DOCKER=${OBS_HOME}/docker
export OBS_ETC=${OBS_HOME}/etc
export OBS_LOGS=${OBS_HOME}/logs
export OBS_PNG=${OBS_HOME}/png
export OBS_SRC=${OBS_HOME}/src
export OBS_PDF=${OBS_HOME}/pdf

export OBS_INSTRUMENTS=${OBS_HOME}/src/instruments
export OBS_MODELS=${OBS_HOME}/src/models
export OBS_OBSERVATIONS=${OBS_HOME}/src/observations
export OBS_TELESCOPES=${OBS_HOME}/src/telescopes
export OBS_TESTS=${OBS_HOME}/src/tests


# +
# database credentials
# -
export OBS_DB_HOST='localhost'
export OBS_DB_NAME='artn'
export OBS_DB_PASS='db_secret'
export OBS_DB_PORT=5432
export OBS_DB_USER='artn'


# +
# PYTHONPATH
# -
_pythonpath=$(env | grep PYTHONPATH | cut -d'=' -f2)
if [[ -z "${_pythonpath}" ]]; then
  export PYTHONPATH=`pwd`
fi
export PYTHONPATH=${OBS_HOME}:${OBS_SRC}:${PYTHONPATH}


# +
# update ephemeris
# -
python3 -c 'from src import *; get_iers()'
