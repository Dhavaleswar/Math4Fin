#!/usr/bin/bash
export PYTHONPATH=$CWD:$PYTHONPATH
export PATH=$CWD:$PATH
JUPYTER_COMMAND="jupyter lab"
echo "Starting Jupyter Lab with command: $JUPYTER_COMMAND"
$JUPYTER_COMMAND