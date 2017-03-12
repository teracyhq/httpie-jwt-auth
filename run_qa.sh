#!/usr/bin/env bash

set -e

pip install -e .
make test
make check-style
make report-coverage
