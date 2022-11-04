#!/usr/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir="/home/christian/gr-HMAC/python"
export GR_CONF_CONTROLPORT_ON=False
export PATH="/home/christian/gr-HMAC/build/python":$PATH
export LD_LIBRARY_PATH="":$LD_LIBRARY_PATH
export PYTHONPATH=/home/christian/gr-HMAC/build/swig:$PYTHONPATH
/usr/bin/python3 /home/christian/gr-HMAC/python/qa_HMAC_verify.py 
