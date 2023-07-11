#!/bin/bash

# example usage:
# $ ./run.sh <../instance.1.in

DIRNAME=`dirname $0`

python3 "$DIRNAME/input.py" | clingo - "$DIRNAME/encoding.lp" | python3 "$DIRNAME/output.py"

