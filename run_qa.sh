#!/usr/bin/env bash

set -e

echo "python --version"
python --version

make resolve
pip install httpie==$HTTPie_VERSION
pip install -e .
make check-style
make test
